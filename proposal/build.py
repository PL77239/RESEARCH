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
@page { size: A4; margin: 16mm 20mm 18mm;
        @bottom-center { content: "www.poland-importers.com"; vertical-align: top; padding-top: 3mm;
                         border-top: 1px solid #c8d1dc; margin-top: 2mm;
                         font-family: Calibri, Carlito, Arial, sans-serif; font-size: 8.5pt;
                         letter-spacing: 0.4px; color: #1f3a5f; } }
body { font-family: Calibri, Carlito, Arial, sans-serif; font-size: 10pt; color: #222; line-height: 1.38; }
h1 { font-size: 16pt; letter-spacing: 0.5px; color: #1f3a5f; margin: 0 0 4px; }
h1 + p { font-size: 11pt; margin-bottom: 10px; }
h1 ~ p:nth-of-type(2), h1 ~ p:nth-of-type(3) { color: #555; margin: 1px 0; }
h2 { font-size: 11.5pt; color: #1f3a5f; text-transform: uppercase; letter-spacing: 0.4px;
     border-bottom: 1px solid #c8d1dc; padding-bottom: 2px; margin: 13px 0 5px; page-break-after: avoid; }
h2:first-of-type { margin-top: 22px; }
p { margin: 4px 0; }
p > strong:only-child { color: #1f3a5f; }
ul { padding-left: 18px; margin: 3px 0 8px; }
li { margin: 1px 0; }
.logo { display: block; width: 21mm; margin: -4mm auto 3mm; }
"""

LOGO = "<img class='logo' src='assets/logo.png' alt='Poland Importers'>"


def main() -> None:
    body = markdown.markdown(SRC.read_text(encoding="utf-8"), extensions=["tables", "fenced_code"])
    HTML.write_text(
        f"<!doctype html><html><head><meta charset='utf-8'>"
        f"<title>BFLEX 2027 – Buyer Mobilisation Proposal – Poland</title>"
        f"<style>{CSS}</style></head><body>{LOGO}{body}</body></html>",
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
