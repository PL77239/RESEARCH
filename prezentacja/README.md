# Prezentacja OS — I/O, magistrale, boot

## Główny plik (Excel)

**[`prezentacja-os.xlsx`](prezentacja-os.xlsx)** — slajdy w arkuszu **Slajdy** (1 wiersz = 1 slajd, ~15 min), plus arkusze z tabelami i krótka instrukcja w **Info**.

Ponowne wygenerowanie Excela (po edycji skryptu):

```bash
python3 build_excel.py
```

## Wersja Marp / PDF (opcjonalnie)

Plik źródłowy: [`prezentacja-os.md`](prezentacja-os.md) (format [Marp](https://marp.app/)).

```bash
npx --yes @marp-team/marp-cli prezentacja-os.md --pdf -o prezentacja-os.pdf
npx --yes @marp-team/marp-cli prezentacja-os.md --html -o prezentacja-os.html
```
