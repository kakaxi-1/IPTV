const axios = require("axios");
const https = require("https");
const OmniBox = require("omnibox_sdk");

const API_HOST = 'https://api.guangsuapi.com';
const API_URL = 'https://api.guangsuapi.com/api.php/provide/vod';

const def_headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36',
    'Accept': 'application/json'
};

const axiosInstance = axios.create({
    httpsAgent: new https.Agent({ rejectUnauthorized: false }),
    timeout: 15000
});

const DANMU_API = process.env.DANMU_API || '';

const logInfo = (message, data = null) => {
    const output = data ? `${message}: ${JSON.stringify(data)}` : message;
    OmniBox.log("info", `[光速资源-DEBUG] ${output}`);
};

const logError = (message, error) => {
    OmniBox.log("error", `[光速资源-DEBUG] ${message}: ${error.message || error}`);
};

const encodeMeta = (obj) => {
    try {
        return Buffer.from(JSON.stringify(obj || {}), 'utf8').toString('base64');
    } catch (_) {
        return '';
    }
};

const decodeMeta = (str) => {
    try {
        return JSON.parse(Buffer.from(str || '', 'base64').toString('utf8'));
    } catch (_) {
        return null;
    }
};

const buildScrapedEpisodeName = (scrapeData, mapping, originalName) => {
    if (!mapping || mapping.episodeNumber === 0 || (mapping.confidence && mapping.confidence < 0.5)) {
        return originalName;
    }
    if (mapping.episodeName) {
        return mapping.episodeName;
    }
    if (scrapeData && Array.isArray(scrapeData.episodes)) {
        const hit = scrapeData.episodes.find(
            (ep) => ep.episodeNumber === mapping.episodeNumber && ep.seasonNumber === mapping.seasonNumber
        );
        if (hit?.name) {
            return `${hit.episodeNumber}.${hit.name}`;
        }
    }
    return originalName;
};

function preprocessTitle(title) {
    if (!title) return '';
    return title
        .replace(/4[kK]|[xX]26[45]|720[pP]|1080[pP]|2160[pP]/g, ' ')
        .replace(/[hH]\.?26[45]/g, ' ')
        .replace(/BluRay|WEB-DL|HDR|REMUX/gi, ' ')
        .replace(/\.mp4|\.mkv|\.avi|\.flv/gi, ' ');
}

function chineseToArabic(cn) {
    const map = { '零': 0, '一': 1, '二': 2, '三': 3, '四': 4, '五': 5, '六': 6, '七': 7, '八': 8, '九': 9, '十': 10 };
    if (!isNaN(cn)) return parseInt(cn, 10);
    if (cn.length === 1) return map[cn] || cn;
    if (cn.length === 2) {
        if (cn[0] === '十') return 10 + map[cn[1]];
        if (cn[1] === '十') return map[cn[0]] * 10;
    }
    if (cn.length === 3) return map[cn[0]] * 10 + map[cn[2]];
    return cn;
}

function extractEpisode(title) {
    if (!title) return '';
    const processedTitle = preprocessTitle(title).trim();

    const cnMatch = processedTitle.match(/第\s*([零一二三四五六七八九十0-9]+)\s*[集话章节回期]/);
    if (cnMatch) return String(chineseToArabic(cnMatch[1]));

    const seMatch = processedTitle.match(/[Ss](?:\d{1,2})?[-._\s]*[Ee](\d{1,3})/i);
    if (seMatch) return seMatch[1];

    const epMatch = processedTitle.match(/\b(?:EP|E)[-._\s]*(\d{1,3})\b/i);
    if (epMatch) return epMatch[1];

    const bracketMatch = processedTitle.match(/[\[\(【(](\d{1,3})[\]\)】)]/);
    if (bracketMatch) {
        const num = bracketMatch[1];
        if (!['720', '1080', '480'].includes(num)) return num;
    }

    return '';
}

function buildFileNameForDanmu(vodName, episodeTitle) {
    if (!vodName) return '';
    if (!episodeTitle || episodeTitle === '正片' || episodeTitle === '播放') {
        return vodName;
    }
    const digits = extractEpisode(episodeTitle);
    if (digits) {
        const epNum = parseInt(digits, 10);
        if (epNum > 0) {
            return epNum < 10 ? `${vodName} S01E0${epNum}` : `${vodName} S01E${epNum}`;
        }
    }
    return vodName;
}

function buildScrapedDanmuFileName(scrapeData, scrapeType, mapping, fallbackVodName, fallbackEpisodeName) {
    if (!scrapeData) {
        return buildFileNameForDanmu(fallbackVodName, fallbackEpisodeName);
    }
    if (scrapeType === 'movie') {
        return scrapeData.title || fallbackVodName;
    }
    const title = scrapeData.title || fallbackVodName;
    const seasonAirYear = scrapeData.seasonAirYear || '';
    const seasonNumber = mapping?.seasonNumber || 1;
    const episodeNumber = mapping?.episodeNumber || 1;
    return `${title}.${seasonAirYear}.S${String(seasonNumber).padStart(2, '0')}E${String(episodeNumber).padStart(2, '0')}`;
}

async function matchDanmu(fileName) {
    if (!DANMU_API || !fileName) return [];
    try {
        logInfo(`匹配弹幕: ${fileName}`);
        const matchUrl = `${DANMU_API}/api/v2/match`;
        const response = await OmniBox.request(matchUrl, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
            },
            body: JSON.stringify({ fileName })
        });

        if (response.statusCode !== 200) {
            logInfo(`弹幕匹配失败: HTTP ${response.statusCode}`);
            return [];
        }

        const matchData = JSON.parse(response.body || '{}');
        if (!matchData.isMatched) {
            logInfo('弹幕未匹配到');
            return [];
        }

        const matches = matchData.matches || [];
        if (matches.length === 0) return [];

        const firstMatch = matches[0];
        const episodeId = firstMatch.episodeId;
        const animeTitle = firstMatch.animeTitle || '';
        const episodeTitle = firstMatch.episodeTitle || '';
        if (!episodeId) return [];

        let danmakuName = '弹幕';
        if (animeTitle && episodeTitle) danmakuName = `${animeTitle} - ${episodeTitle}`;
        else if (animeTitle) danmakuName = animeTitle;
        else if (episodeTitle) danmakuName = episodeTitle;

        const danmakuURL = `${DANMU_API}/api/v2/comment/${episodeId}?format=xml`;
        logInfo(`弹幕匹配成功: ${danmakuName}`);
        return [{ name: danmakuName, url: danmakuURL }];
    } catch (error) {
        logInfo(`弹幕匹配失败: ${error.message}`);
        return [];
    }
}

function formatVideos(list) {
    if (!Array.isArray(list)) return [];
    return list.map(item => {
        if (!item || typeof item !== 'object') return null;
        return {
            vod_id: String(item.vod_id || ''),
            vod_name: String(item.vod_name || ''),
            vod_pic: String(item.vod_pic || ''),
            type_id: String(item.type_id || ''),
            type_name: String(item.type_name || ''),
            vod_year: String(item.vod_year || ''),
            vod_remarks: String(item.vod_remarks || ''),
            vod_time: String(item.vod_time || ''),
            vod_play_from: String(item.vod_play_from || 'default'),
            vod_play_url: String(item.vod_play_url || ''),
            vod_en: String(item.vod_en || '')
        };
    }).filter(v => v && v.vod_id);
}

function formatDetailVideos(list) {
    if (!Array.isArray(list)) return [];
    return list.map(item => {
        if (!item || typeof item !== 'object') return null;
        const vod = {
            vod_id: String(item.vod_id || ''),
            vod_name: String(item.vod_name || ''),
            vod_pic: String(item.vod_pic || ''),
            type_name: String(item.type_name || ''),
            vod_year: String(item.vod_year || ''),
            vod_area: String(item.vod_area || ''),
            vod_remarks: String(item.vod_remarks || ''),
            vod_actor: String(item.vod_actor || ''),
            vod_director: String(item.vod_director || ''),
            vod_content: String(item.vod_content || '').trim(),
            vod_play_from: String(item.vod_play_from || 'default'),
            vod_play_url: String(item.vod_play_url || ''),
            vod_en: String(item.vod_en || '')
        };
        
        vod.vod_play_sources = parsePlaySources(vod);
        
        return vod;
    }).filter(v => v && v.vod_id);
}

async function enrichVideosWithDetails(videos) {
    if (!Array.isArray(videos) || videos.length === 0) return videos;
    const videoIDs = [];
    const videoMap = new Map();
    for (const video of videos) {
        if (!video.vod_pic || video.vod_pic === '' || video.vod_pic === '<nil>') {
            videoIDs.push(video.vod_id);
            videoMap.set(video.vod_id, video);
        }
    }
    if (videoIDs.length === 0) return videos;
    const batchSize = 20;
    for (let i = 0; i < videoIDs.length; i += batchSize) {
        const end = Math.min(i + batchSize, videoIDs.length);
        const batchIDs = videoIDs.slice(i, end);
        try {
            const response = await axiosInstance.get(API_URL, {
                params: { ac: 'videolist', ids: batchIDs.join(',') },
                headers: def_headers
            });
            const data = response.data;
            if (Array.isArray(data.list)) {
                for (const item of data.list) {
                    if (!item || typeof item !== 'object') continue;
                    const vodId = String(item.vod_id || '');
                    const originalVod = videoMap.get(vodId);
                    if (originalVod) {
                        const pic = String(item.vod_pic || '');
                        if (pic && pic !== '<nil>') {
                            originalVod.vod_pic = pic;
                            logInfo(`补全视频 ${vodId} 封面: ${pic}`);
                        }
                        const year = String(item.vod_year || '');
                        if (year && year !== '<nil>') {
                            originalVod.vod_year = year;
                        }
                    }
                }
            }
        } catch (error) {
            logError(`批量获取详情失败`, error);
        }
    }
    return videos;
}

const parsePlaySources = (vodItem) => {
    const playSources = [];
    
    const vodId = vodItem.vod_id;
    const vodName = vodItem.vod_name;
    const playFrom = vodItem.vod_play_from || 'default';
    const playUrl = vodItem.vod_play_url || '';
    
    if (playUrl) {
        logInfo(`检测到直接播放地址: ${playUrl.substring(0, 100)}...`);
        
        const episodes = playUrl.split('#').map((item, index) => {
            const parts = item.split('$');
            const episodeName = parts[0] || `第${index + 1}集`;
            const directUrl = parts[1] || '';
            
            const fid = `${vodId}#${index}`;
            const playMeta = {
                sid: vodId,
                fid: fid,
                v: vodName,
                e: index + 1,
                url: directUrl,
                isDirect: true
            };
            
            return {
                name: episodeName,
                playId: `${directUrl}|||${encodeMeta(playMeta)}`,
                _fid: fid,
                _rawName: episodeName,
                _url: directUrl
            };
        }).filter(ep => ep.playId);
        
        if (episodes.length > 0) {
            playSources.push({
                name: playFrom,
                episodes: episodes
            });
        }
    } else {
        logInfo(`未检测到直接地址，使用播放页模式`);
        
        const episodes = [{
            name: '正片',
            playId: `need_resolve:${vodId}|||${encodeMeta({ 
                sid: vodId, 
                fid: `${vodId}#0`, 
                v: vodName, 
                e: 1,
                playFrom: playFrom
            })}`,
            _fid: `${vodId}#0`,
            _rawName: '正片'
        }];
        
        playSources.push({
            name: playFrom,
            episodes: episodes
        });
    }
    
    return playSources;
};

const PLAY_URL_PATTERNS = [
    (vodId) => `${API_HOST}/play/${vodId}.html`,
    (vodId) => `${API_HOST}/vod/play/${vodId}.html`,
    (vodId) => `${API_HOST}/vod/${vodId}.html`,
    (vodId) => `${API_HOST}/detail/${vodId}.html`,
    (vodId) => `${API_HOST}/movie/${vodId}.html`,
    (vodId) => `${API_HOST}/index.php/vod/play/id/${vodId}.html`,
    (vodId) => `${API_HOST}/vodplay/${vodId}.html`,
    (vodId) => `${API_HOST}/videoplay/${vodId}.html`,
];

async function getPlayPageUrlSmart(vodId, playFrom = 'default') {
    for (const pattern of PLAY_URL_PATTERNS) {
        try {
            const testUrl = pattern(vodId);
            logInfo(`尝试播放页URL: ${testUrl}`);
            
            const headResponse = await axiosInstance.head(testUrl, { timeout: 3000 }).catch(() => null);
            if (headResponse && headResponse.status === 200) {
                logInfo(`发现有效播放页: ${testUrl}`);
                return testUrl;
            }
        } catch (e) {
        }
    }
    
    logInfo(`未探测到有效播放页，使用默认格式: ${API_HOST}/play/${vodId}.html`);
    return `${API_HOST}/play/${vodId}.html`;
}

async function home(params) {
    logInfo("进入首页");
    try {
        const res = await axiosInstance.get(API_URL, { 
            params: { ac: 'list', pg: 1, pagesize: 20 },
            headers: def_headers 
        });
        const data = res.data;
        let videos = formatVideos(data.list || []);
        videos = await enrichVideosWithDetails(videos);
        const classes = (data.class || []).map(item => ({
            type_id: String(item.type_id),
            type_name: item.type_name
        }));
        logInfo(`首页获取到 ${videos.length} 个视频，补全后带封面的视频: ${videos.filter(v => v.vod_pic).length} 个`);
        return { list: videos, class: classes, filters: {} };
    } catch (e) {
        logError("首页请求失败", e);
        return { list: [], class: [] };
    }
}

async function category(params) {
    const { categoryId, page } = params;
    const pg = parseInt(page) || 1;
    logInfo(`请求分类: ${categoryId}, 页码: ${pg}`);
    try {
        const res = await axiosInstance.get(API_URL, {
            params: { ac: 'list', t: categoryId, pg: pg, pagesize: 20 },
            headers: def_headers
        });
        const data = res.data;
        let videos = formatVideos(data.list || []);
        videos = await enrichVideosWithDetails(videos);
        logInfo(`分类结果: ${videos.length}条, 总页数: ${data.pagecount}, 带封面的视频: ${videos.filter(v => v.vod_pic).length} 个`);
        return {
            list: videos,
            page: pg,
            pagecount: data.pagecount || 1
        };
    } catch (e) {
        logError("分类请求失败", e);
        return { list: [], page: pg, pagecount: 0 };
    }
}

async function search(params) {
    const wd = params.keyword || params.wd || "";
    const pg = parseInt(params.page) || 1;
    logInfo(`搜索关键词: ${wd}, 页码: ${pg}`);
    try {
        const res = await axiosInstance.get(API_URL, {
            params: { ac: 'list', wd: wd, pg: pg, pagesize: 100 },
            headers: def_headers
        });
        const data = res.data;
        let videos = formatVideos(data.list || []);
        videos = await enrichVideosWithDetails(videos);
        logInfo(`搜索结果: ${videos.length}条, 总页数: ${data.pagecount}, 总条数: ${data.total || '未知'}`);
        return {
            list: videos,
            page: pg,
            pagecount: data.pagecount || 1,
            total: data.total || 0
        };
    } catch (e) {
        logError("搜索失败", e);
        return { list: [], page: pg, pagecount: 0, total: 0 };
    }
}

async function detail(params, context) {
    const videoId = params.videoId;
    logInfo(`请求详情: ${videoId}`);
    try {
        const res = await axiosInstance.get(API_URL, {
            params: { ac: 'videolist', ids: videoId },
            headers: def_headers
        });
        const data = res.data;
        let videos = formatDetailVideos(data.list || []);
        if (videos.length === 0) return { list: [] };
        const vod = videos[0];
        
        const sourceCandidates = [];
        const playSources = Array.isArray(vod.vod_play_sources) ? vod.vod_play_sources : [];
        for (const source of playSources) {
            for (const ep of source.episodes || []) {
                const meta = ep.playId && ep.playId.includes('|||') ? decodeMeta(ep.playId.split('|||')[1]) : {};
                const fid = ep._fid || meta.fid;
                const rawName = ep._rawName || ep.name || '正片';
                if (!fid) continue;
                sourceCandidates.push({
                    fid: fid,
                    file_id: fid,
                    file_name: rawName,
                    name: rawName,
                    format_type: 'video'
                });
            }
        }
        
        if (sourceCandidates.length > 0 && vod.vod_name) {
            try {
                const sourceId = `spider_source_${context.sourceId}_${videoId}`;
                await OmniBox.processScraping(
                    sourceId,
                    vod.vod_name,
                    vod.vod_name,
                    sourceCandidates
                );
                
                const metadata = await OmniBox.getScrapeMetadata(sourceId);
                const scrapeData = metadata?.scrapeData || null;
                const videoMappings = metadata?.videoMappings || [];
                
                if (scrapeData) {
                    vod.vod_name = scrapeData.title || scrapeData.name || vod.vod_name;
                    if (scrapeData.poster_path) {
                        vod.vod_pic = `https://image.tmdb.org/t/p/w500${scrapeData.poster_path}`;
                        logInfo(`刮削封面成功: ${vod.vod_pic}`);
                    }
                    vod.vod_year = scrapeData.releaseDate ? String(scrapeData.releaseDate).substring(0, 4) : vod.vod_year;
                    vod.vod_content = scrapeData.overview || vod.vod_content;
                    if (scrapeData.credits?.cast) {
                        vod.vod_actor = scrapeData.credits.cast.slice(0, 5).map(c => c.name).join(',');
                    }
                    if (scrapeData.credits?.crew) {
                        const directors = scrapeData.credits.crew
                            .filter(c => c.job === 'Director')
                            .slice(0, 3)
                            .map(c => c.name)
                            .join(',');
                        if (directors) vod.vod_director = directors;
                    }
                    
                    for (const source of playSources) {
                        for (const ep of source.episodes || []) {
                            const meta = ep.playId && ep.playId.includes('|||') ? decodeMeta(ep.playId.split('|||')[1]) : {};
                            const fid = ep._fid || meta.fid;
                            const mapping = videoMappings.find(m => m?.fileId === fid);
                            if (!mapping) continue;
                            
                            const oldName = ep.name;
                            const newName = buildScrapedEpisodeName(scrapeData, mapping, oldName);
                            if (newName && newName !== oldName) {
                                ep.name = newName;
                            }
                            
                            ep._seasonNumber = mapping.seasonNumber;
                            ep._episodeNumber = mapping.episodeNumber;
                        }
                        
                        const hasEpisodeNumber = (source.episodes || []).some(
                            ep => ep._episodeNumber !== undefined && ep._episodeNumber !== null
                        );
                        if (hasEpisodeNumber) {
                            source.episodes.sort((a, b) => {
                                const seasonA = a._seasonNumber || 0;
                                const seasonB = b._seasonNumber || 0;
                                if (seasonA !== seasonB) return seasonA - seasonB;
                                const episodeA = a._episodeNumber || 0;
                                const episodeB = b._episodeNumber || 0;
                                return episodeA - episodeB;
                            });
                        }
                        
                        source.episodes = (source.episodes || []).map(ep => ({
                            name: ep.name,
                            playId: ep.playId
                        }));
                    }
                    
                    vod.vod_play_sources = playSources;
                }
            } catch (error) {
                logError("刮削处理失败", error);
            }
        }
        
        logInfo(`详情获取成功: ${vod.vod_name}, 封面: ${vod.vod_pic ? '有' : '无'}`);
        return { list: [vod] };
    } catch (e) {
        logError("详情获取失败", e);
        return { list: [] };
    }
}

async function play(params, context) {
    const rawPlayId = params.playId || '';
    const flag = params.flag || '';
    
    logInfo(`准备播放: ${rawPlayId}, flag: ${flag}`);

    let playUrl = rawPlayId;
    let vodName = '';
    let episodeName = '';
    let isDirectAddress = false;

    if (rawPlayId.includes('|||')) {
        const [mainPlayId, metaB64] = rawPlayId.split('|||');
        const meta = decodeMeta(metaB64 || '');
        vodName = meta.v || '';
        episodeName = meta.e || '';
        isDirectAddress = meta.isDirect || false;
        
        if (isDirectAddress) {
            playUrl = mainPlayId;
            logInfo(`使用直接播放地址: ${playUrl}`);
        }
        else if (mainPlayId.startsWith('need_resolve:')) {
            const resolveVodId = mainPlayId.split(':')[1] || meta.sid;
            if (resolveVodId) {
                const playPageUrl = await getPlayPageUrlSmart(resolveVodId, meta.playFrom);
                playUrl = playPageUrl;
                logInfo(`智能解析到播放页: ${playUrl}`);
            }
        } else {
            playUrl = mainPlayId;
        }
    }

    let scrapedDanmuFileName = '';
    try {
        const sourceVideoId = params.vodId || (rawPlayId.includes('|||') ? (decodeMeta(rawPlayId.split('|||')[1] || '').sid || '') : '');
        if (sourceVideoId) {
            const sourceId = `spider_source_${context.sourceId}_${sourceVideoId}`;
            const metadata = await OmniBox.getScrapeMetadata(sourceId);
            
            if (metadata && metadata.scrapeData) {
                const meta = rawPlayId.includes('|||') ? decodeMeta(rawPlayId.split('|||')[1] || '') : {};
                const mapping = (metadata.videoMappings || []).find(m => m?.fileId === meta.fid);
                
                scrapedDanmuFileName = buildScrapedDanmuFileName(
                    metadata.scrapeData,
                    metadata.scrapeType || '',
                    mapping,
                    vodName,
                    episodeName
                );
                
                if (metadata.scrapeData.title) {
                    vodName = metadata.scrapeData.title;
                }
                if (mapping?.episodeName) {
                    episodeName = mapping.episodeName;
                }
            }
        }
    } catch (error) {
        logError("获取刮削元数据失败", error);
    }

    let resolvedUrl = playUrl;
    let resolvedHeader = {};
    let parse = 1;

    const isDirectPlayable = /\.(m3u8|mp4|flv|avi|mkv|ts)(?:\?|#|$)/i.test(playUrl || '');
    
    if (isDirectPlayable || isDirectAddress) {
        parse = 0;
        logInfo(`使用直接播放地址: ${playUrl}`);
    } 
    else if (/^https?:\/\//i.test(playUrl || '')) {
        try {
            const sniffResult = await OmniBox.sniffVideo(playUrl);
            if (sniffResult && sniffResult.url) {
                resolvedUrl = sniffResult.url;
                resolvedHeader = sniffResult.header || {};
                parse = 0;
                logInfo(`嗅探成功: ${resolvedUrl}`);
            }
        } catch (sniffError) {
            logError(`嗅探失败`, sniffError);
        }
    }

    const response = {
        urls: [{ 
            name: '默认线路', 
            url: resolvedUrl 
        }],
        flag: flag,
        header: resolvedHeader,
        parse: parse
    };

    if (DANMU_API) {
        let fileName = '';
        if (vodName) {
            fileName = scrapedDanmuFileName || buildFileNameForDanmu(vodName, episodeName);
        }
        
        if (fileName) {
            const danmakuList = await matchDanmu(fileName);
            if (danmakuList && danmakuList.length > 0) {
                response.danmaku = danmakuList;
                logInfo('弹幕已添加到播放响应');
            }
        }
    }

    return response;
}

module.exports = { home, category, search, detail, play };

const runner = require("spider_runner");
runner.run(module.exports);