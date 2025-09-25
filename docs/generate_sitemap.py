#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os, subprocess, datetime, xml.sax.saxutils

BASE_URL   = "https://opmhoubue-eng.github.io/yuanmago-posts"  # 你站点的前缀
POSTS_DIR  = "yuanmago-posts"                                   # 扫描目录
OUTPUT_XML = "sitemap.xml"                                      # 输出文件名

def git_last_commit_iso(path: str) -> str | None:
    """返回文件最后一次 git 提交时间（UTC，ISO8601），失败返回 None"""
    try:
        ts = subprocess.check_output(
            ["git", "log", "-1", '--pretty=format:%cI', "--", path],
            stderr=subprocess.DEVNULL,
            text=True
        ).strip()
        return ts or None
    except Exception:
        return None

def file_mtime_iso(path: str) -> str:
    """返回文件修改时间（UTC，ISO8601）"""
    ts = datetime.datetime.utcfromtimestamp(os.path.getmtime(path))
    return ts.replace(microsecond=0).isoformat() + "Z"

def collect_urls():
    urls = []
    for root, _, files in os.walk(POSTS_DIR):
        for name in files:
            if not name.lower().endswith(".html"):
                continue
            full = os.path.join(root, name)
            rel  = os.path.relpath(full, POSTS_DIR).replace(os.sep, "/")
            url  = f"{BASE_URL}/{rel}"
            last = git_last_commit_iso(full) or file_mtime_iso(full)
            urls.append((url, last))
    # 稳定排序，避免无谓 diff
    urls.sort(key=lambda x: x[0])
    return urls

def write_sitemap(urls):
    with open(OUTPUT_XML, "w", encoding="utf-8") as f:
        f.write('<?xml version="1.0" encoding="UTF-8"?>\n')
        f.write('<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n')
        for loc, lastmod in urls:
            f.write("  <url>\n")
            f.write(f"    <loc>{xml.sax.saxutils.escape(loc)}</loc>\n")
            f.write(f"    <lastmod>{lastmod}</lastmod>\n")
            f.write("  </url>\n")
        f.write("</urlset>\n")

def main():
    if not os.path.isdir(POSTS_DIR):
        raise SystemExit(f"❌ 未找到目录：{POSTS_DIR}")
    urls = collect_urls()
    write_sitemap(urls)
    print(f"✅ 生成 {OUTPUT_XML} 完成，共 {len(urls)} 个页面。")

if __name__ == "__main__":
    main()
