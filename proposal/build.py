"""Render the proposal Markdown to HTML and PDF.

Requires: pip install markdown; google-chrome on PATH.
Usage: python3 proposal/build.py
"""
import pathlib
import subprocess

import markdown

HERE = pathlib.Path(__file__).parent
SRC = HERE / "BFLEX_2027_Buyer_Mobilisation_Poland.md"
HTML = SRC.with_suffix(".html")
PDF = SRC.with_suffix(".pdf")

CSS = """
@page { size: A4; margin: 16mm 15mm; }
body { font-family: 'Helvetica Neue', Arial, sans-serif; font-size: 10pt; color: #1f2933; line-height: 1.45; }
h1 { font-size: 20pt; color: #7a1f1f; margin: 0 0 4px; }
h2 { font-size: 13.5pt; color: #7a1f1f; border-bottom: 2px solid #c9a227; padding-bottom: 3px; margin-top: 22px; page-break-after: avoid; }
h3 { font-size: 11pt; color: #3d2b1f; margin-top: 14px; page-break-after: avoid; }
table { border-collapse: collapse; width: 100%; margin: 8px 0 12px; font-size: 9pt; page-break-inside: avoid; }
th { background: #7a1f1f; color: #fff; text-align: left; padding: 5px 6px; }
td { border-bottom: 1px solid #e3d9cc; padding: 4px 6px; vertical-align: top; }
tr:nth-child(even) td { background: #faf6f0; }
pre { background: #faf6f0; border-left: 4px solid #c9a227; padding: 8px 10px; font-size: 9pt; page-break-inside: avoid; }
hr { border: none; border-top: 1px solid #e3d9cc; margin: 14px 0; }
ul, ol { padding-left: 20px; }
li { margin: 2px 0; }
"""


def main() -> None:
    body = markdown.markdown(SRC.read_text(encoding="utf-8"), extensions=["tables", "fenced_code"])
    HTML.write_text(
        f"<!doctype html><html><head><meta charset='utf-8'>"
        f"<title>BFLEX 2027 – Buyer Mobilisation Proposal – Poland</title>"
        f"<style>{CSS}</style></head><body>{body}</body></html>",
        encoding="utf-8",
    )
    PDF.unlink(missing_ok=True)
    cmd = [
        "google-chrome", "--headless", "--no-sandbox", "--disable-gpu",
        "--no-pdf-header-footer", f"--print-to-pdf={PDF}", HTML.resolve().as_uri(),
    ]
    try:
        subprocess.run(cmd, capture_output=True, timeout=45)
    except subprocess.TimeoutExpired:
        # Headless Chrome sometimes lingers after writing the PDF.
        pass
    if not PDF.exists():
        raise SystemExit("PDF was not generated")
    print(f"Wrote {HTML.name} and {PDF.name}")


if __name__ == "__main__":
    main()
