"""Builds lista-importerow.xlsx and lista-importerow.md from the lists below.

Run: python3 build.py   (requires openpyxl)
"""
from pathlib import Path
from urllib.parse import urlsplit

from openpyxl import Workbook
from openpyxl.styles import Alignment, Font, PatternFill

P = True  # Polish producer

LISTS = [
    ("Bielizna", "Największy importer bielizny", [
        ("LPP S.A. (Sinsay, Reserved, Cropp, House, Mohito)", "https://www.lpp.com"),
        ("Pepco Poland", "https://pepco.pl"),
        ("Biedronka (Jeronimo Martins Polska)", "https://www.biedronka.pl"),
        ("Lidl Polska", "https://www.lidl.pl"),
        ("Esotiq & Henderson S.A. (Henderson)", "https://henderson.pl"),
        ("Atlantic", "https://www.atlantic.pl", P),
        ("Primark Polska", "https://www.primark.com/pl-pl"),
        ("KiK Polska", "https://www.kik.pl"),
        ("Takko Fashion Polska", "https://www.takko.com/pl-pl"),
        ("H&M Polska", "https://www2.hm.com/pl_pl"),
        ("Moraj", "https://moraj.pl"),
        ("4F (OTCF S.A.)", "https://4f.com.pl"),
        ("Calzedonia Group Polska (Tezenis, Intimissimi)", "https://www.tezenis.com/pl"),
        ("Kaufland Polska", "https://www.kaufland.pl"),
        ("Carrefour Polska", "https://www.carrefour.pl"),
        ("Auchan Polska", "https://www.auchan.pl"),
        ("Decathlon Polska", "https://www.decathlon.pl"),
        ("Answear.com", "https://answear.com"),
        ("Modivo", "https://modivo.pl"),
        ("Cornette", "https://cornette.pl", P),
        ("Key", "https://key.com.pl", P),
        ("Gatta", "https://gatta.pl", P),
        ("Julimex", "https://julimex.pl", P),
        ("LA/MA (Lama)", "https://lama.com.pl", P),
        ("Babell", "https://babell.com.pl", P),
        ("Wol-Bar", "https://wol-bar.com.pl", P),
        ("Brubeck", "https://brubeck.pl", P),
        ("BieliznaCentrum.pl", "https://bieliznacentrum.pl"),
        ("Mada.pl", "https://www.mada.pl"),
        ("Kentex", "https://kentex.com.pl"),
    ]),
    ("Skarpety", "Największy importer skarpet", [
        ("LPP S.A. (Sinsay, Reserved, Cropp, House)", "https://www.lpp.com"),
        ("Pepco Poland", "https://pepco.pl"),
        ("Biedronka (Jeronimo Martins Polska)", "https://www.biedronka.pl"),
        ("Lidl Polska", "https://www.lidl.pl"),
        ("Action Polska", "https://www.action.com/pl-pl"),
        ("KiK Polska", "https://www.kik.pl"),
        ("Primark Polska", "https://www.primark.com/pl-pl"),
        ("4F (OTCF S.A.)", "https://4f.com.pl"),
        ("Decathlon Polska", "https://www.decathlon.pl"),
        ("HalfPrice", "https://halfprice.eu/pl"),
        ("JS Sp. z o.o. (Lublin)", "https://www.js.com.pl"),
        ("Moraj", "https://moraj.pl"),
        ("All-Best", "https://www.allbest.pl"),
        ("Wukong Hurtownia", "https://wukonghurtownia.pl"),
        ("Skarpex", "https://www.skarpex.pl"),
        ("Pesail Polska", "https://pesail-polska.pl"),
        ("Modivo", "https://modivo.pl"),
        ("Smyk", "https://www.smyk.com/pl/pl"),
        ("Atlantic", "https://www.atlantic.pl", P),
        ("Cornette", "https://cornette.pl", P),
        ("Wola", "https://wola.pl", P),
        ("Steven", "https://steven.pl", P),
        ("Gatta", "https://gatta.pl", P),
        ("Marilyn", "https://e-marilyn.pl", P),
        ("Milena", "https://milena-skarpety.pl", P),
        ("Soxo", "https://soxo.pl"),
        ("Many Mornings", "https://manymornings.com", P),
        ("Spox Sox", "https://spoxsox.pl", P),
        ("Todo Socks", "https://www.todosocks.pl", P),
        ("Bratex", "http://www.bratexskarpetki.pl", P),
    ]),
    ("Piżamy", "Największy importer piżam", [
        ("LPP S.A. (Sinsay, Reserved, House, Mohito)", "https://www.lpp.com"),
        ("Pepco Poland", "https://pepco.pl"),
        ("Primark Polska", "https://www.primark.com/pl-pl"),
        ("Biedronka (Jeronimo Martins Polska)", "https://www.biedronka.pl"),
        ("Lidl Polska", "https://www.lidl.pl"),
        ("KiK Polska", "https://www.kik.pl"),
        ("HalfPrice", "https://halfprice.eu/pl"),
        ("Smyk", "https://www.smyk.com/pl/pl"),
        ("Modivo", "https://modivo.pl"),
        ("Esotiq", "https://esotiq.com/pl/pl"),
        ("Henderson", "https://henderson.pl"),
        ("Atlantic", "https://www.atlantic.pl", P),
        ("Key", "https://key.com.pl", P),
        ("Italian Fashion", "https://www.italianfashion.pl", P),
        ("Taro", "https://taro.pl", P),
        ("Cornette", "https://cornette.pl", P),
        ("Doctor Nap (dawniej Dobranocka)", "https://doctornap.com/pl", P),
        ("JS Sp. z o.o. (Lublin)", "https://www.js.com.pl"),
        ("Moraj", "https://moraj.pl"),
        ("Vienetta / Nightex", "https://vienetta.pl"),
        ("Hurtownia WEGA (Wrocław)", "https://www.wega.wroc.pl"),
        ("Kuba", "https://kubapizama.pl", P),
        ("Regina", "https://regina.pl", P),
        ("M-Max", "https://m-max.com.pl", P),
        ("Donna", "https://www.bedonna.pl", P),
        ("Sesto Senso", "https://sestosenso24.pl", P),
        ("Cana Nouvelle", "https://cana.pl", P),
        ("Babell", "https://babell.com.pl", P),
        ("Dkaren", "https://dkaren.pl", P),
        ("Gatta", "https://gatta.pl", P),
    ]),
    ("Biustonosze", "Największy importer staników", [
        ("LPP S.A. (Sinsay, Reserved, Mohito)", "https://www.lpp.com"),
        ("Pepco Poland", "https://pepco.pl"),
        ("Esotiq & Henderson S.A. (Esotiq)", "https://esotiq.com"),
        ("Lidl Polska", "https://www.lidl.pl"),
        ("Primark Polska", "https://www.primark.com/pl-pl"),
        ("Hunkemöller Polska", "https://www.hunkemoller.pl"),
        ("Calzedonia Group Polska (Intimissimi, Tezenis)", "https://www.intimissimi.com/pl"),
        ("Triumph Polska", "https://pl.triumph.com"),
        ("H&M Polska", "https://www2.hm.com/pl_pl"),
        ("Etam Polska", "https://www.etam.pl"),
        ("KiK Polska", "https://www.kik.pl"),
        ("Takko Fashion Polska", "https://www.takko.com/pl-pl"),
        ("Answear.com", "https://answear.com"),
        ("Modivo", "https://modivo.pl"),
        ("Dorina", "https://dorina.pl"),
        ("Gorteks", "https://www.gorteks.com.pl", P),
        ("Obsessive", "https://obsessive.com"),
        ("Kontri.pl", "https://www.kontri.pl"),
        ("Ava Lingerie", "https://avalingerie.pl", P),
        ("Krisline", "https://krisline.com", P),
        ("Gaia", "https://www.gaia.com.pl", P),
        ("Gorsenia", "https://gorsenia.pl", P),
        ("Mefemi (dawniej Nipplex)", "https://mefemi.pl", P),
        ("Ewa Bien", "https://ewabien.com", P),
        ("MAT Lingerie", "https://matlingerie.pl", P),
        ("Samanta", "https://samanta.pl", P),
        ("Julimex", "https://julimex.pl", P),
        ("Konrad Lingerie", "https://konrad-bielizna.pl", P),
        ("Lupoline", "https://esklep.lupoline.pl", P),
        ("Lapinee", "https://lapinee.pl"),
    ]),
    ("Bielizna z Turcji", "Największy importer bielizny z Turcji", [
        ("Duman Polska Sp. z o.o.", "https://www.dumanpolska.com.pl"),
        ("Raj-Pol (Częstochowa)", "https://raj-pol.com.pl", P),
        ("FactoryPrice.eu", "https://factoryprice.eu"),
        ("LC Waikiki (sklepy w Polsce)", "https://corporate.lcwaikiki.com"),
        ("NANA Vienetta Polska", "https://vienettahurt.pl"),
        ("Belbest Sp. z o.o.", "https://belbest.com.pl"),
        ("Luka Hurt Sp. z o.o.", "https://hurtownialuka.pl"),
        ("Vienetta – Klaudia Cieplak", "https://vienetta.pl"),
        ("ASG3HURT", "https://asg3hurt.com"),
        ("CentrumHurt", "https://centrumhurt.pl"),
        ("S&D Bielizna Turecka (GD Center)", "https://gdonline.pl/SD-Bielizna-Turecka/pr/100"),
        ("HurtowniaWolka.com / WolkaCentrum.com", "https://hurtowniawolka.com"),
        ("KOZA Underwear Polska (GD Center)", "https://gdonline.pl/KOZA-Underwear/pr/47"),
        ("Larado", "http://larado.pl"),
        ("BETA&PLUS", "https://www.hurt-odziez.pl"),
        ("24Hurt", "https://24hurt.eu"),
        ("LPP S.A.", "https://www.lpp.com"),
        ("Pepco Poland", "https://pepco.pl"),
        ("Moraj", "https://moraj.pl"),
        ("Esotiq & Henderson S.A.", "https://esotiqhenderson.com"),
    ]),
    ("Piżamy z Turcji", "Największy importer piżam z Turcji", [
        ("Duman Polska Sp. z o.o.", "https://pizamahurt.eu"),
        ("FactoryPrice.eu", "https://factoryprice.eu"),
        ("Raj-Pol (Częstochowa)", "https://raj-pol.com.pl", P),
        ("Morella (HASSEM Sp. z o.o.)", "https://morellahurt.pl"),
        ("LC Waikiki (sklepy w Polsce)", "https://corporate.lcwaikiki.com"),
        ("NANA Vienetta Polska", "https://vienettahurt.pl"),
        ("Vienetta – Klaudia Cieplak", "https://vienetta.pl"),
        ("Luka Hurt Sp. z o.o.", "https://hurtownialuka.pl"),
        ("Belbest Sp. z o.o.", "https://belbest.com.pl"),
        ("ANIAPHU – Hurtownia Piżam", "https://www.piżamyhurt.pl"),
        ("HurtowniaWolka.com", "https://hurtowniawolka.com"),
        ("ASG3HURT", "https://asg3hurt.com"),
        ("Tuva Home Sp. z o.o.", "https://sklep.tuvahome.pl"),
        ("CentrumHurt", "https://centrumhurt.pl"),
        ("S&D Bielizna Turecka (GD Center)", "https://gdonline.pl/SD-Bielizna-Turecka/pr/100"),
        ("KOZA Underwear Polska (GD Center)", "https://gdonline.pl/KOZA-Underwear/pr/47"),
        ("24Hurt", "https://24hurt.eu"),
        ("BETA&PLUS", "https://www.hurt-odziez.pl"),
        ("HurtWolka24.pl", "https://hurtwolka24.pl"),
        ("Wolka-Centrum.eu", "https://wolka-centrum.eu"),
        ("Jabos.pl", "https://jabos.pl"),
        ("Bucik Sklep", "https://buciksklep.pl"),
        ("LPP S.A.", "https://www.lpp.com"),
        ("Pepco Poland", "https://pepco.pl"),
        ("Moraj", "https://moraj.pl"),
        ("Esotiq & Henderson S.A.", "https://esotiqhenderson.com"),
    ]),
]

NOTES = [
    "Kolejność jest szacunkowa (wielkość i znaczenie firmy) – brak publicznych danych o wolumenie importu w tych kategoriach.",
    "Wszystkie adresy WWW zostały sprawdzone (strona otwarta lub potwierdzona w wynikach wyszukiwania) w październiku 2026.",
    "Esotiq i Henderson należą do jednej grupy (Esotiq & Henderson S.A.) – jeden kontakt zakupowy.",
    "Sieci zagraniczne (Biedronka, Lidl, Action, Primark, H&M, KiK, Takko, Calzedonia, Triumph, Hunkemöller) często kupują centralnie poza Polską.",
    "Listy „z Turcji”: na końcu listy (LPP, Pepco, Moraj, Esotiq & Henderson) są duzi gracze, dla których Turcja to niewielka część zaopatrzenia.",
    "Dwie firmy podają się za oficjalnego dystrybutora Vienetta (NANA Vienetta Polska – Ptak Rzgów; Klaudia Cieplak – EACC Wólka).",
    "S&D Bielizna Turecka i KOZA Underwear mają tylko profile na gdonline.pl (stoiska w GD Center, Wólka Kosowska).",
    "Pominięto PERUSS (polski dystrybutor tureckiej marki Doreanse) – domeny doreanse.eu i doreanse-shop.pl już nie działają.",
    "ANIAPHU: adres z polską literą „ż” – www.piżamyhurt.pl (zapis punycode: www.xn--piamyhurt-ccc.pl).",
]

HERE = Path(__file__).parent


def rows(entries):
    for i, (name, url, *flag) in enumerate(entries, 1):
        yield i, name, url, "tak" if flag else ""


def ascii_url(url):
    """Excel can't open hyperlinks with non-ASCII host names, so use punycode for those."""
    parts = urlsplit(url)
    return parts._replace(netloc=parts.netloc.encode("idna").decode()).geturl()


def build_xlsx():
    wb = Workbook()
    wb.remove(wb.active)
    head_fill = PatternFill("solid", fgColor="081F45")
    for sheet, title, entries in LISTS:
        ws = wb.create_sheet(sheet)
        ws.append([title])
        ws["A1"].font = Font(bold=True, size=13)
        ws.append(["#", "Nazwa", "WWW", "Polski producent"])
        for cell in ws[2]:
            cell.font = Font(bold=True, color="FFFFFF")
            cell.fill = head_fill
        for i, name, url, prod in rows(entries):
            ws.append([i, name, url, prod])
            link = ws.cell(row=ws.max_row, column=3)
            link.hyperlink = ascii_url(url)
            link.font = Font(color="0D4C9A", underline="single")
        for col, width in zip("ABCD", (5, 52, 50, 17)):
            ws.column_dimensions[col].width = width
        for row in ws.iter_rows(min_row=3, min_col=4, max_col=4):
            row[0].alignment = Alignment(horizontal="center")
        ws.freeze_panes = "A3"
    wb.save(HERE / "lista-importerow.xlsx")


def build_md():
    out = ["# Importerzy bielizny, skarpet i piżam – Polska", "",
           "Kolumna „PL prod.” = polski producent. Pełna lista w `lista-importerow.xlsx` (jedna zakładka na kategorię).", ""]
    for _, title, entries in LISTS:
        out += [f"## {title} ({len(entries)})", "", "| # | Nazwa | WWW | PL prod. |", "|---|---|---|---|"]
        out += [f"| {i} | {name} | {url} | {prod} |" for i, name, url, prod in rows(entries)]
        out.append("")
    out += ["## Uwagi", ""] + [f"- {note}" for note in NOTES] + [""]
    (HERE / "lista-importerow.md").write_text("\n".join(out), encoding="utf-8")


if __name__ == "__main__":
    build_xlsx()
    build_md()
    for _, title, entries in LISTS:
        print(f"{len(entries):3d}  {title}")
