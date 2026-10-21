# Poland-Importers.com – LinkedIn carousel (draft v3)

B2B carousel presenting the company's core services. Format: 7 slides, 1080×1350 px (4:5, LinkedIn's recommended portrait size).

**Upload to LinkedIn:** create a post → *Add a document* → `output/poland-importers-carousel.pdf`.
**Video version:** `output/poland-importers-carousel.mp4` – 30 s, 1080×1350, H.264. Each slide holds for about 4 s with a slow 2% push-in, and slides change with a short dip to dark.
The individual `output/slide-XX.png` files can be used for review or other channels.

## Slides

| # | Content | Photo |
|---|---------|-------|
| 1 | Cover – "Your gateway to Polish buyers", map of Poland in national colours on the CEE map | – |
| 2 | About – 25+ years, 40+ countries, 500+ clients, industries, partner countries | – |
| 3 | 01 · We organize trade missions | India Footwear & Leather Products Show hall, Warsaw 2025 (client photo) |
| 4 | 02 · We find buyers for you | AI-generated: team reviewing market-analysis charts (`buyer-research.jpg`) |
| 5 | 03 · We arrange B2B meetings | AI-generated: handshake at a B2B meeting (`b2b-handshake.jpg`) |
| 6 | Recent projects – logo wall of 8 trade fairs (see below) | – |
| 7 | CTA – website, e-mail, phone | – |

All facts and the real event photos come from poland-importers.com or the client. The slide 4 and 5 images are AI-generated, show no real people and have no event caption.
Spare photos for later iterations are in `assets/photos/` (Egyptian trade mission, buyers at the footwear show, ribbon cutting, Destination Africa, Indian Embassy seminar).

### Trade fair logos (slide 6)

All logos are in `assets/logos/` and were taken from the fairs' official websites. Colour logos keep their brand colours. Single-colour logos are recoloured to the carousel navy (`#081f45`) so the wall looks consistent.

| Logo | Fair | Source |
|------|------|--------|
| `ifco.svg` | IFCO – Istanbul Fashion Connection, Turkey | ifco.com.tr |
| `texhibition.svg` | Texhibition Istanbul, Turkey | texhibitionist.com |
| `bharat-tex.png` | Bharat Tex 2026, New Delhi, India | bharat-tex.com |
| `iigf.png` | India International Garment Fair (organised by IGFA), New Delhi | indiaapparelfair.com |
| `ailpa.png` | AILPA – All India Leather Products & Allied Sourcing Fair, Kolkata | cropped from the AILPA banner on ilpaindia.org |
| `ready-to-show.png` | Ready to Show, Milan, Italy | readytoshow.it (the "at mfj" edition suffix removed) |
| `apparel-sourcing-tashkent.png` | Apparel Sourcing Tashkent, Uzbekistan | apparel-sourcing.uz |
| `heimtextil-uzbekistan.png` | Heimtextil Uzbekistan, Tashkent | lettering captured from the heimtextil.uz homepage lockup (no standalone logo file is published) |

Both Messe Frankfurt logos are shown without the "licensed by Messe Frankfurt Exhibition GmbH" line, so they stay legible at this size.

## Editing

- Text and layout live in `slides.html` (open it in a browser to preview all slides).
- Colours come from the logo: navy `#0d4c9a` / `#081f45` plus the orange-red swoosh `#f39200 → #e53517`.
- Fonts: Montserrat (headings) and Inter (body), bundled in `assets/fonts/` (OFL licence).
- Re-render PNGs, the PDF and the MP4 (requires Google Chrome / Chromium and ffmpeg). `./make_video.sh` rebuilds only the video from existing PNGs:

```bash
./render.sh
```

- The map (`assets/poland-cee-map.svg`) is generated from Natural Earth data. See `tools/make_map.py` for instructions.

## Suggested post caption

> Looking to sell in Poland and Central & Eastern Europe? 🇵🇱
>
> For over 25 years we have been helping producers, chambers of commerce and exporters' associations meet the right buyers:
> ✅ Trade missions tailored to your industry
> ✅ Buyer sourcing and matching
> ✅ B2B meetings with pre-qualified companies
>
> See what we do, then send us your product details.
> 🌐 poland-importers.com
>
> #Poland #CEE #Export #TradeMission #B2B #Sourcing #Import

## To confirm with the client

- Contact details on slide 7: `md@poland-importers.com` (from their Destination Africa flyer) and `+48 601 080 490` (site header).
- Ideally, get official vector logos for AILPA and Heimtextil Uzbekistan from the organisers. The current files are cropped from their websites.
