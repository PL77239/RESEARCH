#!/usr/bin/env python3
"""Build a single .xlsx spreadsheet of leather-goods wholesalers/importers/distributors.

Columns: Country | Company Name | WWW | E-mail
Data mirrors the per-country Markdown files in this repo.
"""

from openpyxl import Workbook
from openpyxl.styles import Font, Alignment, PatternFill, Border, Side
from openpyxl.utils import get_column_letter

# (Country, Company Name, WWW, E-mail)
ROWS = [
    # --- Germany ---
    ("Germany", "iMPEX Lederwaren Import-Export GmbH", "https://www.impex-lederwaren.de", "info@impex-lederwaren.de"),
    ("Germany", "HMT Lederwaren Import GmbH", "https://hmtlederwaren.de", "hmtlederwaren@t-online.de"),
    ("Germany", "APC-NCC Lederwaren", "https://apc-ncc.de", "info@apc-ncc.de"),
    ("Germany", "Bertoni Großhandel", "https://bertoni-grosshandel.de", "bertoni-grosshandel@web.de"),
    ("Germany", "Branco Lederwaren (Sommer & Grubba GbR)", "https://www.branco-lederwaren.de", ""),
    ("Germany", "DEIMOS Lederwaren GmbH", "https://deimosfashion.com", "info@deimosfashion.com"),
    ("Germany", "CLM Lederwaren GmbH & Co. KG", "https://clm-shop.de", "info@clm-shop.de"),
    ("Germany", "Venetto", "https://venetto.de", ""),
    ("Germany", "PICARD Lederwaren GmbH & Co. KG", "https://picard-fashion.com", "tf@picard-fashion.com"),
    ("Germany", "Braun Büffel (Braun GmbH & Co. KG)", "https://braun-bueffel.com", "info@braun-bueffel.com"),
    ("Germany", "Greenburry", "https://www.greenburry.de", ""),

    # --- Lithuania ---
    ("Lithuania", "UAB Sominta", "https://sominta.com", "info@sominta.lt"),
    ("Lithuania", "UAB Vilga", "http://www.vilga.lt", "info@vilga.lt"),
    ("Lithuania", "UAB Arenalis (leather materials)", "https://www.leather.lt", ""),
    ("Lithuania", "Baltijos odos, MB / Baltic Leather Supply (leather materials)", "", ""),
    ("Lithuania", "Revaris (leather materials)", "https://www.revaris.lt", ""),

    # --- Latvia ---
    ("Latvia", "SIA Mille", "https://www.mille.lv", "mille@mille.lv"),
    ("Latvia", "Modes Elementi", "", ""),
    ("Latvia", "SIA Velplev", "https://www.velplev.lv", "velplev@inbox.lv"),
    ("Latvia", "Tailor Riga (SIA ALIAS-Z)", "https://www.tailorriga.lv", ""),
    ("Latvia", "Eric Lasko Production", "https://ericlasko.com", ""),
    ("Latvia", "Lakolina (directory listing - verify)", "https://www.exporthub.com/lakolina/", ""),

    # --- Estonia ---
    ("Estonia", "Nabo Nahktooted OÜ (Nokian Nahkatuote group)", "https://nokiannahkatuote.fi", "nabo@nahkatuote.inet.fi"),
    ("Estonia", "Bagy OÜ", "", "bettigehrke@gmail.com"),
    ("Estonia", "Leather World OÜ (leather materials / footwear)", "https://leather-world.co", "sales@leather-world.co"),
    ("Estonia", "Nakro OÜ (leather materials)", "https://www.nakro.ee", ""),

    # --- Czech Republic ---
    ("Czech Republic", "JUNI EXPORT-IMPORT s.r.o.", "https://www.juni.cz", "info@juni.cz"),
    ("Czech Republic", "PAUL BORDAS FASHION, s.r.o.", "https://www.paulbordas.cz", "info@paulbordas.cz"),
    ("Czech Republic", "UNIVARO – leather s.r.o. (UNIVARO Bags)", "https://www.univaro.cz", "info@univaro.cz"),
    ("Czech Republic", "Gora (gora-velkoobchod)", "https://www.gora-velkoobchod.cz", ""),

    # --- Slovakia ---
    ("Slovakia", "VEGA-LM (VegaLM)", "https://www.vegalm.sk", ""),
    ("Slovakia", "Max s.r.o. (MAX Original Leather / MaxLeather)", "https://maxleather.sk", "max@maxleather.sk"),
    ("Slovakia", "NICOLAUS LEATHER, s.r.o. (leather materials)", "https://nicolausleather.sk", ""),

    # --- Hungary ---
    ("Hungary", "BI-KA Bőráru Kft.", "https://divatnagyker.hu/bi-ka-boraru-kft-bordiszmu-aru-importor-nagykereskedo/", ""),
    ("Hungary", "Skin Bőrdíszmű", "", ""),
    ("Hungary", "Synchrony LM (SLM Bőrdíszmű / Bőrdíszműnagyker)", "https://bordiszmunagyker.hu", ""),
    ("Hungary", "Kadro Bőrdíszmű Nagykereskedés", "https://kadro.hu", "info@kadro.hu"),
    ("Hungary", "Top Bag 2000 Kft. (Karen)", "https://karennagyker.hu", "info@karen.hu"),

    # --- Denmark ---
    ("Denmark", "Axelsen & Søn ApS (Montana / Treats)", "https://axelsenson.com", "info@axelsenson.com"),
    ("Denmark", "Uni-Leather ApS", "https://uni-leather.dk", ""),
    ("Denmark", "Adax A/S", "https://adax.dk", ""),
    ("Denmark", "Markberg", "https://markberg.dk", "salessupport@markberg.com"),
    ("Denmark", "Still Nordic", "https://stillnordic.dk", ""),
    ("Denmark", "SIPO Trading K/S (leather / skins)", "https://sipo.dk", ""),
    ("Denmark", "Sicadan (leather materials)", "https://www.sicadan.dk", "info@sicadan.dk"),
]

HEADERS = ["Country", "Company Name", "WWW", "E-mail"]


def main():
    wb = Workbook()
    ws = wb.active
    ws.title = "Leather Goods Wholesalers"

    header_fill = PatternFill("solid", fgColor="1F4E78")
    header_font = Font(bold=True, color="FFFFFF", size=11)
    thin = Side(style="thin", color="D9D9D9")
    border = Border(left=thin, right=thin, top=thin, bottom=thin)

    ws.append(HEADERS)
    for col in range(1, len(HEADERS) + 1):
        c = ws.cell(row=1, column=col)
        c.fill = header_fill
        c.font = header_font
        c.alignment = Alignment(horizontal="left", vertical="center")
        c.border = border

    for country, name, www, email in ROWS:
        ws.append([country, name, www, email])
        r = ws.max_row
        if www:
            cell = ws.cell(row=r, column=3)
            cell.hyperlink = www
            cell.font = Font(color="0563C1", underline="single")
        if email:
            cell = ws.cell(row=r, column=4)
            cell.hyperlink = f"mailto:{email}"
            cell.font = Font(color="0563C1", underline="single")
        for col in range(1, len(HEADERS) + 1):
            ws.cell(row=r, column=col).border = border
            ws.cell(row=r, column=col).alignment = Alignment(vertical="center")

    widths = [18, 48, 55, 34]
    for i, w in enumerate(widths, start=1):
        ws.column_dimensions[get_column_letter(i)].width = w

    ws.freeze_panes = "A2"
    ws.auto_filter.ref = f"A1:{get_column_letter(len(HEADERS))}{ws.max_row}"

    out = "Leather_Goods_Wholesalers.xlsx"
    wb.save(out)
    print(f"Wrote {out} with {len(ROWS)} companies.")


if __name__ == "__main__":
    main()
