#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
生成在线音效仓库的 manifest.json。

用法：在仓库根目录执行  python tools/gen_manifest.py
它会扫描 talk/ 与 lock/ 下的 wav，计算 sha256 与字节数，
套用 tools/labels.json 里的中文文案，输出根目录 manifest.json。

新增/删除音频后重跑本脚本即可；version 字段每次发布手动 +1
（App 端靠 version 判断是否需要刷新清单），也可用 --bump 自动递增。
"""
import hashlib
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MANIFEST = os.path.join(ROOT, "manifest.json")
LABELS = os.path.join(ROOT, "tools", "labels.json")

# 文件名形如 tts_talk_01.wav / tts_lock_21.wav
NAME_RE = re.compile(r"^(tts_(talk|lock)_(\d+))\.wav$", re.I)


def sha256(path: str) -> str:
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


def load_labels() -> dict:
    with open(LABELS, "r", encoding="utf-8") as f:
        return json.load(f)


def scan(folder: str, cat: str, labels: dict):
    out = []
    d = os.path.join(ROOT, folder)
    if not os.path.isdir(d):
        return out
    for name in sorted(os.listdir(d)):
        m = NAME_RE.match(name)
        if not m:
            continue
        clip_id = m.group(1)
        out.append({
            "id": clip_id,
            "cat": cat,
            "label": labels.get(clip_id, clip_id),
            "file": f"{folder}/{name}",
            "sha256": sha256(os.path.join(d, name)),
            "size": os.path.getsize(os.path.join(d, name)),
            "free": True,
        })
    return out


def main():
    labels = load_labels()
    clips = scan("talk", "talk", labels) + scan("lock", "lock", labels)
    version = 1
    if os.path.isfile(MANIFEST):
        with open(MANIFEST, "r", encoding="utf-8") as f:
            version = int(json.load(f).get("version", 0)) + 1
    if "--bump" in sys.argv:
        version += 1
    data = {
        "version": version,
        "note": "MAXDATA 在线音效库；全部为原创文案 + 自有 TTS 合成，可免费使用",
        "format": "wav pcm_s16le 16000Hz mono",
        "clips": clips,
    }
    with open(MANIFEST, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
        f.write("\n")
    print(f"manifest.json 已生成：version={version}，共 {len(clips)} 条"
          f"（talk={sum(1 for c in clips if c['cat']=='talk')}, "
          f"lock={sum(1 for c in clips if c['cat']=='lock')})")


if __name__ == "__main__":
    main()
