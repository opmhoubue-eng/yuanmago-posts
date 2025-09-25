#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os, datetime, xml.sax.saxutils as sax

BASE_URL = "https://opmhoubue-eng.github.io/yuanmago-posts"  # 你的 Pages 根（无尾斜杠）
ROOT     = "docs"                                            # 扫描 docs/ 目录
OUT      = "docs/sitemap.xml"                                # 输出到 docs/ 下

def file_mtime_iso(p):
    ts = datetime.datetime.utcfromtimestamp(os.path.getmtime(p))
    return ts.replace(microsecond=0).isoformat() + "Z"

urls = []
for r, _, files in os.walk(ROOT):
    for n in files:
        if not n.lower().endswith(".html"):
            continue
        full = os.path.join(r, n)
        rel  = os.path.relpath(full, ROOT).replace(os.sep, "/")
        loc  = f"{BASE_URL}/{rel}"
        last = file_mtime_iso(full)
        urls.append((loc, last))

urls.sort(key=lambda x: x[0])

os.makedirs(os.path.dirname(OUT), exist_ok=True)
with open(OUT, "w", encoding="utf-8") as f:
    f.write('<?xml version="1.0" encoding="UTF-8"?>\n')
    f.write('<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n')
    for loc, last in urls:
        f.write("  <url>\n")
        f.write(f"    <loc>{sax.escape(loc)}</loc>\n")
        f.write(f"    <lastmod>{last}</lastmod>\n")
        f.write("  </url>\n")
    f.write("</urlset>\n")

print(f"✅ wrote {OUT} with {len(urls)} urls")
