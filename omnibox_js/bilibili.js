// @name 哔哩大全
// @author 
// @description 弹幕：支持
// @dependencies: axios
// @version 1.0.8
// @downloadURL https://gh-proxy.org/https://github.com/Silent1566/OmniBox-Spider/raw/refs/heads/main/综合/哔哩大全.js

/**
 * 哔哩大全 - 极简版（只有一个推荐页面）
 */
const axios = require("axios");
const OmniBox = require("omnibox_sdk");

// ==================== 配置区域 ====================
const BILI_COOKIE = process.env.BILI_COOKIE || "";
const DANMU_API = process.env.DANMU_API || "";

const BILI_HEADERS = {
  "User-Agent":
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
  Referer: "https://www.bilibili.com",
  ...(BILI_COOKIE ? { Cookie: BILI_COOKIE } : {}),
};

const isLoggedIn = () => Boolean(BILI_COOKIE && BILI_COOKIE.includes("SESSDATA="));

// 只有一个分类：推荐
const CLASSES = [
  { type_id: "recommend", type_name: "🔥 热门推荐" },
];

const QUALITY_NAME_MAP = {
  127: "8K 超高清",
  126: "杜比视界",
  125: "HDR 真彩色",
  120: "4K 超清",
  116: "1080P60 高帧率",
  112: "1080P+ 高码率",
  80: "1080P 高清",
  74: "720P60 高帧率",
  64: "720P 高清",
  32: "480P 清晰",
  16: "360P 流畅",
};

function logInfo(msg) {
  OmniBox.log("info", `[BILI-ALL] ${msg}`);
}

function logError(msg, err) {
  OmniBox.log("error", `[BILI-ALL] ${msg}: ${err?.message || err}`);
}

/**
 * 下载图片并转换为Base64
 */
async function downloadImageAsBase64(url) {
  if (!url) return '';
  
  try {
    logInfo(`downloadImageAsBase64: 下载图片 ${url}`);
    
    const response = await axios.get(url, {
      headers: {
        'User-Agent': BILI_HEADERS['User-Agent'],
        'Referer': 'https://www.bilibili.com',
        'Accept': 'image/webp,image/apng,image/*,*/*;q=0.8',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
        'Connection': 'keep-alive',
      },
      responseType: 'arraybuffer',
      timeout: 10000
    });
    
    if (response.status === 200 && response.data) {
      const contentType = response.headers['content-type'] || 'image/jpeg';
      const base64 = Buffer.from(response.data, 'binary').toString('base64');
      const dataUrl = `data:${contentType};base64,${base64}`;
      logInfo(`downloadImageAsBase64: 成功转换为Base64，大小: ${base64.length} 字符`);
      return dataUrl;
    }
  } catch (error) {
    logInfo(`downloadImageAsBase64: 下载失败 ${error.message}`);
  }
  
  return '';
}

/**
 * 获取B站视频封面
 */
async function getCoverBase64(aid) {
  if (!aid) return '';
  
  try {
    logInfo(`getCoverBase64: 获取aid=${aid}的封面`);
    
    const { data } = await axios.get(`https://api.bilibili.com/x/web-interface/view?aid=${aid}`, {
      headers: BILI_HEADERS,
      timeout: 5000
    });
    
    if (data?.code === 0 && data?.data?.pic) {
      const picUrl = data.data.pic;
      logInfo(`getCoverBase64: 获取到封面URL: ${picUrl}`);
      
      const base64 = await downloadImageAsBase64(picUrl);
      if (base64) {
        return base64;
      }
    }
  } catch (error) {
    logInfo(`getCoverBase64: 请求失败: ${error.message}`);
  }
  
  return '';
}

function formatDuration(seconds) {
  const sec = parseInt(seconds, 10) || 0;
  if (sec <= 0) return "00:00";
  const minutes = Math.floor(sec / 60);
  const secs = sec % 60;
  return `${String(minutes).padStart(2, "0")}:${String(secs).padStart(2, "0")}`;
}

function preprocessTitle(title) {
  if (!title) return "";
  return String(title)
    .replace(/4[kK]|[xX]26[45]|720[pP]|1080[pP]|2160[pP]|1280x720|1920x1080/g, " ")
    .replace(/[hH]\.?26[45]/g, " ")
    .replace(/BluRay|WEB-DL|HDR|REMUX/gi, " ")
    .replace(/\.mp4|\.mkv|\.avi|\.flv/gi, " ")
    .trim();
}

function chineseToArabic(cn) {
  const map = {
    零: 0,
    一: 1,
    二: 2,
    三: 3,
    四: 4,
    五: 5,
    六: 6,
    七: 7,
    八: 8,
    九: 9,
    十: 10,
  };
  if (!Number.isNaN(Number(cn))) return parseInt(cn, 10);
  if (cn.length === 1) return map[cn] ?? cn;
  if (cn.length === 2) {
    if (cn[0] === "十") return 10 + (map[cn[1]] || 0);
    if (cn[1] === "十") return (map[cn[0]] || 0) * 10;
  }
  if (cn.length === 3) return (map[cn[0]] || 0) * 10 + (map[cn[2]] || 0);
  return cn;
}

function extractEpisode(title) {
  if (!title) return "";
  const processed = preprocessTitle(title);

  const seMatch = processed.match(/[Ss](?:\d{1,2})?[-._\s]*[Ee](\d{1,3})/i);
  if (seMatch) return seMatch[1];

  const cnMatch = processed.match(/第\s*([零一二三四五六七八九十0-9]+)\s*[集话章节回期]/);
  if (cnMatch) return String(chineseToArabic(cnMatch[1]));

  const epMatch = processed.match(/\b(?:EP|E)[-._\s]*(\d{1,3})\b/i);
  if (epMatch) return epMatch[1];

  const bracketMatch = processed.match(/[\[\(【（](\d{1,3})[\]\)】）]/);
  if (bracketMatch && !["720", "1080", "480"].includes(bracketMatch[1])) {
    return bracketMatch[1];
  }

  return "";
}

function buildFileNameForDanmu(vodName, episodeTitle) {
  if (!vodName) return "";
  if (!episodeTitle || episodeTitle === "正片" || episodeTitle === "播放") return vodName;

  const digits = extractEpisode(episodeTitle);
  if (!digits) return vodName;

  const epNum = parseInt(digits, 10);
  if (!epNum || epNum <= 0) return vodName;
  return epNum < 10 ? `${vodName} S01E0${epNum}` : `${vodName} S01E${epNum}`;
}

function inferFileNameFromURL(url) {
  try {
    const urlObj = new URL(url);
    let base = urlObj.pathname.split("/").pop() || "";
    const dotIndex = base.lastIndexOf(".");
    if (dotIndex > 0) base = base.substring(0, dotIndex);
    base = base.replace(/[_-]/g, " ").replace(/\./g, " ").trim();
    return base || url;
  } catch {
    return url;
  }
}

async function matchDanmu(fileName, cid) {
  if (cid) {
    return [{ name: "B站弹幕", url: `https://api.bilibili.com/x/v1/dm/list.so?oid=${cid}` }];
  }

  if (!DANMU_API || !fileName) return [];

  try {
    const matchUrl = `${DANMU_API}/api/v2/match`;
    const response = await OmniBox.request(matchUrl, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        "User-Agent": BILI_HEADERS["User-Agent"],
      },
      body: JSON.stringify({ fileName }),
    });

    if (response.statusCode !== 200) return [];

    const matchData = JSON.parse(response.body || "{}");
    if (!matchData.isMatched || !Array.isArray(matchData.matches) || matchData.matches.length === 0) {
      return [];
    }

    const firstMatch = matchData.matches[0];
    const episodeId = firstMatch.episodeId;
    if (!episodeId) return [];

    const animeTitle = firstMatch.animeTitle || "";
    const episodeTitle = firstMatch.episodeTitle || "";
    const name = animeTitle && episodeTitle ? `${animeTitle} - ${episodeTitle}` : animeTitle || episodeTitle || "弹幕";

    return [{ name, url: `${DANMU_API}/api/v2/comment/${episodeId}?format=xml` }];
  } catch (error) {
    logError("匹配弹幕失败", error);
    return [];
  }
}

/**
 * 首页 - 热门推荐
 */
async function home(params) {
  try {
    logInfo("开始获取首页推荐数据...");
    
    // 获取热门视频列表，每页20个
    const pg = params.page || 1;
    const url = `https://api.bilibili.com/x/web-interface/popular?ps=20&pn=${pg}`;
    const { data } = await axios.get(url, { headers: BILI_HEADERS, timeout: 5000 });

    logInfo(`首页API返回: code=${data?.code}`);
    
    const items = data?.data?.list || [];
    
    // 并行处理所有封面，提高速度
    const promises = items.map(async (item) => {
      logInfo(`处理视频 ${item.aid} 的封面...`);
      const cover = await getCoverBase64(item.aid);
      
      return {
        vod_id: String(item.aid || ""),
        vod_name: String(item.title || "").replace(/<[^>]*>/g, ""),
        vod_pic: cover || '',
        vod_remarks: formatDuration(item.duration),
      };
    });
    
    const list = await Promise.all(promises);

    logInfo(`首页处理完成，共 ${list.length} 个视频`);
    
    return {
      class: CLASSES,
      list,
    };
  } catch (error) {
    logError("首页获取失败", error);
    return { class: CLASSES, list: [] };
  }
}

/**
 * 分类 - 统一返回推荐页的内容
 */
async function category(params) {
  // 不管传什么分类ID，都返回推荐内容
  return home(params);
}

/**
 * 搜索 - 返回推荐内容（或者可以改为B站搜索）
 */
async function search(params) {
  const keyword = params.keyword || params.wd || "";
  
  // 如果有搜索关键词，返回搜索结果
  if (keyword) {
    try {
      logInfo(`开始搜索: ${keyword}, 页码: ${params.page || 1}`);
      
      const pg = params.page || 1;
      const { data } = await axios.get("https://api.bilibili.com/x/web-interface/search/type", {
        headers: BILI_HEADERS,
        params: {
          search_type: "video",
          keyword,
          page: pg,
        },
        timeout: 5000
      });

      const items = (data?.data?.result || []).filter((item) => item.type === "video");
      
      const promises = items.map(async (item) => {
        const cover = await getCoverBase64(item.aid);
        return {
          vod_id: String(item.aid || ""),
          vod_name: String(item.title || "").replace(/<[^>]*>/g, ""),
          vod_pic: cover || '',
          vod_remarks: item.duration || '',
        };
      });
      
      const list = await Promise.all(promises);

      return {
        page: parseInt(pg),
        pagecount: data?.data?.numPages || 1,
        total: data?.data?.numResults || list.length,
        list,
      };
    } catch (error) {
      logError("搜索失败", error);
    }
  }
  
  // 没有关键词就返回推荐
  return home(params);
}

/**
 * 详情
 */
async function detail(params) {
  const videoId = params.videoId;
  if (!videoId) return { list: [] };

  try {
    logInfo(`获取详情: videoId=${videoId}`);
    
    const { data } = await axios.get(`https://api.bilibili.com/x/web-interface/view?aid=${videoId}`, {
      headers: BILI_HEADERS,
      timeout: 5000
    });

    logInfo(`详情API返回: code=${data?.code}`);
    
    const video = data?.data;
    if (!video) return { list: [] };

    const cover = await getCoverBase64(videoId);

    const episodes = (video.pages || []).map((p, i) => {
      const part = p.part || `第${i + 1}集`;
      return {
        name: part,
        playId: `${videoId}_${p.cid}|${video.title || ""}|${part}`,
      };
    });

    return {
      list: [
        {
          vod_id: String(videoId),
          vod_name: String(video.title || "").replace(/<[^>]*>/g, ""),
          vod_pic: cover || '',
          vod_content: String(video.desc || ""),
          vod_play_sources: [
            {
              name: "B站视频",
              episodes,
            },
          ],
        },
      ],
    };
  } catch (error) {
    logError("详情获取失败", error);
    return { list: [] };
  }
}

/**
 * 播放
 */
async function play(params) {
  let playId = params.playId || "";
  const flag = params.flag || "";

  if (!playId) {
    return { urls: [], parse: 1, header: {}, flag };
  }

  let vodName = "";
  let episodeName = "";

  if (playId.includes("|")) {
    const parts = playId.split("|");
    playId = parts[0] || "";
    vodName = parts[1] || "";
    episodeName = parts[2] || "";
  }

  const idParts = playId.split("_");
  if (idParts.length < 2) {
    return {
      urls: [{ name: "播放", url: playId }],
      parse: /\.(m3u8|mp4|flv)$/i.test(playId) ? 0 : 1,
      header: {},
      flag,
    };
  }

  const avid = idParts[0];
  const cid = idParts[1];
  const loggedIn = isLoggedIn();

  const qualityList = loggedIn
    ? [127, 126, 125, 120, 116, 112, 80, 74, 64, 32, 16]
    : [80, 64, 32, 16];

  const headers = {
    ...BILI_HEADERS,
    Referer: `https://www.bilibili.com/video/av${avid}`,
    Origin: "https://www.bilibili.com",
  };

  const qualitySet = new Set();
  const availableQualities = [];

  for (const qn of qualityList) {
    const useDash = qn > 116;
    try {
      const { data } = await axios.get("https://api.bilibili.com/x/player/playurl", {
        headers,
        params: {
          avid,
          cid,
          qn,
          fnval: useDash ? 4048 : 1,
          fourk: qn >= 120 ? 1 : 0,
          ...(!loggedIn ? { try_look: 1 } : {}),
        },
        timeout: 5000
      });

      if (data?.code !== 0 || !data?.data) continue;

      const payload = data.data;
      const actualQn = payload.quality || qn;
      if (qualitySet.has(actualQn)) continue;
      qualitySet.add(actualQn);

      if (payload.dash?.video?.length) {
        const bestVideo = [...payload.dash.video].sort((a, b) => {
          if ((b.id || 0) !== (a.id || 0)) return (b.id || 0) - (a.id || 0);
          if ((b.bandwidth || 0) !== (a.bandwidth || 0)) return (b.bandwidth || 0) - (a.bandwidth || 0);
          return (b.width || 0) - (a.width || 0);
        })[0];

        const bestAudio = [...(payload.dash.audio || [])].sort((a, b) => (b.bandwidth || 0) - (a.bandwidth || 0))[0];

        if (bestVideo) {
          availableQualities.push({
            name: QUALITY_NAME_MAP[actualQn] || `DASH ${bestVideo.width || "?"}p`,
            url: bestVideo.base_url || bestVideo.baseUrl,
            qn: actualQn,
            audioUrl: bestAudio?.base_url || bestAudio?.baseUrl || "",
          });
        }
      } else if (payload.durl?.[0]?.url) {
        availableQualities.push({
          name: QUALITY_NAME_MAP[actualQn] || `画质${actualQn}`,
          url: payload.durl[0].url,
          qn: actualQn,
          audioUrl: "",
        });
      }
    } catch {
      // 忽略单个画质异常，继续尝试其他画质
    }
  }

  if (availableQualities.length === 0) {
    return {
      urls: [{ name: "播放", url: playId }],
      parse: 1,
      header: headers,
      flag,
    };
  }

  availableQualities.sort((a, b) => b.qn - a.qn);

  const urls = availableQualities.map((q) => ({
    name: q.name,
    url: q.url,
  }));

  const response = {
    urls,
    parse: 0,
    header: {
      "User-Agent": headers["User-Agent"],
      Referer: headers.Referer,
      Origin: headers.Origin,
    },
    flag,
  };

  if (availableQualities[0]?.audioUrl) {
    response.extra = { audio: availableQualities[0].audioUrl };
  }

  let fileName = buildFileNameForDanmu(vodName || params.vodName || "", episodeName || params.episodeName || "");
  if (!fileName && urls[0]?.url) {
    fileName = inferFileNameFromURL(urls[0].url);
  }
  const danmaku = await matchDanmu(fileName, cid);
  if (danmaku.length > 0) {
    response.danmaku = danmaku;
  }

  return response;
}

module.exports = {
  home,
  category,
  search,
  detail,
  play,
};

const runner = require("spider_runner");
runner.run(module.exports);
