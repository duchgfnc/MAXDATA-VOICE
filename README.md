# MAXDATA 在线音效库

车机 App「车外喊话 / 锁车音效」的在线音频资源仓库。App 联网后从这里拉取清单、按需下载音频到本地播放，新增音效无需重新发布 APK。

## 内容

- `manifest.json` — 音频清单：id / 分类 / 文案 / 相对路径 / sha256 / 字节数 / 是否免费（version=3，共 150 条）
- `talk/` — 车外喊话音频（50 条：礼貌让行、安全警示、停车进出、夜间灯光、充电、恶劣天气、行人孩童、搞怪整活）
- `lock/` — 锁车音效（100 条：商务确认、温馨道别、萌系、东北幽默、干饭打工人、仪式感、短提示音）
- `tools/gen_manifest.py` — 增删音频后重新生成清单
- `tools/labels.json` — id 到中文文案的映射（150 条）

**与 APK 内置音效零冲突**：本仓库已剔除所有与 APK 内置相同的 id
（`tts_talk_01..20`、`tts_lock_01..32`）和文案（共 58 条）。在线条目从
`tts_talk_21` / `tts_lock_33` 起编号；下载后不会覆盖内置音效在
`cacheDir/fx/` 下的缓存文件，列表里也不会与内置项重名。

音频格式统一为 WAV / PCM 16bit / 16000Hz / 单声道，与车机端 PcmPlayer 链路一致。全部为本项目原创文案 + 公开中文 TTS 自行合成，只取用车场景与口语梗的语义，不复制任何第三方 IP 原声、影视台词或现成音频文件，无版权风险，可免费使用。锁车音效均短于 2 秒，符合非 23 控制器的短音效预算。

## 通过 jsDelivr 访问

仓库推送到 GitHub 后，用以下固定地址访问（把 `duchgfnc/MAXDATA-VOICE` 换成你的实际仓库名，`main` 换成你的默认分支）：

```
清单：https://cdn.jsdelivr.net/gh/duchgfnc/MAXDATA-VOICE@main/manifest.json
音频：https://cdn.jsdelivr.net/gh/duchgfnc/MAXDATA-VOICE@main/talk/tts_talk_21.wav
```

`@main` 会跟随分支最新提交，但 jsDelivr 有 60~300 秒缓存。更新音频后如需立即生效，可把 `@main` 改成 `@版本号`（打 Git tag），或调用刷新接口：

```
https://purge.jsdelivr.net/gh/duchgfnc/MAXDATA-VOICE@main/manifest.json
```

## 新增一段音效

1. 用 `tools/gen_voice.py` 的方法合成 WAV（16k/单声道/16bit），按 `tts_talk_NN.wav` 或 `tts_lock_NN.wav` 命名，放进对应目录。编号必须避开 APK 内置段（talk ≤ 20 / lock ≤ 32），文案也不要与内置重名，否则会覆盖缓存、列表重名。
2. 在 `tools/labels.json` 里加上 id 与中文文案。
3. 执行 `python tools/gen_manifest.py`（会递增 version）。
4. 提交推送。App 端检测到 version 变化会刷新清单，用户按需下载新音频。

## 注意

- 本仓库只放音频与清单，不放任何密钥、Token 或个人数据。
- 单文件小于 20MB（jsDelivr 上限），当前每条约 20~60KB。
- 公开仓库即可，无需私有。
