"""Build docs/solution_doc.pdf from docs/solution_doc.md (needs Edge or Chrome; no paid tools).

    python docs/build_pdf.py
"""
from __future__ import annotations

import shutil
import subprocess
import sys
from pathlib import Path

import markdown

HERE = Path(__file__).resolve().parent
CSS = """
@page { size: A4; margin: 13mm 14mm 12mm 14mm; }
body { font-family: 'Segoe UI', Calibri, Arial, sans-serif; font-size: 9.3pt; line-height: 1.36; color: #1d1d1b; }
h1 { font-size: 15pt; margin: 0 0 2px; color: #1f6f5c; }
h2 { font-size: 10.6pt; margin: 9px 0 3px; color: #1f6f5c; border-bottom: 1px solid #d9d5cc; padding-bottom: 1px; }
p { margin: 3px 0; }
ul, ol { margin: 2px 0 3px 0; padding-left: 17px; }
li { margin: 1px 0; }
table { border-collapse: collapse; width: 100%; margin: 4px 0; font-size: 8.6pt; }
th, td { border: 1px solid #d9d5cc; padding: 2px 5px; text-align: left; vertical-align: top; }
th { background: #f0eee8; }
code { font-family: Consolas, monospace; font-size: 8.4pt; background: #f0eee8; padding: 0 2px; }
.sub { color: #555; font-size: 8.8pt; margin-bottom: 4px; }
a { color: #1f6f5c; }
"""


def browser() -> str:
    for c in (r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
              r"C:\Program Files\Microsoft\Edge\Application\msedge.exe",
              r"C:\Program Files\Google\Chrome\Application\chrome.exe",
              shutil.which("chromium") or "", shutil.which("google-chrome") or ""):
        if c and Path(c).exists():
            return c
    sys.exit("Edge/Chrome not found")


def main():
    md = (HERE / "solution_doc.md").read_text(encoding="utf-8")
    body = markdown.markdown(md, extensions=["tables", "md_in_html"])
    html = f"<!doctype html><html><head><meta charset='utf-8'><title>Nyaya Saathi - solution doc</title>" \
           f"<style>{CSS}</style></head><body>{body}</body></html>"
    out_html = HERE / "solution_doc.html"
    out_html.write_text(html, encoding="utf-8")
    pdf = HERE / "solution_doc.pdf"
    subprocess.run([browser(), "--headless=new", "--disable-gpu", "--no-pdf-header-footer",
                    f"--print-to-pdf={pdf}", out_html.as_uri()], check=True, capture_output=True, timeout=120)
    try:
        from pypdf import PdfReader
        print(f"{pdf} - {len(PdfReader(str(pdf)).pages)} page(s)")
    except Exception:  # noqa: BLE001
        print(pdf)


if __name__ == "__main__":
    main()
