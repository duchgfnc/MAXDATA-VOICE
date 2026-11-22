#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""把 gen_voice_batch2.py 里的 150 条新文案合并进 labels.json。

只在 voice-repo 根目录执行：python tools/merge_labels.py
从项目 tools/gen_voice_batch2.py 读取 TALK/LOCK 列表（用 AST 解析，不执行合成），
把 id->文案 写进 labels.json，保留已有条目（旧的 20+32 不动）。
"""
import ast
import json
import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROJ = os.path.dirname(os.path.dirname(ROOT))  # MaxData2
SRC = os.path.join(PROJ, "tools", "gen_voice_batch2.py")
LABELS = os.path.join(ROOT, "tools", "labels.json")


def read_lists():
    with open(SRC, "r", encoding="utf-8") as f:
        tree = ast.parse(f.read())
    out = {}
    for node in tree.body:
        if isinstance(node, ast.Assign) and len(node.targets) == 1:
            name = getattr(node.targets[0], "id", "")
            if name in ("TALK", "LOCK") and isinstance(node.value, ast.List):
                items = []
                for el in node.value.elts:
                    if isinstance(el, ast.Tuple) and len(el.elts) >= 2:
                        cid = ast.literal_eval(el.elts[0])
                        text = ast.literal_eval(el.elts[1])
                        items.append((cid, text))
                out[name] = items
    return out


def main():
    lists = read_lists()
    labels = {}
    if os.path.isfile(LABELS):
        with open(LABELS, "r", encoding="utf-8") as f:
            labels = json.load(f)
    added = 0
    for key in ("TALK", "LOCK"):
        for cid, text in lists.get(key, []):
            if cid not in labels:
                added += 1
            labels[cid] = text
    with open(LABELS, "w", encoding="utf-8") as f:
        json.dump(labels, f, ensure_ascii=False, indent=2)
        f.write("\n")
    print(f"labels.json 已更新：新增/覆盖 {added} 条，总计 {len(labels)} 条")


if __name__ == "__main__":
    main()
