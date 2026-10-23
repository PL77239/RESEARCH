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
@page { size: A4; margin: 20mm 20mm; }
body { font-family: Arial, sans-serif; font-size: 10.5pt; color: #000; line-height: 1.4; }
h1 { font-size: 14pt; margin: 0 0 6px; }
h2 { font-size: 11.5pt; margin: 16px 0 6px; page-break-after: avoid; }
p { margin: 4px 0; }
ul { padding-left: 20px; margin: 4px 0 8px; }
li { margin: 1px 0; }
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
