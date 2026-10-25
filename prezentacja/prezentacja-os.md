---
marp: true
theme: default
paginate: true
size: 16:9
style: |
  section {
    font-family: 'Segoe UI', system-ui, sans-serif;
  }
  section.lead h1 {
    text-align: center;
  }
  section.lead p {
    text-align: center;
  }
  table {
    font-size: 0.78em;
  }
  h2 {
    color: #1a365d;
  }
---

<!-- _class: lead -->

# Urządzenia I/O, magistrale i uruchamianie komputera

**Przedmiot: Systemy operacyjne / architektura komputera**

Krótkie omówienie — ok. **15 minut**

---

## Plan prezentacji

1. **Urządzenia wejścia-wyjścia** — jak CPU współpracuje ze sprzętem
2. **Magistrale** — łącza wewnątrz komputera
3. **Uruchamianie komputera** — od włączenia zasilania do systemu operacyjnego

---

## Urządzenia wejścia-wyjścia (I/O)

- **Urządzenia zewnętrzne**: klawiatura, dysk, karta sieciowa, drukarka…
- CPU **nie** „rozmawia” z nimi bezpośrednio — pośredniczy **sterownik urządzenia** (kontroler):
  - rejestry **stanu** i **sterowania**
  - **bufor lokalny** na dane

System operacyjny udostępnia urządzenia procesom przez **sterowniki** i warstwę abstrakcji (np. pliki, gniazda).

---

## Trzy metody transferu danych I/O

| Metoda | Idea | Typowe zastosowanie |
|--------|------|---------------------|
| **Odpytywanie (polling)** | CPU w pętli sprawdza, czy urządzenie gotowe | Proste, wolne urządzenia; małe systemy |
| **Przerwania** | CPU pracuje dalej; urządzenie **sygnalizuje** zakończenie | Klawiatura, mysz, porty |
| **DMA** | Specjalny układ **sam** przenosi bloki RAM ↔ urządzenie | Dyski, sieć — duże transfery |

---

## Odpytywanie vs przerwania vs DMA

**Polling** — prosty kod, ale **marnowanie cykli CPU** (aktywne czekanie).

**I/O sterowane przerwaniami** — lepsze wykorzystanie procesora; po zdarzeniu CPU wykonuje **procedurę obsługi przerwania** (ISR).

**DMA** — procesor tylko **inicjuje** transfer; po całym bloku — **jedno** przerwanie. Minimalne obciążenie CPU przy dużych danych.

---

## Przerwania wielokrotne i spooling (skrót)

- Przy wielu sygnałach naraz: obsługa **sekwencyjna**, **zagnieżdżona** lub **priorytetowa** (poziomy priorytetu w jądrze).
- **Spooling** — buforowanie strumienia (np. kolejka wydruków na dysku), aby proces użytkownika nie czekał na wolne urządzenie.

*Powiązanie z SO: planowanie, kolejki urządzeń, synchronizacja.*

---

## Magistrala systemowa — definicja

**Magistrala** = wspólne linie + logika sterująca + ustalony **protokół** wymiany danych między:

- procesorem (CPU),
- pamięcią RAM,
- kontrolerami I/O.

Bez magistrali komponenty nie mogłyby współdzielić adresów i danych w spójny sposób.

---

## Trzy podstawowe magistrale

| Magistrala | Funkcja |
|------------|---------|
| **Adresowa** | *Gdzie* w pamięci lub *który* port I/O (np. *n* linii → do 2^*n* adresów) |
| **Danych** | *Co* jest przesyłane (szerokość np. 32/64 bitów na cykl) |
| **Sterująca** | Sygnały READ/WRITE, zegar, reset, **żądania przerwań** |

---

## Ewolucja: równoległa → szeregowa

- **Równoległe** szyny (PCI, AGP, ATA): wiele bitów naraz → przy wysokich częstotliwościach problemy (**crosstalk**, **clock skew**).
- **Szeregowe łącza punkt–punkt** (PCIe, SATA, USB): wyższa efektywna przepustowość, **full-duplex**, mniejsze złącza.

Na płycie głównej dominują dziś **PCI Express**, **SATA/M.2**, **USB**.

---

## Przykładowe standardy (skrót)

| Standard | Typ | Zastosowanie |
|----------|-----|--------------|
| PCI / AGP | równoległy | starsze rozszerzenia, GPU (AGP) |
| **PCIe** | szeregowy, punkt–punkt | GPU, NVMe |
| **SATA / M.2** | szeregowy | dyski twarde i SSD |
| **USB** | szeregowy | urządzenia peryferyjne |
| I²C / SPI / UART | szeregowy | embedded, IoT |

---

## Uruchamianie komputera (bootstrapping)

**Cel:** od momentu **włączenia zasilania** do działającego **jądra systemu operacyjnego** (i dalej — interfejs użytkownika).

Kluczowy element firmware: **BIOS** (legacy) lub **UEFI** (nowoczesny standard).

---

## BIOS a UEFI

| | **BIOS** | **UEFI** |
|---|----------|----------|
| Partycjonowanie | **MBR** (max ~2 TB, 4 partycje podst.) | **GPT** (>2 TB, wiele partycji) |
| Interfejs | tekstowy | często graficzny |
| Bezpieczeństwo | ograniczone | m.in. **Secure Boot** |

Oba: kod w **Flash/ROM** na płycie głównej, pierwszy software po hardware reset.

---

## Etapy rozruchu (uproszczony schemat)

1. **POST** — test sprzętu (CPU, RAM, GPU, chłodzenie…)
2. **Wybór nośnika rozruchowego** — odczyt **MBR** lub partycji **EFI System**
3. **Bootloader** — np. GRUB, Windows Boot Manager
4. **Ładowanie jądra SO** + sterowniki (HAL, moduły jądra)
5. **Usługi użytkownika** — sesja, logowanie, powłoka graficzna

---

## MBR i GPT — po co to w SO?

- **MBR**: pierwszy sektor dysku (512 B), tablica partycji, **limit 2 TB** i liczby partycji.
- **GPT**: nowoczesna tablica partycji, spójna z **UEFI** i dużymi dyskami.

Bootloader ładuje **jądro** — dopiero wtedy pełne zarządzanie procesami, pamięcią i I/O przejmuje **system operacyjny**.

---

<!-- _class: lead -->

## Podsumowanie

- **I/O**: sterowniki urządzeń; polling, przerwania, **DMA**
- **Magistrale**: adres, dane, sterowanie; trend na **PCIe/USB/SATA**
- **Start**: **POST → firmware → bootloader → jądro SO**

Te warstwy łączą **sprzęt** z abstrakcjami, którymi operuje system operacyjny.

---

## Źródła

1. **Materiał dydaktyczny (PDF):** *Architektura komputerów: I/O, magistrale i booting* — interakcja CPU–I/O, magistrala systemowa, BIOS/UEFI *(plik: `architektura-komputerow-io-magistrale-bios.pdf`)*
2. **A. Silberschatz, P. B. Galvin, G. Gagne**, *Systemy operacyjne*, **Wydanie V**, Wydawnictwo Naukowe PWN *(rozdziały: urządzenia I/O, struktury systemu, współpraca CPU z hardware)*

*Dodatkowo (opcjonalnie): dokumentacja producentów chipsetów, specyfikacje UEFI Forum, materiały wykładowe uczelni.*

---

<!-- _class: lead -->

# Dziękuję za uwagę

**Pytania?**
