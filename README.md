# MAXDATA 在线音效库 v6

App「在线音效」拉取用。清单 **manifest.json**（App 读这个）+ **manifest-v6.json**（同内容，
独立版本文件，绕过 CDN 旧缓存）。

## 内容

| 目录 | 数量 | 命名 |
|---|---|---|
| `talk/` | 88 | `v6_talk_001…` 车外喊话 |
| `lock/` | 100 | `v6_lock_001…` 锁车音效（按类别分：AI语音 / 动漫影视 / 动物自然 / 影视梗 …） |

统一 **16 kHz / 单声道 / 16 bit PCM WAV**，峰值 0.84（−1.5 dBFS），首 4 ms attack、尾 6 ms release。
最长 9.1 秒，App 播放时按功放窗口（约 4 秒）裁剪，不会卡。

## 清单字段

```json
{ "id": "v6_lock_001", "cat": "lock", "category": "动漫影视",
  "label": "蜡笔小新 呱呱呱（动漫影视）", "file": "lock/v6_lock_001.wav",
  "sha256": "…", "size": 433000, "free": true, "ms": 4620 }
```

`category` 是源目录的类别名，方便以后按类目过滤（比如只保留机械/电子提示音）。

## 上传（188 个文件，网页单次上限 100 个）

**网页分批（不需要 token）**：仓库 → Add file → Upload files，分三批：

1. `manifest.json` + `manifest-v6.json`
2. `talk/` 整个文件夹（88 个）
3. `lock/` 整个文件夹（100 个）

**API 一次推完（需要 Token）**：本目录 `upload.ps1`，Token 需 **Contents: Read and write**：

```
$env:GH_TOKEN = "ghp_xxx"
.\upload.ps1 -Mode all
```

## 版本语义

App 拉清单时取「本地快照版本」与「远端最高版本」的较大者，**v6 > v5 > v4 > v3**。
所以 v6 上线后，列表里只有这 188 条；旧条目（`tts_*` / `lib_*` / `v5_*`）不再显示，
文件仍在仓库里，回滚只需把 `manifest.json` 的 version 改回旧值再上传。

## 素材来源

来自用户提供的第三方站点素材（清单 CSV 标注了来源与下载量）。本目录只做格式统一与清单生成，
不改变素材归属；是否公开分发由仓库所有者决定。
