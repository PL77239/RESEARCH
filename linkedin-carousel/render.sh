#!/usr/bin/env bash
# Renders slides.html to output/slide-XX.png (1080x1350) and output/poland-importers-carousel.pdf.
set -euo pipefail

cd "$(dirname "$0")"
CHROME="${CHROME:-$(command -v google-chrome || command -v chromium || command -v chromium-browser)}"
SRC="file://$PWD/slides.html"
COUNT=$(grep -c '<section class="slide' slides.html)
FLAGS=(--headless=new --disable-gpu --no-sandbox --hide-scrollbars --force-device-scale-factor=1
       --virtual-time-budget=5000 --no-first-run)

# Some headless Chrome builds keep running after writing the file, so wait for the output and stop it.
run_chrome() {
  local out=$1; shift
  local profile; profile=$(mktemp -d)
  setsid "$CHROME" "${FLAGS[@]}" --user-data-dir="$profile" "$@" >/dev/null 2>&1 &
  local pid=$!
  for _ in $(seq 1 120); do
    if ! kill -0 "$pid" 2>/dev/null; then break; fi
    if [[ -s "$out" ]]; then sleep 1; break; fi
    sleep 0.5
  done
  kill -- "-$pid" 2>/dev/null || true
  wait "$pid" 2>/dev/null || true
  sleep 0.5
  rm -rf "$profile" 2>/dev/null || true
  [[ -s "$out" ]] || { echo "failed to render $out" >&2; exit 1; }
  echo "rendered $out"
}

mkdir -p output
rm -f output/*.png output/*.pdf

for i in $(seq 1 "$COUNT"); do
  out=$(printf "output/slide-%02d.png" "$i")
  run_chrome "$out" --window-size=1080,1350 --screenshot="$out" "$SRC#$i"
done

run_chrome output/poland-importers-carousel.pdf --no-pdf-header-footer \
  --print-to-pdf=output/poland-importers-carousel.pdf "$SRC"
