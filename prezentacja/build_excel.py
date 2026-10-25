#!/usr/bin/env python3
"""Generuje prezentacja-os.xlsx z treści slajdów."""
from openpyxl import Workbook
from openpyxl.styles import Font, Alignment, PatternFill, Border, Side
from openpyxl.utils import get_column_letter

HEADER_FILL = PatternFill("solid", fgColor="1A365D")
HEADER_FONT = Font(bold=True, color="FFFFFF", size=11)
TITLE_FONT = Font(bold=True, size=14, color="1A365D")
SLIDE_TITLE_FONT = Font(bold=True, size=12)
BODY_FONT = Font(size=11)
THIN = Side(style="thin", color="CCCCCC")
BORDER = Border(left=THIN, right=THIN, top=THIN, bottom=THIN)
wrap = Alignment(wrap_text=True, vertical="top")
center = Alignment(horizontal="center", vertical="center", wrap_text=True)


def style_table(sheet):
    for col in range(1, sheet.max_column + 1):
        c = sheet.cell(1, col)
        c.font = HEADER_FONT
        c.fill = HEADER_FILL
        c.alignment = center
        c.border = BORDER
    for r in range(2, sheet.max_row + 1):
        for col in range(1, sheet.max_column + 1):
            cell = sheet.cell(r, col)
            cell.border = BORDER
            cell.font = BODY_FONT
            cell.alignment = wrap
    for col in range(1, sheet.max_column + 1):
        sheet.column_dimensions[get_column_letter(col)].width = 28


def main():
    wb = Workbook()

    slides = [
        ("Wstęp", "Urządzenia I/O, magistrale i uruchamianie komputera",
         "Przedmiot: Systemy operacyjne / architektura komputera\nKrótkie omówienie — ok. 15 minut", 1),
        ("Plan", "Plan prezentacji",
         "1. Urządzenia wejścia-wyjścia — jak CPU współpracuje ze sprzętem\n"
         "2. Magistrale — łącza wewnątrz komputera\n"
         "3. Uruchamianie komputera — od włączenia zasilania do systemu operacyjnego", 1),
        ("I/O", "Urządzenia wejścia-wyjścia (I/O)",
         "• Urządzenia zewnętrzne: klawiatura, dysk, karta sieciowa, drukarka…\n"
         "• CPU nie komunikuje się z nimi bezpośrednio — pośredniczy sterownik urządzenia (kontroler):\n"
         "  – rejestry stanu i sterowania\n"
         "  – bufor lokalny na dane\n"
         "• System operacyjny udostępnia urządzenia procesom przez sterowniki i warstwę abstrakcji (pliki, gniazda).", 1.5),
        ("I/O", "Trzy metody transferu danych I/O",
         "Odpytywanie (polling): CPU w pętli sprawdza gotowość urządzenia — proste, małe systemy.\n"
         "Przerwania: CPU pracuje dalej; urządzenie sygnalizuje zakończenie — klawiatura, mysz.\n"
         "DMA: układ sam przenosi bloki RAM ↔ urządzenie — dyski, sieć, duże transfery.\n"
         "(Szczegóły w arkuszu Tabela_I_O.)", 1.5),
        ("I/O", "Odpytywanie vs przerwania vs DMA",
         "Polling — prosty kod, marnowanie cykli CPU (aktywne czekanie).\n"
         "I/O sterowane przerwaniami — lepsze wykorzystanie CPU; procedura obsługi przerwania (ISR).\n"
         "DMA — procesor inicjuje transfer; po bloku jedno przerwanie; minimalne obciążenie CPU.", 1),
        ("I/O", "Przerwania wielokrotne i spooling",
         "• Wiele przerwań naraz: obsługa sekwencyjna, zagnieżdżona lub priorytetowa.\n"
         "• Spooling — buforowanie strumienia (np. kolejka wydruków na dysku).\n"
         "• Powiązanie z SO: planowanie, kolejki urządzeń, synchronizacja.", 1),
        ("Magistrale", "Magistrala systemowa — definicja",
         "Magistrala = wspólne linie + logika sterująca + protokół wymiany danych między:\n"
         "• procesorem (CPU)\n• pamięcią RAM\n• kontrolerami I/O", 1),
        ("Magistrale", "Trzy podstawowe magistrale",
         "Adresowa — gdzie w pamięci lub który port I/O (n linii → do 2^n adresów).\n"
         "Danych — co jest przesyłane (szerokość np. 32/64 bitów na cykl).\n"
         "Sterująca — READ/WRITE, zegar, reset, żądania przerwań.", 1),
        ("Magistrale", "Ewolucja: równoległa → szeregowa",
         "Równoległe szyny (PCI, AGP, ATA): crosstalk, clock skew przy wysokich częstotliwościach.\n"
         "Szeregowe łącza punkt–punkt (PCIe, SATA, USB): wyższa przepustowość, full-duplex.\n"
         "Dziś dominują: PCI Express, SATA/M.2, USB.", 1),
        ("Magistrale", "Przykładowe standardy",
         "PCI/AGP — równoległy, starsze rozszerzenia i GPU.\n"
         "PCIe — szeregowy punkt–punkt, GPU, NVMe.\n"
         "SATA/M.2 — pamięci masowe.\n"
         "USB — urządzenia peryferyjne.\n"
         "I²C/SPI/UART — embedded, IoT.\n"
         "(Tabela w arkuszu Tabela_Standardy.)", 1),
        ("Boot", "Uruchamianie komputera (bootstrapping)",
         "Cel: od włączenia zasilania do działającego jądra systemu operacyjnego.\n"
         "Firmware: BIOS (legacy) lub UEFI (nowoczesny standard).", 1),
        ("Boot", "BIOS a UEFI",
         "BIOS: MBR (max ~2 TB, 4 partycje podst.), interfejs tekstowy.\n"
         "UEFI: GPT (>2 TB), interfejs graficzny, Secure Boot.\n"
         "Oba: kod w Flash/ROM na płycie głównej — pierwszy software po resecie sprzętowym.", 1.5),
        ("Boot", "Etapy rozruchu",
         "1. POST — test CPU, RAM, GPU, chłodzenia\n"
         "2. Wybór nośnika — MBR lub partycja EFI System\n"
         "3. Bootloader — GRUB, Windows Boot Manager\n"
         "4. Ładowanie jądra SO + sterowniki (HAL)\n"
         "5. Usługi użytkownika — sesja, logowanie, pulpit", 1.5),
        ("Boot", "MBR i GPT — po co to w SO?",
         "MBR: pierwszy sektor (512 B), limit 2 TB i liczby partycji.\n"
         "GPT: duże dyski, spójność z UEFI.\n"
         "Bootloader ładuje jądro — wtedy SO przejmuje procesy, pamięć i I/O.", 1),
        ("Podsumowanie", "Podsumowanie",
         "• I/O: sterowniki; polling, przerwania, DMA\n"
         "• Magistrale: adres, dane, sterowanie; PCIe/USB/SATA\n"
         "• Start: POST → firmware → bootloader → jądro SO", 1),
        ("Źródła", "Źródła",
         "1. Materiał dydaktyczny (PDF): Architektura komputerów: I/O, magistrale i booting "
         "(architektura-komputerow-io-magistrale-bios.pdf)\n"
         "2. A. Silberschatz, P. B. Galvin, G. Gagne, Systemy operacyjne, Wydanie V, PWN\n"
         "Opcjonalnie: dokumentacja chipsetów, UEFI Forum, materiały wykładowe.", 1),
        ("Koniec", "Dziękuję za uwagę",
         "Pytania?", 0.5),
    ]

    row_heights = [45, 50, 95, 85, 75, 70, 65, 70, 75, 95, 50, 70, 95, 70, 65, 85, 40]

    ws = wb.active
    ws.title = "Slajdy"
    headers = ["Lp.", "Sekcja", "Tytuł slajdu", "Treść (do prezentacji)", "Czas [min]"]
    ws.append(headers)
    for col in range(1, len(headers) + 1):
        c = ws.cell(row=1, column=col)
        c.font = HEADER_FONT
        c.fill = HEADER_FILL
        c.alignment = center
        c.border = BORDER

    for i, (sec, title, body, mins) in enumerate(slides, 1):
        ws.append([i, sec, title, body, mins])
        r = ws.max_row
        ws.cell(r, 1).alignment = center
        ws.cell(r, 5).alignment = center
        for col in range(1, 6):
            ws.cell(r, col).border = BORDER
            ws.cell(r, col).font = BODY_FONT
        ws.cell(r, 3).font = SLIDE_TITLE_FONT
        ws.cell(r, 4).alignment = wrap
        ws.row_dimensions[r].height = row_heights[i - 1]

    ws.column_dimensions["A"].width = 5
    ws.column_dimensions["B"].width = 14
    ws.column_dimensions["C"].width = 38
    ws.column_dimensions["D"].width = 72
    ws.column_dimensions["E"].width = 10

    total_min = sum(s[3] for s in slides)
    footer = ws.max_row + 2
    ws.cell(footer, 3, "Suma czasu (szac.):").font = Font(bold=True)
    ws.cell(footer, 5, total_min).font = Font(bold=True)

    ws2 = wb.create_sheet("Tabela_I_O")
    ws2.append(["Metoda", "Rola procesora", "Zaangażowanie CPU", "Zastosowanie"])
    for row in [
        ("Odpytywanie (polling)", "Ciągłe testowanie stanu sterownika", "Bardzo wysokie", "Małe, szybkie I/O"),
        ("Przerwania", "Inicjalizacja + obsługa przerwania", "Umiarkowane", "Klawiatura, mysz, porty"),
        ("DMA", "Inicjalizacja i sygnał końca bloku", "Minimalne", "Dyski, karty sieciowe"),
    ]:
        ws2.append(list(row))
    style_table(ws2)

    ws3 = wb.create_sheet("Tabela_Standardy")
    ws3.append(["Standard", "Typ transmisji", "Architektura", "Zastosowanie"])
    for row in [
        ("PCI", "Równoległa 32/64-bit", "Szyna współdzielona", "Starsze karty rozszerzeń"),
        ("AGP", "Równoległa 32-bit", "Dedykowany kanał GPU", "Karta graficzna – RAM"),
        ("PCI Express", "Szeregowa", "Punkt–punkt", "GPU, dyski NVMe"),
        ("SATA / M.2", "Szeregowa", "Dupleks / PCIe NVMe", "Pamięci masowe"),
        ("USB", "Szeregowa", "Magistrala / hub", "Urządzenia peryferyjne"),
        ("I²C / SPI / UART", "Szeregowa", "Master–Slave", "Embedded, IoT"),
    ]:
        ws3.append(list(row))
    style_table(ws3)

    ws4 = wb.create_sheet("Tabela_BIOS_UEFI")
    ws4.append(["Cecha", "BIOS", "UEFI"])
    for row in [
        ("Partycjonowanie", "MBR (max ~2 TB, 4 part. podst.)", "GPT (>2 TB, wiele partycji)"),
        ("Interfejs", "Tekstowy", "Często graficzny"),
        ("Bezpieczeństwo", "Ograniczone", "Secure Boot"),
        ("Nośnik kodu", "Flash/ROM na płycie głównej", "Flash/ROM na płycie głównej"),
    ]:
        ws4.append(list(row))
    style_table(ws4)

    ws5 = wb.create_sheet("Info")
    ws5["A1"] = "Prezentacja: Urządzenia I/O, magistrale, uruchamianie komputera"
    ws5["A1"].font = TITLE_FONT
    info = [
        ("Jak używać:", ""),
        ("1.", "Arkusz Slajdy — każdy wiersz = jeden slajd (~15 min łącznie)."),
        ("2.", "Prezentacja: ukryj nagłówki, powiększ widok lub drukuj (1 wiersz = 1 strona)."),
        ("3.", "Arkusze Tabela_* — materiał pomocniczy do slajdów z tabelami."),
        ("4.", "Alternatywnie: prezentacja-os.pdf (Marp) w tym folderze."),
    ]
    for i, (a, b) in enumerate(info, start=3):
        ws5.cell(i, 1, a)
        ws5.cell(i, 2, b)
        ws5.cell(i, 2).alignment = wrap
    ws5.column_dimensions["A"].width = 14
    ws5.column_dimensions["B"].width = 78

    out = "/workspace/prezentacja/prezentacja-os.xlsx"
    wb.save(out)
    print(f"Zapisano: {out}")


if __name__ == "__main__":
    main()
