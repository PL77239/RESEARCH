#!/usr/bin/env bash
# Regenerates the diagrams, the .docx reports and their PDF previews.
# Requires: python3 with python-docx and matplotlib, LibreOffice (soffice) for PDF export.
set -euo pipefail
cd "$(dirname "$0")"
mkdir -p build output

for lang in en pl; do
  python3 src/diagram.py "$lang" "build/diagram_${lang}.png"
done

python3 src/build.py content_en en "output/Exercise3_Type1_vs_Type2_Hypervisors_EN.docx"
python3 src/build.py content_pl pl "output/Cwiczenie3_Wirtualizatory_typu_I_i_II_PL.docx"
python3 src/build.py content_en_short en "output/Exercise3_Short_Answer_EN.docx"
python3 src/build.py content_pl_short pl "output/Cwiczenie3_Krotka_odpowiedz_PL.docx"

soffice --headless --convert-to pdf --outdir output output/*.docx >/dev/null
