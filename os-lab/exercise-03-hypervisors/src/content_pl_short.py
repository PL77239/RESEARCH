TITLE_PAGE = {
    "compact": True,
    "line_spacing": 1.15,
    "course": "Systemy Operacyjne",
    "exercise": "Ćwiczenie 3",
    "title": "Wirtualizatory typu I, typu II i Server designed",
    "fields": [
        ("Imię i nazwisko", "[[Imię Nazwisko]]"),
        ("Nr albumu", "[[000000]]"),
        ("Grupa", "[[Grupa]]"),
        ("Data", "[[data]]"),
    ],
}

BODY = [
    ("h2", "1. Definicje"),
    ("p",
     "**Hypervisor** (hipernadzorca, monitor maszyn wirtualnych – VMM) to oprogramowanie, które tworzy "
     "i uruchamia maszyny wirtualne. Dzieli między nie fizyczny procesor, pamięć, dyski i sieć oraz izoluje "
     "je od siebie."),
    ("p",
     "**Typ I (bare-metal)** – hypervisor instalowany **bezpośrednio na fizycznym sprzęcie**, bez systemu "
     "operacyjnego hosta. Sam jest minimalnym systemem operacyjnym z bezpośrednim dostępem do sprzętu "
     "i korzysta z wirtualizacji wspomaganej sprzętowo (Intel VT-x / AMD-V). Przykłady: VMware ESXi, "
     "Microsoft Hyper-V, Xen, KVM."),
    ("p",
     "**Typ II (hostowany)** – hypervisor jest **aplikacją instalowaną w istniejącym systemie "
     "operacyjnym** (Windows, macOS, Linux). Jest w pełni zależny od systemu hosta, przez który uzyskuje "
     "dostęp do procesora, pamięci, dysków i urządzeń. Przykłady: Oracle VirtualBox, VMware Workstation, "
     "VMware Fusion, Parallels Desktop."),
    ("p",
     "**Server designed** – kompletne **platformy wirtualizacyjne przeznaczone dla serwerów i centrów "
     "danych**. Zwykle opierają się na hypervisorze typu I i dodają centralne zarządzanie wieloma hostami, "
     "klastry, wysoką dostępność (HA), migrację działających maszyn na żywo, współdzieloną pamięć masową, "
     "sieci wirtualne i kopie zapasowe. Ta kategoria opisuje przeznaczenie produktu (obsługę całej "
     "infrastruktury), a nie miejsce hypervisora. Przykłady: VMware vSphere (ESXi + vCenter), Hyper-V "
     "z klastrem pracy awaryjnej Windows Server, Proxmox VE, XCP-ng/XenServer, Nutanix AHV."),

    ("h2", "2. Najważniejsze różnice"),
    ("table", "Tabela 1. Typ I, typ II i Server designed.",
     ["", "Typ I", "Typ II", "Server designed"],
     [
         ["Działa na", "Bezpośrednio na sprzęcie", "Systemie operacyjnym hosta",
          "Klastrze serwerów (pod spodem typ I)"],
         ["Wydajność", "Zbliżona do natywnej", "Niższa (narzut systemu hosta)", "Zbliżona do natywnej"],
         ["Obsługa sprzętu", "Ograniczona (sprzęt certyfikowany)",
          "Szeroka (wszystko, co obsługuje system hosta)", "Ograniczona (certyfikowane serwery)"],
         ["Bezpieczeństwo", "Wysokie, mała powierzchnia ataku", "Zależy od systemu hosta",
          "Wysokie + kontrola dostępu, audyt"],
         ["Instalacja / zarządzanie", "Instalowany jak system, zarządzany zdalnie",
          "Instalowany jak program, lokalny interfejs", "Złożone; centralna konsola dla wielu hostów"],
         ["Skala", "Wiele maszyn na jednym hoście", "Kilka maszyn na komputerze",
          "Setki maszyn na wielu hostach"],
         ["Koszt", "Często płatny (są darmowe opcje)", "Najczęściej darmowy",
          "Najwyższy (poza rozwiązaniami open source)"],
     ],
     [3.0, 4.2, 4.2, 4.6]),

    ("h2", "3. Zalety i wady"),
    ("table", "Tabela 2. Zalety i wady.",
     ["Typ", "Zalety", "Wady"],
     [
         ["Typ I",
          ["Najwyższa wydajność", "Bezpieczny i stabilny (praca 24/7)", "Skaluje się do wielu maszyn"],
          ["Wymaga dedykowanej maszyny", "Ograniczona obsługa sprzętu",
           "Trudniejsza instalacja i administracja"]],
         ["Typ II",
          ["Bardzo łatwa instalacja i obsługa", "Działa na prawie każdym komputerze",
           "Zwykle darmowy; migawki, foldery współdzielone"],
          ["Wolniejszy, zwłaszcza dysk i sieć", "Awaria lub atak na system hosta dotyka też maszyn",
           "Nie nadaje się do serwerów produkcyjnych"]],
         ["Server designed",
          ["Wysoka dostępność, migracja na żywo", "Centralne zarządzanie i automatyzacja",
           "Efektywne wykorzystanie całej infrastruktury"],
          ["Drogie (produkty komercyjne)", "Wymaga kilku serwerów i współdzielonej pamięci masowej",
           "Złożone; potrzebni doświadczeni administratorzy"]],
     ],
     [3.0, 6.5, 6.5]),

    ("h2", "4. Kiedy stosować który typ"),
    ("bullets", [
        "**Typ I** – dedykowany serwer z usługami produkcyjnymi, które muszą być szybkie i bezpieczne, "
        "np. firmowa baza danych, serwer poczty lub plików albo dostawca hostingu.",
        "**Typ II** – maszyny wirtualne jako narzędzie na własnym komputerze: nauka (np. Linux na laptopie "
        "z Windows na zajęcia z SO), programowanie i testy, aplikacje Windows na komputerze Mac, stare "
        "oprogramowanie lub bezpieczne otwieranie podejrzanych plików.",
        "**Server designed** – firma uruchamiająca wiele maszyn na kilku serwerach, które nie mogą przestać "
        "działać: centra danych, chmury prywatne, wirtualne pulpity (VDI). Proxmox VE lub XCP-ng to darmowe "
        "opcje dla małych firm i domowych laboratoriów.",
    ]),
    ("p",
     "**Uwaga:** KVM i Hyper-V to przypadki graniczne. Oba włącza się w istniejącym systemie (Linux lub "
     "Windows), ale potem działają pod nim i bezpośrednio zarządzają sprzętem, dlatego zwykle klasyfikuje "
     "się je jako typ I."),

    ("h2", "Źródła"),
    ("refs", [
        "Hypervisor wirtualizacyjny typu 1 oraz typu 2 – co je różni?, magnifier.pl, 2020, "
        "https://magnifier.pl/hypervisor-typ-1-typ-2-porownanie/",
        "Bilski P., Systemy operacyjne – Ćwiczenia 3: Wirtualizator Hyper-V (materiały z zajęć).",
    ]),
]
