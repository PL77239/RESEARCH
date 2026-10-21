#!/usr/bin/env bash
# Builds output/poland-importers-carousel.mp4 (1080x1350, ~30 s) from output/slide-XX.png.
# Each slide is held still, like a PDF page; slides change with a short dip to dark.
set -euo pipefail

cd "$(dirname "$0")"
FPS=30
HOLD=4.98     # seconds each slide is on screen, including its transitions
FADE=0.8      # dip-to-dark transition length

slides=(output/slide-*.png)
n=${#slides[@]}

inputs=() filters=""
for i in "${!slides[@]}"; do
  inputs+=(-loop 1 -framerate "$FPS" -t "$HOLD" -i "${slides[$i]}")
  filters+="[$i:v]scale=1080:1350,fps=$FPS,setsar=1,format=yuv420p[v$i];"
done

prev="v0"
for ((i = 1; i < n; i++)); do
  offset=$(awk "BEGIN{print $i*($HOLD-$FADE)}")
  filters+="[$prev][v$i]xfade=transition=fadeblack:duration=$FADE:offset=$offset[x$i];"
  prev="x$i"
done
total=$(awk "BEGIN{print $n*$HOLD-($n-1)*$FADE}")
filters+="[$prev]fade=t=in:d=0.4,fade=t=out:st=$(awk "BEGIN{print $total-0.6}"):d=0.6[out]"

ffmpeg -loglevel error -y "${inputs[@]}" -filter_complex "$filters" -map "[out]" \
  -c:v libx264 -preset slow -crf 18 -pix_fmt yuv420p -r "$FPS" -movflags +faststart \
  output/poland-importers-carousel.mp4
echo "rendered output/poland-importers-carousel.mp4 (${total}s)"
