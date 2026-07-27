#!/usr/bin/env python3
"""Build a single .xlsx spreadsheet of leather-goods companies with a fit classification.

Goal context: we want to SELL finished leather goods (made in India) to these companies.
So the ideal targets are IMPORTERS / DISTRIBUTORS / STOCK-HOLDING WHOLESALERS that buy
finished leather goods for resale. Companies that only make their own products, artisan
makers, and hide/materials suppliers are not buyers of a finished catalogue.

Sheet 1 "All companies": Country | Company | WWW | E-mail | Business type | Fit
Sheet 2 "Priority targets": only the strong-fit importers/distributors/wholesalers.
"""

from openpyxl import Workbook
from openpyxl.styles import Font, Alignment, PatternFill, Border, Side
from openpyxl.utils import get_column_letter

# Fit codes
YES = "Yes - importer / distributor / stock wholesaler (buys finished goods to resell)"
MAYBE = "Maybe - own production or own-design brand (only if you offer OEM / private label)"
NO = "No - materials/hides/footwear supplier or artisan own-make / not a finished-goods buyer"

# (Country, Company, WWW, E-mail, Business type, Fit)
ROWS = [
    # --- Germany ---
    ("Germany", "iMPEX Lederwaren Import-Export GmbH", "https://www.impex-lederwaren.de", "info@impex-lederwaren.de", "Importer & wholesaler of small leather goods/bags", YES),
    ("Germany", "HMT Lederwaren Import GmbH", "https://hmtlederwaren.de", "hmtlederwaren@t-online.de", "Importer & wholesaler (imports from factories)", YES),
    ("Germany", "APC-NCC Lederwaren", "https://apc-ncc.de", "info@apc-ncc.de", "B2B wholesaler (own brands sourced abroad)", YES),
    ("Germany", "Bertoni Großhandel", "https://bertoni-grosshandel.de", "bertoni-grosshandel@web.de", "B2B wholesaler of bags/accessories", YES),
    ("Germany", "DEIMOS Lederwaren GmbH", "https://deimosfashion.com", "info@deimosfashion.com", "Wholesaler / cash & carry + private label", YES),
    ("Germany", "CLM Lederwaren GmbH & Co. KG", "https://clm-shop.de", "info@clm-shop.de", "Wholesaler (brand distribution)", YES),
    ("Germany", "Greenburry (bags for living GmbH)", "https://www.greenburry.de", "info@bagsforliving.de", "Brand/importer - already sources finished goods from India & Europe", YES),
    ("Germany", "MB Lederwaren-Importe GmbH", "https://www.mb-lederwaren.de", "info@mb-lederwaren.de", "Wholesale importer of leather goods/luggage", YES),
    ("Germany", "LM-International (Europa) GmbH", "https://lmi.de", "", "Importer & wholesaler (imports all articles itself)", YES),
    ("Germany", "Koffer-Zentrale.de", "https://koffer-zentrale.de", "", "Direct importer / B2B wholesaler (dealers only)", YES),
    ("Germany", "Branco Lederwaren (Sommer & Grubba GbR)", "https://www.branco-lederwaren.de", "", "Own production + private label (manufacturer)", MAYBE),
    ("Germany", "PICARD Lederwaren GmbH & Co. KG", "https://picard-fashion.com", "tf@picard-fashion.com", "Manufacturer/brand (own production EU) + private label", MAYBE),
    ("Germany", "Venetto", "https://venetto.de", "", "Own manufacturer 'Made in Germany'", NO),
    ("Germany", "Braun Büffel (Braun GmbH & Co. KG)", "https://braun-bueffel.com", "info@braun-bueffel.com", "Own manufacturer 'Made in Germany' (premium)", NO),
    ("Germany", "Esquire Lederwaren – Rupp & Ricker GmbH", "https://www.esquire-lederwaren.de", "info@esquire-lederwaren.de", "Own manufacturer/brand (own factory, own patents)", NO),

    # --- Lithuania ---
    ("Lithuania", "ANIS, UAB", "https://www.anis.lt", "info@anis.lt", "Distributor/importer of brands + retail (wholesale & retail)", YES),
    ("Lithuania", "UAB Sominta", "https://sominta.com", "info@sominta.lt", "Own manufacturer (handbags) + contract mfr", MAYBE),
    ("Lithuania", "UAB Vilga", "http://www.vilga.lt", "info@vilga.lt", "Own manufacturer (natural leather goods)", MAYBE),
    ("Lithuania", "VIKTODA, UAB", "http://www.viktoda.lt", "", "Own manufacturer + trade", MAYBE),
    ("Lithuania", "UAB Arenalis", "https://www.leather.lt", "", "Leather materials / hides & fittings", NO),
    ("Lithuania", "Baltijos odos, MB / Baltic Leather Supply", "", "", "Leather materials / hides & fittings", NO),
    ("Lithuania", "Revaris", "https://www.revaris.lt", "", "Leather materials (natural & artificial)", NO),

    # --- Latvia ---
    ("Latvia", "Modes Elementi", "", "", "Distributor/wholesaler of branded accessories (stock)", YES),
    ("Latvia", "SIA Mille", "https://www.mille.lv", "mille@mille.lv", "Own manufacturer (produces for brands) / OEM", MAYBE),
    ("Latvia", "SIA Velplev", "https://www.velplev.lv", "velplev@inbox.lv", "Own manufacturer (bag production)", MAYBE),
    ("Latvia", "Tailor Riga (SIA ALIAS-Z)", "https://www.tailorriga.lv", "", "Own manufacturer / artisan", NO),
    ("Latvia", "Eric Lasko Production", "https://ericlasko.com", "", "Artisan manufacturer (no outsourcing, no mass production)", NO),
    ("Latvia", "SB Ādas Dizains (Sandra Birze)", "https://sbadasdizains.lv", "sb@sbadasdizains.lv", "Artisan handmade manufacturer", NO),
    ("Latvia", "Buduart", "https://www.buduart.lv", "", "Own-design brand / own workshop", NO),
    ("Latvia", "Lakolina", "https://www.exporthub.com/lakolina/", "", "Directory listing; appears own-make - unverified", NO),

    # --- Estonia ---
    ("Estonia", "Gasell AS", "https://gasell.ee", "gasell@gasell.ee", "Wholesaler & importer (maaletooja) of bags/accessories", YES),
    ("Estonia", "Nabo Nahktooted OÜ", "https://nokiannahkatuote.fi", "nabo@nahkatuote.inet.fi", "Importer + manufacturer (imports finished bags/wallets)", YES),
    ("Estonia", "Bagy OÜ", "", "bettigehrke@gmail.com", "Wholesale agent for leather goods", YES),
    ("Estonia", "Fashion House Eesti OÜ", "", "leif.karlsson@meridiangroup.eu", "Wholesale agent for leather goods", YES),
    ("Estonia", "Stalcom OÜ", "https://stalcom.ee", "", "Custom leather goods producer + wholesale", MAYBE),
    ("Estonia", "Leather World OÜ", "https://leather-world.co", "sales@leather-world.co", "Leather materials / footwear distribution", NO),
    ("Estonia", "Nakro OÜ", "https://www.nakro.ee", "", "Leather materials / tannery", NO),

    # --- Czech Republic ---
    ("Czech Republic", "JUNI EXPORT-IMPORT s.r.o.", "https://www.juni.cz", "info@juni.cz", "Importer & wholesaler of leather goods", YES),
    ("Czech Republic", "PAUL BORDAS FASHION, s.r.o.", "https://www.paulbordas.cz", "info@paulbordas.cz", "Distributor/importer (represents foreign brands)", YES),
    ("Czech Republic", "UNIVARO – leather s.r.o.", "https://www.univaro.cz", "info@univaro.cz", "Exclusive importer/distributor of brands", YES),
    ("Czech Republic", "Kožená galanterie GaToLi (Libor Tomáš)", "https://e-jola.webnode.cz", "libor.tomas@avonet.cz", "Wholesaler/distributor of leather goods", YES),
    ("Czech Republic", "Gora (gora-velkoobchod)", "https://www.gora-velkoobchod.cz", "", "Wholesaler of leather goods (verify)", YES),
    ("Czech Republic", "Karoly (Letohrad)", "https://www.firmy.cz/detail/12856470-karoly-letohrad-cervena.html", "", "Wholesaler & importer of leather goods", YES),
    ("Czech Republic", "SEGALI", "https://www.segali.cz", "velkoobchod@segali.cz", "Own manufacturer + wholesale / private label", MAYBE),

    # --- Slovakia ---
    ("Slovakia", "Max s.r.o. (MAX Original Leather)", "https://maxleather.sk", "max@maxleather.sk", "Importer of Italian leather goods + wholesale", YES),
    ("Slovakia", "VEGA-LM (VegaLM)", "https://www.vegalm.sk", "vega@vegalm.sk", "Own manufacturer + wholesale/retail", MAYBE),
    ("Slovakia", "Arwel, s.r.o.", "https://www.arwel.sk", "", "Own manufacturer + wholesale", MAYBE),
    ("Slovakia", "NICOLAUS LEATHER, s.r.o.", "https://nicolausleather.sk", "", "Leather materials (bovine leather production)", NO),

    # --- Hungary ---
    ("Hungary", "Farkas Bőrdíszmű", "https://farkasbordiszmu.hu", "", "Importer/wholesaler - imports directly from India, China, Poland, Italy, Germany", YES),
    ("Hungary", "BI-KA Bőráru Kft.", "https://bikabor.hu", "bikabor@bikabor.hu", "Importer & wholesaler (imports from Italy etc.)", YES),
    ("Hungary", "Skin Bőrdíszmű Nagykereskedés (Skintaska)", "https://skintaska.hu", "", "Wholesaler/importer (Hungarian & imported goods)", YES),
    ("Hungary", "Synchrony LM (SLM / Bőrdíszműnagyker)", "https://bordiszmunagyker.hu", "info@bordiszmunagyker.hu", "Wholesaler of leather goods", YES),
    ("Hungary", "Kadro Bőrdíszmű Nagykereskedés", "https://kadro.hu", "info@kadro.hu", "Wholesaler (sells to resellers only)", YES),
    ("Hungary", "Top Bag 2000 Kft. (Karen)", "https://karennagyker.hu", "info@karen.hu", "Wholesaler/distributor of bag brands", YES),
    ("Hungary", "Zolferex Kft. (Nettáska)", "https://www.nettaska.hu", "info@zolferex.hu", "Importer/distributor (exclusive importer of EU brands)", YES),

    # --- Denmark ---
    ("Denmark", "Uni-Leather ApS", "https://uni-leather.dk", "", "Wholesale; makes own leather goods + imports shoes", MAYBE),
    ("Denmark", "Axelsen & Søn ApS (Montana/Treats)", "https://axelsenson.com", "info@axelsenson.com", "Manufacturer + B2B custom/personalized", MAYBE),
    ("Denmark", "Adax A/S", "https://adax.dk", "", "Own-design brand - already produces in India (OEM prospect)", MAYBE),
    ("Denmark", "Markberg", "https://markberg.dk", "salessupport@markberg.com", "Own-design brand - contract mfr worldwide (OEM prospect)", MAYBE),
    ("Denmark", "Still Nordic", "https://stillnordic.dk", "", "Own-design brand (OEM prospect)", MAYBE),
    ("Denmark", "dbramante1928", "https://www.dbramante1928.com", "", "Own-design brand (cases/bags)", MAYBE),
    ("Denmark", "Depeche (Depeche Denmark)", "https://www.depeche.dk", "", "Own-design brand", MAYBE),
    ("Denmark", "SIPO Trading K/S", "https://sipo.dk", "", "Leather / skins / fur materials", NO),
    ("Denmark", "Sicadan", "https://www.sicadan.dk", "info@sicadan.dk", "Leather materials for manufacturers", NO),
]

HEADERS = ["Country", "Company Name", "WWW", "E-mail", "Business type", "Fit for buying Indian leather goods"]

HEADER_FILL = PatternFill("solid", fgColor="1F4E78")
HEADER_FONT = Font(bold=True, color="FFFFFF", size=11)
THIN = Side(style="thin", color="D9D9D9")
BORDER = Border(left=THIN, right=THIN, top=THIN, bottom=THIN)
LINK_FONT = Font(color="0563C1", underline="single")

FIT_FILL = {
    YES: PatternFill("solid", fgColor="E2EFDA"),   # green
    MAYBE: PatternFill("solid", fgColor="FFF2CC"),  # amber
    NO: PatternFill("solid", fgColor="FCE4D6"),     # red
}
WIDTHS = [16, 42, 42, 32, 52, 60]


def write_sheet(ws, rows):
    ws.append(HEADERS)
    for col in range(1, len(HEADERS) + 1):
        c = ws.cell(row=1, column=col)
        c.fill = HEADER_FILL
        c.font = HEADER_FONT
        c.alignment = Alignment(horizontal="left", vertical="center")
        c.border = BORDER

    for country, name, www, email, btype, fit in rows:
        ws.append([country, name, www, email, btype, fit])
        r = ws.max_row
        if www:
            cell = ws.cell(row=r, column=3)
            cell.hyperlink = www
            cell.font = LINK_FONT
        if email:
            cell = ws.cell(row=r, column=4)
            cell.hyperlink = f"mailto:{email}"
            cell.font = LINK_FONT
        for col in range(1, len(HEADERS) + 1):
            cell = ws.cell(row=r, column=col)
            cell.border = BORDER
            cell.alignment = Alignment(vertical="center", wrap_text=(col in (5, 6)))
        ws.cell(row=r, column=6).fill = FIT_FILL[fit]

    for i, w in enumerate(WIDTHS, start=1):
        ws.column_dimensions[get_column_letter(i)].width = w
    ws.freeze_panes = "A2"
    ws.auto_filter.ref = f"A1:{get_column_letter(len(HEADERS))}{ws.max_row}"


def main():
    wb = Workbook()
    ws_all = wb.active
    ws_all.title = "All companies"
    write_sheet(ws_all, ROWS)

    priority = [r for r in ROWS if r[5] == YES]
    ws_pri = wb.create_sheet("Priority targets")
    write_sheet(ws_pri, priority)

    out = "Leather_Goods_Wholesalers.xlsx"
    wb.save(out)
    n_yes = sum(1 for r in ROWS if r[5] == YES)
    n_maybe = sum(1 for r in ROWS if r[5] == MAYBE)
    n_no = sum(1 for r in ROWS if r[5] == NO)
    print(f"Wrote {out}: {len(ROWS)} companies total "
          f"(Yes={n_yes}, Maybe={n_maybe}, No={n_no}).")


if __name__ == "__main__":
    main()
