# Poland-Importers.com – LinkedIn carousel (draft v1)

B2B carousel presenting the company's core services. Format: 7 slides, 1080×1350 px (4:5, LinkedIn's recommended portrait size).

**Upload to LinkedIn:** create a post → *Add a document* → `output/poland-importers-carousel.pdf`.
The individual `output/slide-XX.png` files can be used as an image post or for review.

## Slides

| # | Content | Photo |
|---|---------|-------|
| 1 | Cover – "Your gateway to Polish buyers", map of Poland in national colours on the CEE map | – |
| 2 | About – 25+ years, 40+ countries, 500+ clients, industries, partner countries | – |
| 3 | 01 · We organize trade missions | Egyptian apparel trade mission (AECE), Warsaw 2025 |
| 4 | 02 · We find buyers for you | India Footwear & Leather Products Show, Warsaw 2025 |
| 5 | 03 · We arrange B2B meetings | Business talks during the Egyptian trade mission |
| 6 | Recent projects – India show, Egyptian mission, Destination Africa (Cairo) | 3 photos |
| 7 | CTA – website, e-mail, phone | – |

All facts and photos come from poland-importers.com (service pages, *About*, *News*, media library).
Spare photos for later iterations are in `assets/photos/` (show hall, Indian Embassy seminar).

## Editing

- Text and layout live in `slides.html` (open it in a browser to preview all slides).
- Colours come from the logo: navy `#0d4c9a` / `#081f45` plus the orange-red swoosh `#f39200 → #e53517`.
- Fonts: Montserrat (headings) and Inter (body), bundled in `assets/fonts/` (OFL licence).
- Re-render PNGs and the PDF (requires Google Chrome / Chromium):

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
> Swipe through to see what we do, then send us your product details.
> 🌐 poland-importers.com
>
> #Poland #CEE #Export #TradeMission #B2B #Sourcing #Import

## To confirm with the client

- Contact details on slide 7: `md@poland-importers.com` (from their Destination Africa flyer) and `+48 601 080 490` (site header).
- Whether the caption "Polish buyers at Destination Africa" is OK (based on the News entry "We brought buyers to Destination Africa").
- Whether a short animated version (MP4/GIF) is wanted in addition to the carousel.
