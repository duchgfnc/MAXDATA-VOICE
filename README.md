# MAXDATA 锁车音效库 · 分类版

车机 App「锁车音效 / 车外喊话」的在线音频仓库。**锁车音效 215 条，按 8 个类别分目录**，另含车外喊话 88 条。App 联网后拉 `manifest.json`，按需下载到本地播放，新增音效不用重发 APK。

> 版本 **v7** ｜ 条目 **303** ｜ 体积 **55.8 MB** ｜ 清单 `manifest.json` / `manifest-v7.json`

## 按类别找音效

| 类别 | 数量 | 目录 | 说明 |
|---|---:|---|---|
| **网络热梗** | 103 | [`lock/meme/`](lock/meme/) | 短视频热梗、口头禅、搞笑段子 |
| **动漫影视** | 25 | [`lock/anime/`](lock/anime/) | 蜡笔小新、皮卡丘、海绵宝宝、小猪佩奇等动画角色梗 |
| **AI语音** | 22 | [`lock/ai/`](lock/ai/) | AI 合成的提示语、贾维斯式播报、巡逻/哨兵口令 |
| **游戏音效** | 18 | [`lock/game/`](lock/game/) | 超级玛丽、斗地主、吃鸡等游戏音 |
| **动物自然** | 15 | [`lock/animal/`](lock/animal/) | 青蛙、鸟叫、虫鸣等自然拟声 |
| **影视梗** | 11 | [`lock/tv/`](lock/tv/) | 影视台词、恐怖音效、皇上驾到等剧情梗 |
| **机械车辆** | 11 | [`lock/machine/`](lock/machine/) | 引擎、气刹、电动车提示音等机械/车辆声 |
| **系统数码** | 10 | [`lock/system/`](lock/system/) | Windows 关机、开机音、提示音等系统声 |
| 车外喊话 | 88 | [`talk/`](talk/) | 礼貌通行 / 玩梗社死 / 安全警示等 6 类 |

## 三种用法

**1. 网页直接试听**：浏览器打开 [`index.html`](index.html)（或 GitHub Pages），按类别筛选、搜索、点一下就能听，不用下载。

**2. 特斯拉 / 极氪 / 领克 / 小鹏（Boombox）**：下载任意 wav，改名 `LockChime.wav`，U 盘根目录建 `Boombox` 文件夹放进去（和 `TeslaCam` 同一层），插车 → 控制 → 锁车音效 → 选 Boombox。

**3. MAXDATA 车机 App**：功能 → 锁车音效 → 在线音效，选类别下载即可（自动校验 SHA-256）。

## CDN 地址（App 用，四源自动回退）

```
https://cdn.jsdmirror.com/gh/duchgfnc/MAXDATA-VOICE@main/manifest.json
https://jsd.onmicrosoft.cn/gh/duchgfnc/MAXDATA-VOICE@main/manifest.json
https://jsd.cdn.zzko.cn/gh/duchgfnc/MAXDATA-VOICE@main/manifest.json
https://cdn.jsdelivr.net/gh/duchgfnc/MAXDATA-VOICE@main/manifest.json

单条音频：https://<上面的域名>/gh/duchgfnc/MAXDATA-VOICE@main/lock/meme/v7_lock_001.wav
```

## 目录结构

```
lock/
  meme/    103 条
  anime/   25 条
  ai/      22 条
  game/    18 条
  animal/  15 条
  tv/      11 条
  machine/ 11 条
  system/  10 条
talk/              88 条
manifest.json      清单（version 7）
manifest-v7.json   同一份副本（绕 CDN 对固定路径的旧缓存）
index.html         分类试听台
```

## 分类清单

<details>
<summary><b>点开看全部 215 条</b></summary>


### 网络热梗（103）

| # | 音效 | 时长 | 下载量 | 文件 |
|---:|---|---:|---:|---|
| 9 | 曼波 | 0:01 | 20401 | [`v7_lock_009.wav`](lock/meme/v7_lock_009.wav) |
| 11 | 小飞棍来咯 | 0:02 | 17416 | [`v7_lock_011.wav`](lock/meme/v7_lock_011.wav) |
| 13 | 害嗨害 | 0:01 | 15536 | [`v7_lock_013.wav`](lock/meme/v7_lock_013.wav) |
| 16 | 你干嘛 | 0:04 | 14492 | [`v7_lock_015.wav`](lock/meme/v7_lock_015.wav) |
| 20 | 晚安 巴卡巴卡 | 0:04 | 13052 | [`v7_lock_019.wav`](lock/meme/v7_lock_019.wav) |
| 21 | 大司马的笑声(1) | 0:05 | 12180 | [`v7_lock_020.wav`](lock/meme/v7_lock_020.wav) |
| 26 | 雷军are u ok | 0:01 | 10457 | [`v7_lock_024.wav`](lock/meme/v7_lock_024.wav) |
| 30 | 歪比巴卜 | 0:01 | 10041 | [`v7_lock_028.wav`](lock/meme/v7_lock_028.wav) |
| 31 | Labubu可爱俏皮版 | 0:03 | 9907 | [`v7_lock_029.wav`](lock/meme/v7_lock_029.wav) |
| 33 | oi 借过一下 | 0:04 | 9677 | [`v7_lock_031.wav`](lock/meme/v7_lock_031.wav) |
| 35 | 给我擦皮鞋（纯人声版） | 0:01 | 9543 | [`v7_lock_033.wav`](lock/meme/v7_lock_033.wav) |
| 47 | oi放大音量版 | 0:01 | 8427 | [`v7_lock_044.wav`](lock/meme/v7_lock_044.wav) |
| 50 | 我勒个豆(18) | 0:02 | 8223 | [`v7_lock_046.wav`](lock/meme/v7_lock_046.wav) |
| 51 | 遥遥领先 | 0:02 | 8216 | [`v7_lock_047.wav`](lock/meme/v7_lock_047.wav) |
| 55 | 我的刀盾 | 0:01 | 7440 | [`v7_lock_051.wav`](lock/meme/v7_lock_051.wav) |
| 61 | 一giao我里giao | 0:03 | 6484 | [`v7_lock_057.wav`](lock/meme/v7_lock_057.wav) |
| 70 | yeeeeee～aboom | 0:03 | 5954 | [`v7_lock_064.wav`](lock/meme/v7_lock_064.wav) |
| 79 | 呜嗦呜嗦 | 0:06 | 5310 | [`v7_lock_072.wav`](lock/meme/v7_lock_072.wav) |
| 80 | 性能收束 | 0:04 | 5284 | [`v7_lock_073.wav`](lock/meme/v7_lock_073.wav) |
| 85 | 比比拉不 | 0:01 | 5211 | [`v7_lock_076.wav`](lock/meme/v7_lock_076.wav) |
| 86 | 巴巴博一 | 0:01 | 5197 | [`v7_lock_077.wav`](lock/meme/v7_lock_077.wav) |
| 91 | 理想进行曲短 | 0:05 | 4979 | [`v7_lock_081.wav`](lock/meme/v7_lock_081.wav) |
| 92 | 钵钵鸡 | 0:04 | 4958 | [`v7_lock_082.wav`](lock/meme/v7_lock_082.wav) |
| 93 | 曼波三连 | 0:04 | 4939 | [`v7_lock_083.wav`](lock/meme/v7_lock_083.wav) |
| 94 | 来了老弟？ | 0:02 | 4927 | [`v7_lock_084.wav`](lock/meme/v7_lock_084.wav) |
| 103 | byebye小孩声音 | 0:01 | 4723 | [`v7_lock_088.wav`](lock/meme/v7_lock_088.wav) |
| 105 | 噔 | 0:01 | 4605 | [`v7_lock_089.wav`](lock/meme/v7_lock_089.wav) |
| 108 | 动感光波 | 0:02 | 4406 | [`v7_lock_091.wav`](lock/meme/v7_lock_091.wav) |
| 109 | 绫波丽再见 | 0:03 | 4374 | [`v7_lock_092.wav`](lock/meme/v7_lock_092.wav) |
| 113 | CS下包 | 0:04 | 4302 | [`v7_lock_095.wav`](lock/meme/v7_lock_095.wav) |
| 116 | 哈喽关锁声音 | 0:05 | 4216 | [`v7_lock_096.wav`](lock/meme/v7_lock_096.wav) |
| 120 | Timi.(7) | 0:02 | 4103 | [`v7_lock_099.wav`](lock/meme/v7_lock_099.wav) |
| 125 | 道路千万条，安全第一条 | 0:11 | 4049 | [`v7_lock_101.wav`](lock/meme/v7_lock_101.wav) |
| 126 | YU7_GT | 0:10 | 3966 | [`v7_lock_102.wav`](lock/meme/v7_lock_102.wav) |
| 128 | 赌神出场 | 0:05 | 3910 | [`v7_lock_104.wav`](lock/meme/v7_lock_104.wav) |
| 130 | 塞尔达 呀哈哈(17) | 0:02 | 3886 | [`v7_lock_105.wav`](lock/meme/v7_lock_105.wav) |
| 131 | 麦当劳张嘟嘟版 | 0:02 | 3884 | [`v7_lock_106.wav`](lock/meme/v7_lock_106.wav) |
| 134 | 你是来拉屎的吧 | 0:01 | 3836 | [`v7_lock_107.wav`](lock/meme/v7_lock_107.wav) |
| 137 | 敖闰-大哥怕是忘了小妹的能耐 | 0:03 | 3793 | [`v7_lock_108.wav`](lock/meme/v7_lock_108.wav) |
| 138 | 长城炮 | 0:07 | 3781 | [`v7_lock_109.wav`](lock/meme/v7_lock_109.wav) |
| 139 | 巴别塔身份认证 | 0:04 | 3701 | [`v7_lock_110.wav`](lock/meme/v7_lock_110.wav) |
| 140 | 关锁成功 请带好随身物品 哈罗 | 0:03 | 3679 | [`v7_lock_111.wav`](lock/meme/v7_lock_111.wav) |
| 142 | [莱德队长]汪汪队出发 | 0:01 | 3666 | [`v7_lock_113.wav`](lock/meme/v7_lock_113.wav) |
| 145 | labubu1 | 0:04 | 3570 | [`v7_lock_115.wav`](lock/meme/v7_lock_115.wav) |
| 147 | 拔剑声 | 0:01 | 3531 | [`v7_lock_116.wav`](lock/meme/v7_lock_116.wav) |
| 148 | 尴尬结束 | 0:04 | 3492 | [`v7_lock_117.wav`](lock/meme/v7_lock_117.wav) |
| 149 | 开心消消乐背景音效 | 0:01 | 3492 | [`v7_lock_118.wav`](lock/meme/v7_lock_118.wav) |
| 150 | 麦当劳纯音乐 | 0:03 | 3451 | [`v7_lock_119.wav`](lock/meme/v7_lock_119.wav) |
| 151 | 解闭锁音 | 0:01 | 3414 | [`v7_lock_120.wav`](lock/meme/v7_lock_120.wav) |
| 153 | 理想进行曲 | 0:09 | 3388 | [`v7_lock_121.wav`](lock/meme/v7_lock_121.wav) |
| 156 | 只因你太美 | 0:04 | 3290 | [`v7_lock_122.wav`](lock/meme/v7_lock_122.wav) |
| 157 | 江江 | 0:01 | 3285 | [`v7_lock_123.wav`](lock/meme/v7_lock_123.wav) |
| 167 | 英雄联盟伊泽瑞尔-是时候表演真正的技术了 | 0:02 | 3144 | [`v7_lock_126.wav`](lock/meme/v7_lock_126.wav) |
| 168 | 悬疑哈基米 | 0:07 | 3138 | [`v7_lock_127.wav`](lock/meme/v7_lock_127.wav) |
| 169 | 嘎子 百事可乐 | 0:04 | 3119 | [`v7_lock_128.wav`](lock/meme/v7_lock_128.wav) |
| 172 | 是表哥吗 | 0:03 | 3043 | [`v7_lock_131.wav`](lock/meme/v7_lock_131.wav) |
| 173 | 假面骑士555待机 | 0:03 | 3013 | [`v7_lock_132.wav`](lock/meme/v7_lock_132.wav) |
| 175 | 你才是奶龙 | 0:04 | 2962 | [`v7_lock_133.wav`](lock/meme/v7_lock_133.wav) |
| 177 | 我踏马来啦(19) | 0:01 | 2942 | [`v7_lock_134.wav`](lock/meme/v7_lock_134.wav) |
| 179 | 哥哥姐姐让下，我要倒车啦（苏浩宸） | 0:05 | 2921 | [`v7_lock_135.wav`](lock/meme/v7_lock_135.wav) |
| 186 | 哈吉米 | 0:03 | 2807 | [`v7_lock_137.wav`](lock/meme/v7_lock_137.wav) |
| 187 | 提莫队长正在待命 | 0:02 | 2762 | [`v7_lock_138.wav`](lock/meme/v7_lock_138.wav) |
| 189 | 是表哥吗？呃。。是表弟呀！表哥。。。 | 0:05 | 2761 | [`v7_lock_139.wav`](lock/meme/v7_lock_139.wav) |
| 193 | 哟呵 | 0:01 | 2740 | [`v7_lock_140.wav`](lock/meme/v7_lock_140.wav) |
| 195 | 打嗝音效 | 0:02 | 2722 | [`v7_lock_141.wav`](lock/meme/v7_lock_141.wav) |
| 203 | 公主请上车（猴哥） | 0:02 | 2625 | [`v7_lock_144.wav`](lock/meme/v7_lock_144.wav) |
| 204 | 阿豆 | 0:02 | 2618 | [`v7_lock_145.wav`](lock/meme/v7_lock_145.wav) |
| 205 | 网飞片头 | 0:04 | 2592 | [`v7_lock_146.wav`](lock/meme/v7_lock_146.wav) |
| 210 | 蛋仔派对（嘎哒嘎哒） | 0:02 | 2502 | [`v7_lock_147.wav`](lock/meme/v7_lock_147.wav) |
| 213 | 新年快乐 恭喜发财 | 0:02 | 2488 | [`v7_lock_149.wav`](lock/meme/v7_lock_149.wav) |
| 214 | 东京热11-车友 | 0:07 | 2485 | [`v7_lock_150.wav`](lock/meme/v7_lock_150.wav) |
| 215 | 青花瓷 | 0:05 | 2482 | [`v7_lock_151.wav`](lock/meme/v7_lock_151.wav) |
| 219 | 英雄联盟提莫-整装待发 | 0:03 | 2461 | [`v7_lock_154.wav`](lock/meme/v7_lock_154.wav) |
| 220 | 往事只能哈基米（锁车音） | 0:06 | 2458 | [`v7_lock_155.wav`](lock/meme/v7_lock_155.wav) |
| 226 | 阿斗 | 0:01 | 2366 | [`v7_lock_159.wav`](lock/meme/v7_lock_159.wav) |
| 228 | 哈夫克之声 | 0:04 | 2360 | [`v7_lock_160.wav`](lock/meme/v7_lock_160.wav) |
| 230 | 哥哥姐姐让一下，我要倒车啦 | 0:04 | 2357 | [`v7_lock_161.wav`](lock/meme/v7_lock_161.wav) |
| 232 | 板面 | 0:02 | 2336 | [`v7_lock_162.wav`](lock/meme/v7_lock_162.wav) |
| 233 | 锁车-来财 | 0:01 | 2320 | [`v7_lock_163.wav`](lock/meme/v7_lock_163.wav) |
| 237 | 四川芬达没坐_QQ浏览器格式转换_QQ浏览器转格式 | 0:01 | 2268 | [`v7_lock_166.wav`](lock/meme/v7_lock_166.wav) |
| 238 | 金将军阅兵1(11) | 0:03 | 2253 | [`v7_lock_167.wav`](lock/meme/v7_lock_167.wav) |
| 239 | 个性音效 | 0:03 | 2249 | [`v7_lock_168.wav`](lock/meme/v7_lock_168.wav) |
| 243 | 狼叫声 | 0:06 | 2206 | [`v7_lock_171.wav`](lock/meme/v7_lock_171.wav) |
| 246 | 牢大 | 0:03 | 2166 | [`v7_lock_172.wav`](lock/meme/v7_lock_172.wav) |
| 247 | 吉利汽车 | 0:10 | 2155 | [`v7_lock_173.wav`](lock/meme/v7_lock_173.wav) |
| 255 | 音效-坎话 | 0:02 | 2093 | [`v7_lock_175.wav`](lock/meme/v7_lock_175.wav) |
| 257 | V8 | 0:03 | 2064 | [`v7_lock_176.wav`](lock/meme/v7_lock_176.wav) |
| 259 | 泰罗哈基米 | 0:09 | 2039 | [`v7_lock_177.wav`](lock/meme/v7_lock_177.wav) |
| 260 | 小马云 | 0:02 | 2037 | [`v7_lock_178.wav`](lock/meme/v7_lock_178.wav) |
| 264 | 锁车 | 0:08 | 2018 | [`v7_lock_181.wav`](lock/meme/v7_lock_181.wav) |
| 266 | 监狱兔 | 0:04 | 2005 | [`v7_lock_182.wav`](lock/meme/v7_lock_182.wav) |
| 268 | 蓝莲哈吉米 | 0:05 | 1978 | [`v7_lock_183.wav`](lock/meme/v7_lock_183.wav) |
| 271 | 防盗启用-科幻 | 0:03 | 1963 | [`v7_lock_185.wav`](lock/meme/v7_lock_185.wav) |
| 274 | 反转进行曲-_是关中王来了_-Kam-Ridr 4 | 0:05 | 1944 | [`v7_lock_186.wav`](lock/meme/v7_lock_186.wav) |
| 275 | 爆笑 | 0:03 | 1935 | [`v7_lock_187.wav`](lock/meme/v7_lock_187.wav) |
| 277 | 哎呀，快走 | 0:02 | 1907 | [`v7_lock_188.wav`](lock/meme/v7_lock_188.wav) |
| 279 | 半岛铁盒 无对话 | 0:09 | 1869 | [`v7_lock_189.wav`](lock/meme/v7_lock_189.wav) |
| 281 | 凡人修仙传 | 0:04 | 1863 | [`v7_lock_191.wav`](lock/meme/v7_lock_191.wav) |
| 282 | 马保国-偷袭 | 0:01 | 1852 | [`v7_lock_192.wav`](lock/meme/v7_lock_192.wav) |
| 287 | 晚安锁车 | 0:04 | 1836 | [`v7_lock_196.wav`](lock/meme/v7_lock_196.wav) |
| 288 | 检测到核弹发射 | 0:02 | 1832 | [`v7_lock_197.wav`](lock/meme/v7_lock_197.wav) |
| 292 | BT-所有舱门已关闭​ | 0:04 | 1806 | [`v7_lock_200.wav`](lock/meme/v7_lock_200.wav) |
| - | 你干嘛哎哟 | 0:03 | - | [`v6_lock_075.wav`](lock/meme/v6_lock_075.wav) |

### 动漫影视（25）

| # | 音效 | 时长 | 下载量 | 文件 |
|---:|---|---:|---:|---|
| 1 | 蜡笔小新 呱呱呱 | 0:05 | 51448 | [`v7_lock_001.wav`](lock/anime/v7_lock_001.wav) |
| 7 | 蜡笔小新拜拜 | 0:05 | 21253 | [`v7_lock_007.wav`](lock/anime/v7_lock_007.wav) |
| 8 | 蜡笔小新-车子的门被锁上了 | 0:05 | 20863 | [`v7_lock_008.wav`](lock/anime/v7_lock_008.wav) |
| 17 | 小黄人-拜拜 | 0:03 | 14263 | [`v7_lock_016.wav`](lock/anime/v7_lock_016.wav) |
| 18 | 蜡笔小新+呱呱+啾啾 | 0:07 | 13740 | [`v7_lock_017.wav`](lock/anime/v7_lock_017.wav) |
| 22 | 海绵宝宝- 治愈 | 0:04 | 11797 | [`v7_lock_021.wav`](lock/anime/v7_lock_021.wav) |
| 28 | 公主请上车（海绵宝宝） | 0:02 | 10266 | [`v7_lock_026.wav`](lock/anime/v7_lock_026.wav) |
| 38 | 乌萨奇锁车音效 | 0:04 | 9366 | [`v7_lock_035.wav`](lock/anime/v7_lock_035.wav) |
| 40 | 皮卡丘1 | 0:02 | 8944 | [`v7_lock_037.wav`](lock/anime/v7_lock_037.wav) |
| 52 | 小黄人-降噪清晰版-拜拜-小黄人清晰版 | 0:01 | 8009 | [`v7_lock_048.wav`](lock/anime/v7_lock_048.wav) |
| 54 | 老大加油 蜡笔小新 | 0:03 | 7900 | [`v7_lock_050.wav`](lock/anime/v7_lock_050.wav) |
| 66 | 蜡笔小新 | 0:03 | 6290 | [`v7_lock_061.wav`](lock/anime/v7_lock_061.wav) |
| 76 | 蜡笔小新青蛙叫16bitmono | 0:05 | 5488 | [`v7_lock_069.wav`](lock/anime/v7_lock_069.wav) |
| 122 | 公主请上车（派大星） | 0:02 | 4070 | [`v7_lock_100.wav`](lock/anime/v7_lock_100.wav) |
| 143 | 蜡笔小新呱呱高音 | 0:05 | 3644 | [`v7_lock_114.wav`](lock/anime/v7_lock_114.wav) |
| 162 | 小黄人 | 0:03 | 3227 | [`v7_lock_124.wav`](lock/anime/v7_lock_124.wav) |
| 170 | 乌萨奇叫声 | 0:01 | 3106 | [`v7_lock_129.wav`](lock/anime/v7_lock_129.wav) |
| 217 | 小黄人-呜拜拜可用 | 0:06 | 2475 | [`v7_lock_153.wav`](lock/anime/v7_lock_153.wav) |
| - | 小新锁门 | 0:05 | - | [`v6_lock_013.wav`](lock/anime/v6_lock_013.wav) |
| - | 蜡笔小新锁车 低音量(2) 5 | 0:04 | - | [`v6_lock_031.wav`](lock/anime/v6_lock_031.wav) |
| - | 蜡笔小新结尾 | 0:05 | - | [`v6_lock_063.wav`](lock/anime/v6_lock_063.wav) |
| - | 小猪佩奇 | 0:03 | - | [`v6_lock_090.wav`](lock/anime/v6_lock_090.wav) |
| - | 蜡笔小新锁车(11) | 0:04 | - | [`v6_lock_091.wav`](lock/anime/v6_lock_091.wav) |
| - | 皮卡丘2 | 0:02 | - | [`v6_lock_097.wav`](lock/anime/v6_lock_097.wav) |
| - | 海绵宝宝_宝贝_中 | 0:02 | - | [`v6_lock_099.wav`](lock/anime/v6_lock_099.wav) |

### AI语音（22）

| # | 音效 | 时长 | 下载量 | 文件 |
|---:|---|---:|---:|---|
| 27 | seeyousir-贾维斯 | 0:03 | 10371 | [`v7_lock_025.wav`](lock/ai/v7_lock_025.wav) |
| 29 | （D档）我们出发吧-AI | 0:02 | 10073 | [`v7_lock_027.wav`](lock/ai/v7_lock_027.wav) |
| 45 | 主人请慢走 | 0:01 | 8603 | [`v7_lock_042.wav`](lock/ai/v7_lock_042.wav) |
| 56 | （副驾开门）欢迎来到动物成-AI | 0:02 | 7101 | [`v7_lock_052.wav`](lock/ai/v7_lock_052.wav) |
| 58 | 锁车完成，哨兵模式已激活 | 0:03 | 7032 | [`v7_lock_054.wav`](lock/ai/v7_lock_054.wav) |
| 62 | 爱车锁定成功，守护模式开启 | 0:03 | 6445 | [`v7_lock_058.wav`](lock/ai/v7_lock_058.wav) |
| 67 | （主驾安全带）我们要去巡逻了-AI | 0:03 | 6270 | [`v7_lock_062.wav`](lock/ai/v7_lock_062.wav) |
| 71 | 欢迎回家-贾维斯 | 0:04 | 5950 | [`v7_lock_065.wav`](lock/ai/v7_lock_065.wav) |
| 75 | （R档）倒车请注意-AI | 0:02 | 5489 | [`v7_lock_068.wav`](lock/ai/v7_lock_068.wav) |
| 78 | 主人，爱车已锁好 | 0:02 | 5346 | [`v7_lock_071.wav`](lock/ai/v7_lock_071.wav) |
| 83 | （左后关门）欢迎你我亲爱的-AI | 0:04 | 5261 | [`v7_lock_075.wav`](lock/ai/v7_lock_075.wav) |
| 89 | （P档）把车停好 嘟嘟交通警-AI | 0:03 | 5056 | [`v7_lock_079.wav`](lock/ai/v7_lock_079.wav) |
| 107 | 智能电动车哨兵模式 | 0:09 | 4491 | [`v7_lock_090.wav`](lock/ai/v7_lock_090.wav) |
| 112 | （主驾开门）我是尼克狐尼克-AI | 0:02 | 4318 | [`v7_lock_094.wav`](lock/ai/v7_lock_094.wav) |
| 127 | （P档）你把我的婴儿车锁上了-AI | 0:04 | 3961 | [`v7_lock_103.wav`](lock/ai/v7_lock_103.wav) |
| 141 | （D档）狡猾的兔子-AI | 0:03 | 3677 | [`v7_lock_112.wav`](lock/ai/v7_lock_112.wav) |
| 164 | （N档）现在是空挡-AI | 0:03 | 3205 | [`v7_lock_125.wav`](lock/ai/v7_lock_125.wav) |
| 200 | （右后门）奇妙之旅-AI | 0:04 | 2642 | [`v7_lock_142.wav`](lock/ai/v7_lock_142.wav) |
| 242 | 主人您好 | 0:01 | 2215 | [`v7_lock_170.wav`](lock/ai/v7_lock_170.wav) |
| 283 | see you Sir② | 0:02 | 1845 | [`v7_lock_193.wav`](lock/ai/v7_lock_193.wav) |
| - | see you Sir① | 0:03 | - | [`v6_lock_042.wav`](lock/ai/v6_lock_042.wav) |
| - | 倒车请注意 | 0:03 | - | [`v6_lock_093.wav`](lock/ai/v6_lock_093.wav) |

### 游戏音效（18）

| # | 音效 | 时长 | 下载量 | 文件 |
|---:|---|---:|---:|---|
| 3 | 超级玛丽 | 0:04 | 31779 | [`v7_lock_003.wav`](lock/game/v7_lock_003.wav) |
| 10 | 孙尚香 - 大小姐驾到统统闪开 | 0:03 | 19431 | [`v7_lock_010.wav`](lock/game/v7_lock_010.wav) |
| 19 | 马里奥 | 0:03 | 13264 | [`v7_lock_018.wav`](lock/game/v7_lock_018.wav) |
| 53 | 红警没电 | 0:02 | 7947 | [`v7_lock_049.wav`](lock/game/v7_lock_049.wav) |
| 57 | 红警任务完成 | 0:01 | 7043 | [`v7_lock_053.wav`](lock/game/v7_lock_053.wav) |
| 68 | 日本ACG-Super Mario Bros | 0:01 | 6124 | [`v7_lock_063.wav`](lock/game/v7_lock_063.wav) |
| 77 | 超级玛丽gameover | 0:02 | 5473 | [`v7_lock_070.wav`](lock/game/v7_lock_070.wav) |
| 81 | cs 1.4 ok lets go | 0:01 | 5280 | [`v7_lock_074.wav`](lock/game/v7_lock_074.wav) |
| 95 | 魂斗罗 | 0:05 | 4917 | [`v7_lock_085.wav`](lock/game/v7_lock_085.wav) |
| 98 | 马里奥-开始 | 0:03 | 4873 | [`v7_lock_087.wav`](lock/game/v7_lock_087.wav) |
| 117 | 高达启动 | 0:02 | 4184 | [`v7_lock_097.wav`](lock/game/v7_lock_097.wav) |
| 119 | 武器大师-哼 一个能打的都没有 | 0:04 | 4171 | [`v7_lock_098.wav`](lock/game/v7_lock_098.wav) |
| 201 | 红警-脖子右拧 | 0:01 | 2636 | [`v7_lock_143.wav`](lock/game/v7_lock_143.wav) |
| 253 | 马里奥-金币 | 0:05 | 2118 | [`v7_lock_174.wav`](lock/game/v7_lock_174.wav) |
| 261 | 红警(9) | 0:02 | 2033 | [`v7_lock_179.wav`](lock/game/v7_lock_179.wav) |
| 280 | 马里奥-吃蘑菇 | 0:02 | 1866 | [`v7_lock_190.wav`](lock/game/v7_lock_190.wav) |
| 290 | 击杀-王者荣耀 | 0:02 | 1818 | [`v7_lock_199.wav`](lock/game/v7_lock_199.wav) |
| - | 斗地主 赢了 | 0:04 | - | [`v6_lock_056.wav`](lock/game/v6_lock_056.wav) |

### 动物自然（15）

| # | 音效 | 时长 | 下载量 | 文件 |
|---:|---|---:|---:|---|
| 2 | 青蛙叫-呱 | 0:01 | 43346 | [`v7_lock_002.wav`](lock/animal/v7_lock_002.wav) |
| 4 | 青蛙2声 | 0:01 | 27731 | [`v7_lock_004.wav`](lock/animal/v7_lock_004.wav) |
| 14 | 呱 | 0:00 | 14903 | [`v7_lock_014.wav`](lock/animal/v7_lock_014.wav) |
| 24 | 呱1+2 | 0:01 | 10750 | [`v7_lock_023.wav`](lock/animal/v7_lock_023.wav) |
| 32 | 鸡你太美 | 0:02 | 9727 | [`v7_lock_030.wav`](lock/animal/v7_lock_030.wav) |
| 39 | 青蛙叫 呱 呱 呱 | 0:02 | 9026 | [`v7_lock_036.wav`](lock/animal/v7_lock_036.wav) |
| 96 | 蛙叫2 | 0:02 | 4904 | [`v7_lock_086.wav`](lock/animal/v7_lock_086.wav) |
| 216 | 羊叫-请回答1988 | 0:03 | 2478 | [`v7_lock_152.wav`](lock/animal/v7_lock_152.wav) |
| 221 | 鸡蛋鸭蛋荷包蛋 | 0:01 | 2433 | [`v7_lock_156.wav`](lock/animal/v7_lock_156.wav) |
| 224 | 雷军08锁车 | 0:03 | 2401 | [`v7_lock_157.wav`](lock/animal/v7_lock_157.wav) |
| 236 | 张嘟嘟钵钵鸡 | 0:04 | 2303 | [`v7_lock_165.wav`](lock/animal/v7_lock_165.wav) |
| 262 | 雷军星舰7 | 0:03 | 2026 | [`v7_lock_180.wav`](lock/animal/v7_lock_180.wav) |
| 284 | 呱 麦当劳 | 0:03 | 1845 | [`v7_lock_194.wav`](lock/animal/v7_lock_194.wav) |
| - | 呱-11-呱 | 0:01 | - | [`v6_lock_061.wav`](lock/animal/v6_lock_061.wav) |
| - | 呱2 1 | 0:01 | - | [`v6_lock_071.wav`](lock/animal/v6_lock_071.wav) |

### 影视梗（11）

| # | 音效 | 时长 | 下载量 | 文件 |
|---:|---|---:|---:|---|
| 12 | 我要验牌（纯人声版） | 0:01 | 16652 | [`v7_lock_012.wav`](lock/tv/v7_lock_012.wav) |
| 23 | 岳云鹏 - 真走啊 | 0:01 | 11192 | [`v7_lock_022.wav`](lock/tv/v7_lock_022.wav) |
| 41 | 皇上驾到 | 0:04 | 8907 | [`v7_lock_038.wav`](lock/tv/v7_lock_038.wav) |
| 60 | 还吃？收你们来了-哪吒2(3)(3) | 0:03 | 6702 | [`v7_lock_056.wav`](lock/tv/v7_lock_056.wav) |
| 64 | 牌没有问题（除杂音版） | 0:01 | 6396 | [`v7_lock_059.wav`](lock/tv/v7_lock_059.wav) |
| 65 | 变形金刚关机ing | 0:03 | 6354 | [`v7_lock_060.wav`](lock/tv/v7_lock_060.wav) |
| 87 | 你打我撒纯享版-太乙真人-哪吒2(8)(8) | 0:02 | 5176 | [`v7_lock_078.wav`](lock/tv/v7_lock_078.wav) |
| 90 | 哪吒-滴答滴答滴滴答 | 0:03 | 5029 | [`v7_lock_080.wav`](lock/tv/v7_lock_080.wav) |
| 184 | 你打我撒DJ版-太乙真人-哪吒2(7)(7) | 0:02 | 2833 | [`v7_lock_136.wav`](lock/tv/v7_lock_136.wav) |
| - | 恐怖音效 | 0:07 | - | [`v6_lock_079.wav`](lock/tv/v6_lock_079.wav) |
| - | 皇上驾到高音 | 0:04 | - | [`v6_lock_096.wav`](lock/tv/v6_lock_096.wav) |

### 机械车辆（11）

| # | 音效 | 时长 | 下载量 | 文件 |
|---:|---|---:|---:|---|
| 5 | 智能电动车锁车声 | 0:06 | 27728 | [`v7_lock_005.wav`](lock/machine/v7_lock_005.wav) |
| 36 | 3D锁车音效 | 0:04 | 9458 | [`v7_lock_034.wav`](lock/machine/v7_lock_034.wav) |
| 43 | 欢迎使用本公司只能电动车 | 0:03 | 8767 | [`v7_lock_040.wav`](lock/machine/v7_lock_040.wav) |
| 49 | 大气的锁车音效 | 0:03 | 8245 | [`v7_lock_045.wav`](lock/machine/v7_lock_045.wav) |
| 59 | 拖拉机启动 | 0:04 | 6914 | [`v7_lock_055.wav`](lock/machine/v7_lock_055.wav) |
| 72 | 解锁音效 | 0:03 | 5912 | [`v7_lock_066.wav`](lock/machine/v7_lock_066.wav) |
| 74 | 跑车音频 | 0:09 | 5653 | [`v7_lock_067.wav`](lock/machine/v7_lock_067.wav) |
| 110 | 飞机提示音 | 0:02 | 4350 | [`v7_lock_093.wav`](lock/machine/v7_lock_093.wav) |
| 241 | 00001绫波丽启动音 | 0:06 | 2218 | [`v7_lock_169.wav`](lock/machine/v7_lock_169.wav) |
| 269 | 锁车音效1 | 0:03 | 1965 | [`v7_lock_184.wav`](lock/machine/v7_lock_184.wav) |
| 289 | 啾啾-防盗启动 | 0:00 | 1821 | [`v7_lock_198.wav`](lock/machine/v7_lock_198.wav) |

### 系统数码（10）

| # | 音效 | 时长 | 下载量 | 文件 |
|---:|---|---:|---:|---|
| 6 | windows关机 | 0:02 | 24877 | [`v7_lock_006.wav`](lock/system/v7_lock_006.wav) |
| 34 | 友商是xx（含提示音） | 0:02 | 9558 | [`v7_lock_032.wav`](lock/system/v7_lock_032.wav) |
| 42 | 1996 因特尔 | 0:03 | 8783 | [`v7_lock_039.wav`](lock/system/v7_lock_039.wav) |
| 44 | 支付宝到账 10 万元 | 0:04 | 8743 | [`v7_lock_041.wav`](lock/system/v7_lock_041.wav) |
| 46 | windows 开机 | 0:04 | 8497 | [`v7_lock_043.wav`](lock/system/v7_lock_043.wav) |
| 171 | 支付宝到账100万 | 0:05 | 3101 | [`v7_lock_130.wav`](lock/system/v7_lock_130.wav) |
| 211 | 微信收款 1 万元 | 0:04 | 2499 | [`v7_lock_148.wav`](lock/system/v7_lock_148.wav) |
| 225 | 简洁超Q的提示音 | 0:02 | 2376 | [`v7_lock_158.wav`](lock/system/v7_lock_158.wav) |
| 234 | 番茄花园开机 | 0:08 | 2316 | [`v7_lock_164.wav`](lock/system/v7_lock_164.wav) |
| 285 | GBA 开机 | 0:04 | 1838 | [`v7_lock_195.wav`](lock/system/v7_lock_195.wav) |

</details>

## 清单字段

| 字段 | 含义 |
|---|---|
| `id` | 唯一 ID，也是 App 缓存文件名（`cacheDir/fx/<id>.wav`），**不要改** |
| `cat` | 大类：`lock` 锁车 / `talk` 喊话 |
| `category` | 中文子类别（按它筛选） |
| `label` | 显示名 |
| `file` | 仓库内相对路径 |
| `sha256` / `size` | 下载校验 |
| `ms` | 时长（毫秒） |
| `downloads` / `rank` / `tesla` | 站点热度、站内排名、是否可直接用于特斯拉 Boombox |

## 版本记录

- **v7**：锁车音效合并去重后 215 条（新增 200 条站点原文件 + 保留旧版独有的 15 条），按 8 个类别分目录；同名重复（85 条，同一音效的另一种编码）已剔除；新增 `index.html` 分类试听台。
- v6：锁车 100 + 喊话 88，条目已带 `category` 但未分目录。

## 关于素材

音效来自公开网络榜单，仅用于个人车机自定义锁车提示音的试听与自用，**请勿商用或二次分发**；涉及角色/影视/名人声音的条目，权利归原作者所有。如权利人要求，可提交 Issue 删除对应文件。

