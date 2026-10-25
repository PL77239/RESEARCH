"""Render the proposal Markdown to a second, corporate-style PDF ("bis").

Requires: pip install markdown; google-chrome on PATH.
Usage: python3 proposal/build_bis.py
"""
import pathlib
import re
import subprocess

import markdown

HERE = pathlib.Path(__file__).parent
SRC = HERE / "BFLEX_2027_Buyer_Mobilisation_Poland.md"
HTML = HERE / "BFLEX_2027_Buyer_Mobilisation_Poland_bis.html"
PDF = HERE / "BFLEX_2027_Buyer_Mobilisation_Poland_bis.pdf"

NAVY = "#1f3a5f"
ORANGE = "#e8832a"
GREY = "#5f6b7a"
LIGHT = "#f2f5f9"

CSS = f"""
@page {{ size: A4; margin: 14mm 18mm 20mm;
  @bottom-left {{ content: "Poland Importers – Trading and Market Research"; vertical-align: top;
      padding-top: 3mm; border-top: 0.6pt solid #c8d1dc; font-family: Calibri, Carlito, Arial, sans-serif;
      font-size: 8pt; color: {GREY}; }}
  @bottom-center {{ content: ""; border-top: 0.6pt solid #c8d1dc; }}
  @bottom-right {{ content: "www.poland-importers.com   |   " counter(page) " / " counter(pages);
      vertical-align: top; padding-top: 3mm; border-top: 0.6pt solid #c8d1dc;
      font-family: Calibri, Carlito, Arial, sans-serif; font-size: 8pt; color: {NAVY}; }} }}
body {{ font-family: Calibri, Carlito, Arial, sans-serif; font-size: 9.8pt; color: #222; line-height: 1.3; margin: 0; }}

.top {{ display: flex; justify-content: space-between; align-items: center;
        border-bottom: 3px solid {NAVY}; padding-bottom: 6px; }}
.top img {{ width: 20mm; display: block; }}
.top .tag {{ text-align: right; font-size: 8.5pt; letter-spacing: 2px; text-transform: uppercase; color: {GREY}; }}
.top .tag b {{ display: block; font-size: 11pt; letter-spacing: 3px; color: {ORANGE}; }}

.title {{ margin: 10px 0 8px; }}
.title h1 {{ font-size: 21pt; line-height: 1.15; color: {NAVY}; margin: 0 0 4px; letter-spacing: 0.3px; }}
.title .event {{ font-size: 11pt; color: {ORANGE}; font-weight: bold; }}

.meta {{ display: flex; background: {LIGHT}; border-left: 4px solid {ORANGE}; padding: 7px 12px; margin-bottom: 4px; }}
.meta div {{ flex: 1; }}
.meta span {{ display: block; font-size: 7.5pt; text-transform: uppercase; letter-spacing: 1px; color: {GREY}; }}
.meta b {{ font-size: 9.5pt; color: {NAVY}; }}

h2 {{ font-size: 12pt; color: {NAVY}; text-transform: uppercase; letter-spacing: 0.5px;
      margin: 12px 0 4px; padding-bottom: 2px; border-bottom: 1px solid #c8d1dc; page-break-after: avoid; }}
h2 .n {{ display: inline-block; background: {NAVY}; color: #fff; border-radius: 3px; min-width: 17px;
         text-align: center; padding: 0 4px; margin-right: 8px; font-size: 10.5pt; }}
p {{ margin: 4px 0; }}
p > strong:only-child {{ display: block; color: {NAVY}; margin-top: 8px; font-size: 10.2pt; }}
ul {{ list-style: none; padding-left: 14px; margin: 3px 0 7px; }}
li {{ position: relative; margin: 1.5px 0; }}
li::before {{ content: ""; position: absolute; left: -12px; top: 0.52em; width: 5px; height: 5px; background: {ORANGE}; }}
ul + p {{ margin-top: 7px; }}
p.note {{ background: {LIGHT}; border-left: 4px solid {NAVY}; padding: 5px 10px; margin: 8px 0 4px; }}
"""


def build_html() -> str:
    text = SRC.read_text(encoding="utf-8")
    head, rest = text.split("\n## ", 1)
    title = re.search(r"^# (.+)$", head, re.M).group(1)
    event = re.search(r"^\*\*(.+)\*\*$", head, re.M).group(1)
    prepared_for = re.search(r"Prepared for: (.+)", head).group(1)
    prepared_by = re.search(r"Prepared by: (.+)", head).group(1)
    date = re.search(r"Date: (.+)", head).group(1)

    body = markdown.markdown("## " + rest, extensions=["tables", "fenced_code"])
    body = re.sub(r"<h2>(\d+)\. (.*?)</h2>", r"<h2><span class='n'>\1</span>\2</h2>", body)
    body = body.replace("<p>Note:", "<p class='note'><b>Note:</b>")

    header = (
        "<div class='top'><img src='assets/logo.png' alt='Poland Importers'>"
        "<div class='tag'><b>Proposal</b>Trade mission &amp; buyer mobilisation</div></div>"
        f"<div class='title'><h1>{title.title().replace('Bflex', 'BFLEX')}</h1>"
        f"<div class='event'>{event}</div></div>"
        "<div class='meta'>"
        f"<div><span>Prepared for</span><b>{prepared_for}</b></div>"
        f"<div><span>Prepared by</span><b>{prepared_by}</b></div>"
        f"<div style='flex:0 0 28mm'><span>Date</span><b>{date}</b></div></div>"
    )
    return (
        "<!doctype html><html><head><meta charset='utf-8'>"
        "<title>BFLEX 2027 – Buyer Mobilisation Proposal – Poland</title>"
        f"<style>{CSS}</style></head><body>{header}{body}</body></html>"
    )


def main() -> None:
    HTML.write_text(build_html(), encoding="utf-8")
    PDF.unlink(missing_ok=True)
    cmd = [
        "google-chrome", "--headless", "--no-sandbox", "--disable-gpu",
        "--no-pdf-header-footer", f"--print-to-pdf={PDF}", HTML.resolve().as_uri(),
    ]
    try:
        subprocess.run(cmd, capture_output=True, timeout=45)
    except subprocess.TimeoutExpired:
        pass
    if not PDF.exists():
        raise SystemExit("PDF was not generated")
    print(f"Wrote {HTML.name} and {PDF.name}")


if __name__ == "__main__":
    main()
