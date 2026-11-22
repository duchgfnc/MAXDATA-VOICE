# MAXDATA 在线音效库

车机 App「车外喊话 / 锁车音效」的在线音频资源仓库。App 联网后从这里拉取清单、按需下载音频到本地播放，新增音效无需重新发布 APK。

## 内容

- `manifest.json` — 音频清单：id / 分类 / 文案 / 相对路径 / sha256 / 字节数 / 是否免费
- `talk/` — 车外喊话音频（20 条）
- `lock/` — 锁车音效（32 条）
- `tools/gen_manifest.py` — 增删音频后重新生成清单
- `tools/labels.json` — id 到中文文案的映射

音频格式统一为 WAV / PCM 16bit / 16000Hz / 单声道，与车机端 PcmPlayer 链路一致。全部为本项目原创文案 + 自有 TTS 合成，无第三方音频素材版权风险，可免费使用。

## 通过 jsDelivr 访问

仓库推送到 GitHub 后，用以下固定地址访问（把 `duchgfnc/MAXDATA-VOICE` 换成你的实际仓库名，`main` 换成你的默认分支）：

```
清单：https://cdn.jsdelivr.net/gh/duchgfnc/MAXDATA-VOICE@main/manifest.json
音频：https://cdn.jsdelivr.net/gh/duchgfnc/MAXDATA-VOICE@main/talk/tts_talk_01.wav
```

`@main` 会跟随分支最新提交，但 jsDelivr 有 60~300 秒缓存。更新音频后如需立即生效，可把 `@main` 改成 `@版本号`（打 Git tag），或调用刷新接口：

```
https://purge.jsdelivr.net/gh/duchgfnc/MAXDATA-VOICE@main/manifest.json
```

## 新增一段音效

1. 用 `tools/gen_voice.py` 的方法合成 WAV（16k/单声道/16bit），按 `tts_talk_NN.wav` 或 `tts_lock_NN.wav` 命名，放进对应目录。
2. 在 `tools/labels.json` 里加上 id 与中文文案。
3. 执行 `python tools/gen_manifest.py`（会递增 version）。
4. 提交推送。App 端检测到 version 变化会刷新清单，用户按需下载新音频。

## 注意

- 本仓库只放音频与清单，不放任何密钥、Token 或个人数据。
- 单文件小于 20MB（jsDelivr 上限），当前每条约 20~60KB。
- 公开仓库即可，无需私有。
