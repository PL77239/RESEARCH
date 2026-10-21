#!/usr/bin/env bash
# Builds output/poland-importers-carousel.mp4 (1080x1350, ~30 s) from output/slide-XX.png.
# Each slide is held still, like a PDF page, while a thin orange line fills along the bottom edge;
# slides change with a short dip to dark.
set -euo pipefail

cd "$(dirname "$0")"
FPS=30
HOLD=4.98     # seconds each slide is on screen, including its transitions
FADE=0.8      # dip-to-dark transition length

slides=(output/slide-*.png)
n=${#slides[@]}

BAR_H=8      # progress line along the bottom edge, filling while the slide is on screen
fill=$(awk "BEGIN{print $HOLD-$FADE}")

inputs=() filters="gradients=s=1080x$BAR_H:c0=0xf39200:c1=0xe53517:x0=0:y0=0:x1=1079:y1=0:speed=0.00001:r=$FPS,split=$n"
for i in "${!slides[@]}"; do filters+="[bar$i]"; done
filters+=";"
for i in "${!slides[@]}"; do
  inputs+=(-loop 1 -framerate "$FPS" -t "$HOLD" -i "${slides[$i]}")
  # The full gradient bar is drawn once; the slide's own bottom strip slides off it to reveal it.
  filters+="[$i:v]scale=1080:1350,fps=$FPS,setsar=1,split[s$i][c$i];"
  filters+="[c$i]crop=1080:$BAR_H:0:1350-$BAR_H[strip$i];"
  filters+="[s$i][bar$i]overlay=y=H-h:shortest=1[b$i];"
  filters+="[b$i][strip$i]overlay=x='W*min(t/$fill\,1)':y=H-h:eval=frame,format=yuv420p[v$i];"
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
