TITLE_PAGE = {
    "university": "[[Nazwa uczelni]]",
    "faculty": "[[Wydział / Katedra]]",
    "course": "Systemy Operacyjne",
    "exercise": "Ćwiczenie 3 – Wirtualizator Hyper-V oraz porównanie dostępnych na rynku wirtualizatorów",
    "title": "Wirtualizatory typu I i typu II",
    "subtitle": "Definicje, różnice, zalety i wady, zastosowania oraz charakterystyka wirtualizatorów "
    "typu I, typu II i Server designed",
    "fields": [
        ("Autor", "[[Imię Nazwisko]]"),
        ("Nr albumu", "[[000000]]"),
        ("Grupa", "[[Grupa]]"),
        ("Prowadzący", "mgr inż. Piotr Bilski"),
    ],
    "place_date": "[[Miejscowość]], [[data]]",
}

BODY = [
    # ------------------------------------------------------------------ 1
    ("h1", "1. Wprowadzenie"),
    ("p",
     "**Wirtualizacja** to technika oddzielająca oprogramowanie od fizycznego sprzętu, na którym jest "
     "uruchamiane. Cienka warstwa oprogramowania tworzy abstrakcję procesora, pamięci, pamięci masowej "
     "i urządzeń sieciowych. Dzięki temu na jednym fizycznym komputerze (**hoście**) może jednocześnie "
     "działać wiele odizolowanych **maszyn wirtualnych (VM)**, a każda z nich ma własny system operacyjny "
     "(**system gościa**, ang. guest OS)."),
    ("p",
     "Elementem, który to umożliwia, jest **hypervisor**, nazywany też hipernadzorcą lub **monitorem "
     "maszyn wirtualnych (VMM – Virtual Machine Monitor)**. Jego zadania to: przydzielanie maszynom "
     "wirtualnym czasu procesora, pamięci i urządzeń wejścia-wyjścia, izolowanie maszyn od siebie "
     "nawzajem i od hosta, przechwytywanie instrukcji uprzywilejowanych wykonywanych przez systemy "
     "gości oraz kontrolowanie komunikacji między maszynami wirtualnymi a fizycznym sprzętem."),
    ("p",
     "Podział hypervisorów na **typ I** i **typ II** wprowadził Robert P. Goldberg w 1973 roku [3] "
     "i nadal jest to podstawowy sposób ich opisu. Kryterium jest proste: **gdzie hypervisor znajduje "
     "się względem sprzętu i systemu operacyjnego**. Hypervisor typu I działa bezpośrednio na sprzęcie, "
     "a hypervisor typu II działa jako aplikacja w istniejącym systemie operacyjnym (rysunek 1)."),
    ("p",
     "Współczesne procesory x86 mają sprzętowe wsparcie wirtualizacji: **Intel VT-x** i **AMD-V** "
     "(wirtualizacja procesora), **EPT/NPT** (inaczej SLAT – sprzętowe tłumaczenie adresów pamięci gościa) "
     "oraz **VT-d/AMD-Vi** (IOMMU, służące do bezpośredniego przypisywania urządzeń fizycznych maszynie "
     "wirtualnej). Większość obecnych hypervisorów typu I wymaga tych rozszerzeń, a hypervisory typu II "
     "również z nich korzystają. Mocno zmniejsza to różnicę wydajności, jaka istniała, gdy wirtualizacja "
     "opierała się wyłącznie na technikach programowych, takich jak translacja binarna [1][2]."),
    ("figure", "diagram_{lang}.png",
     "Rysunek 1. Architektura hypervisora typu I (po lewej) i typu II (po prawej). Opracowanie własne na "
     "podstawie [1]."),

    # ------------------------------------------------------------------ 2
    ("h1", "2. Wirtualizator typu I (bare-metal, natywny)"),
    ("h2", "2.1. Definicja"),
    ("p",
     "**Hypervisor typu I** instaluje się **bezpośrednio na fizycznym sprzęcie** (\"na gołym metalu\", "
     "ang. bare metal), a nie w systemie operacyjnym. Sam jest wyspecjalizowanym, minimalnym systemem "
     "operacyjnym, którego jedynym zadaniem jest uruchamianie maszyn wirtualnych. Ma **bezpośredni dostęp "
     "do zasobów sprzętowych**, bez pośrednictwa systemu operacyjnego ogólnego przeznaczenia i jego "
     "sterowników. Wykorzystuje pełną wirtualizację z akceleracją sprzętową, której potrzebuje do "
     "poprawnego działania [1]."),
    ("p",
     "W niektórych rozwiązaniach obok hypervisora działa uprzywilejowana maszyna zarządzająca, która "
     "dostarcza sterowniki urządzeń i narzędzia administracyjne: **dom0** w Xen oraz **partycja główna** "
     "(root/parent partition) w Microsoft Hyper-V. Nawet wtedy hypervisor działa pod wszystkimi systemami "
     "operacyjnymi, również pod systemem zarządzającym, więc jest to nadal architektura typu I."),
    ("h2", "2.2. Możliwości"),
    ("bullets", [
        "Wydajność zbliżona do natywnej, ponieważ między maszynami wirtualnymi a sprzętem nie ma systemu "
        "hosta.",
        "Uruchamianie dziesiątek, a nawet setek maszyn wirtualnych na jednym serwerze (konsolidacja serwerów).",
        "Zaawansowane zarządzanie pamięcią: nadsubskrypcja (overcommitment), współdzielenie stron, "
        "ballooning i kompresja.",
        "Migracja na żywo (live migration) działającej maszyny wirtualnej między hostami fizycznymi bez jej "
        "zatrzymywania (np. vMotion, Hyper-V Live Migration).",
        "Wysoka dostępność (HA) i klastry: po awarii maszyny wirtualne automatycznie uruchamiają się na "
        "innym hoście.",
        "Bezpośrednie przypisywanie sprzętu: PCI passthrough, karty sieciowe SR-IOV, współdzielenie lub "
        "przekazywanie GPU (np. dla VDI lub zadań AI).",
        "Zdalne, scentralizowane zarządzanie wieloma hostami przez konsole webowe i API.",
        "Silna izolacja i mała powierzchnia ataku, ponieważ kod hypervisora jest niewielki.",
    ]),
    ("h2", "2.3. Ograniczenia"),
    ("bullets", [
        "**Ograniczona obsługa sprzętu.** Nie ma systemu ogólnego przeznaczenia, który dostarczałby "
        "sterowniki, więc hypervisor działa tylko na certyfikowanym sprzęcie z jego listy zgodności "
        "(HCL). Dotyczy to zwłaszcza VMware ESXi [1].",
        "**Wymaga dedykowanej maszyny.** Hypervisor zastępuje system operacyjny, więc komputer nie może "
        "jednocześnie służyć jako zwykła stacja robocza.",
        "**Trudniejsza instalacja i administracja.** Wymagana jest wiedza z zakresu sieci, pamięci masowej "
        "i narzędzi zdalnego zarządzania.",
        "**Koszt licencji.** Komercyjne edycje dla przedsiębiorstw (VMware vSphere, Windows Server "
        "Datacenter) mogą być drogie, choć istnieją darmowe rozwiązania open source (KVM, Xen, Proxmox VE, "
        "XCP-ng).",
        "**Zwykle zarządzany z innego komputera.** Do codziennej administracji potrzebny jest osobny "
        "komputer z przeglądarką lub konsolą.",
    ]),
    ("h2", "2.4. Zastosowania"),
    ("bullets", [
        "Centra danych i serwerownie: konsolidacja wielu fizycznych serwerów na kilku hostach.",
        "Chmury publiczne i prywatne (IaaS): AWS (hypervisor Nitro oparty na KVM), Google Cloud (KVM), "
        "Microsoft Azure (Hyper-V) oraz chmury oparte na OpenStack.",
        "Produkcyjne systemy firmowe: kontrolery domeny, bazy danych, poczta, systemy ERP i serwery plików.",
        "Infrastruktura wirtualnych pulpitów (VDI): wiele pulpitów użytkowników udostępnianych z serwerów "
        "centralnych.",
        "Dostawcy hostingu i VPS, telekomunikacja (NFV – wirtualizacja funkcji sieciowych) oraz edge "
        "computing.",
        "Odtwarzanie po awarii (DR): replikacja maszyn wirtualnych do drugiej lokalizacji (np. Hyper-V "
        "Replica, vSphere Replication).",
    ]),
    ("procon", "Tabela 1. Zalety i wady hypervisorów typu I.",
     "Zalety", [
         "Najwyższa wydajność i efektywne wykorzystanie zasobów",
         "Lepsze bezpieczeństwo: mała powierzchnia ataku, brak podatności dziedziczonych po systemie "
         "desktopowym",
         "Stabilność i niezawodność – projektowany do pracy 24/7",
         "Skalowalność: wiele maszyn wirtualnych na hoście, klastry wielu hostów",
         "Funkcje dla przedsiębiorstw: migracja na żywo, HA, równoważenie obciążenia, replikacja",
         "Scentralizowane zdalne zarządzanie i automatyzacja (API, PowerShell, Ansible)",
     ],
     "Wady", [
         "Ograniczony zakres obsługiwanego sprzętu (HCL)",
         "Wymaga dedykowanej maszyny fizycznej",
         "Bardziej złożona instalacja, konfiguracja i administracja",
         "Licencje komercyjne mogą być drogie",
         "Wymaga osobnej stacji lub konsoli do zarządzania",
         "Błąd konfiguracji lub awaria hosta dotyka wszystkich jego maszyn wirtualnych",
     ]),

    # ------------------------------------------------------------------ 3
    ("h1", "3. Wirtualizator typu II (hostowany)"),
    ("h2", "3.1. Definicja"),
    ("p",
     "**Hypervisor typu II** to **aplikacja instalowana w istniejącym systemie operacyjnym** (systemie "
     "hosta), tak jak każdy inny program. Jest **w pełni zależny od systemu hosta**, z którego korzysta do "
     "planowania pracy procesora, zarządzania pamięcią RAM, odczytów i zapisów na dysku oraz dostępu do "
     "urządzeń. Ponieważ sprzętem zarządza system hosta, hypervisor może działać na prawie każdym "
     "komputerze obsługiwanym przez ten system. Ceną jest niższa wydajność, ponieważ każda operacja gościa "
     "przechodzi przez dodatkową warstwę [1]."),
    ("p",
     "Hypervisory typu II również korzystają z akceleracji sprzętowej (VT-x/AMD-V), gdy jest dostępna. "
     "Niektóre z nich, gdy sprzęt nie ma potrzebnych funkcji, mogą użyć technik programowych, takich jak "
     "translacja binarna lub pełna emulacja (QEMU TCG) [1]."),
    ("h2", "3.2. Możliwości"),
    ("bullets", [
        "Szybka instalacja – kilka minut, jak w przypadku każdej innej aplikacji; nie jest potrzebna "
        "dedykowana maszyna.",
        "Działa na zwykłych laptopach i komputerach stacjonarnych z systemem Windows, macOS lub Linux, "
        "dzięki czemu obsługuje szeroki zakres sprzętu.",
        "Systemy hosta i gościa działają jednocześnie, obok siebie, na jednym ekranie.",
        "Funkcje integracji z pulpitem: foldery współdzielone, wspólny schowek, przeciągnij i upuść, "
        "przekierowanie urządzeń USB, tryb zintegrowany (okna aplikacji gościa na pulpicie hosta) oraz "
        "akceleracja grafiki 3D.",
        "Migawki (snapshoty) i klony, dzięki którym łatwo wrócić do znanego stanu – idealne do "
        "eksperymentów.",
        "Elastyczne sieci wirtualne: NAT, mostkowana (bridged), tylko z hostem (host-only) i sieć "
        "wewnętrzna.",
        "Niektóre produkty (QEMU) potrafią emulować inną architekturę procesora, np. ARM lub RISC-V na "
        "komputerze x86.",
    ]),
    ("h2", "3.3. Ograniczenia"),
    ("bullets", [
        "**Niższa wydajność**, szczególnie operacji dyskowych i sieciowych, ponieważ żądania przechodzą "
        "przez system hosta i jego sterowniki. Maszyny wirtualne konkurują też z aplikacjami hosta "
        "o procesor i pamięć RAM.",
        "**Bezpieczeństwo zależy od systemu hosta.** Przejęcie hosta oznacza przejęcie wszystkich maszyn "
        "wirtualnych. Powierzchnia ataku jest większa (system hosta plus aplikacja hypervisora). Podatności "
        "w emulowanych urządzeniach, takie jak VENOM (CVE-2015-3456) w wirtualnym kontrolerze stacji "
        "dyskietek w QEMU, mogą umożliwić \"ucieczkę z maszyny wirtualnej\" (VM escape).",
        "**Stabilność zależy od hosta.** Aktualizacje, ponowne uruchomienia lub awarie systemu hosta "
        "zatrzymują wszystkie maszyny wirtualne.",
        "**Ograniczona skalowalność.** Zwykle kilka maszyn wirtualnych na hoście, bez klastrów, HA "
        "i migracji na żywo między hostami.",
        "**Konflikty między hypervisorami.** W systemie Windows włączenie Hyper-V (z którego korzystają też "
        "WSL 2 i zabezpieczenia oparte na wirtualizacji) powoduje, że VirtualBox i VMware Workstation muszą "
        "działać przez interfejs Windows Hypervisor Platform, co może obniżyć ich wydajność.",
        "**Nie nadaje się do serwerów produkcyjnych**, które muszą działać 24/7.",
    ]),
    ("h2", "3.4. Zastosowania"),
    ("bullets", [
        "Edukacja: nauka systemów operacyjnych (np. instalacja Linuksa na laptopie z Windows na potrzeby "
        "zajęć z SO) i budowanie sieci laboratoryjnych.",
        "Tworzenie i testowanie oprogramowania w kilku systemach operacyjnych lub ich wersjach oraz "
        "odtwarzanie błędów.",
        "Uruchamianie aplikacji wymagających innego systemu (np. programów dla Windows na komputerze Mac).",
        "Uruchamianie starszego oprogramowania, które nie działa w nowym systemie (np. starej aplikacji dla "
        "Windows XP).",
        "Bezpieczeństwo: bezpieczne otwieranie podejrzanych plików, analiza złośliwego oprogramowania "
        "w odizolowanej maszynie z migawkami oraz dystrybucje do testów penetracyjnych (Kali Linux).",
        "Prezentacje, szkolenia, weryfikacja koncepcji (proof of concept) i szybkie testowanie nowych "
        "systemów.",
    ]),
    ("procon", "Tabela 2. Zalety i wady hypervisorów typu II.",
     "Zalety", [
         "Bardzo łatwa instalacja i obsługa (interfejs graficzny)",
         "Działa na prawie każdym komputerze – szeroka zgodność sprzętowa",
         "Nie jest potrzebna dedykowana maszyna; host i goście działają jednocześnie",
         "Najczęściej darmowy (VirtualBox, VMware Workstation Pro/Fusion Pro, QEMU)",
         "Wygodna integracja z pulpitem (schowek, foldery współdzielone, USB)",
         "Migawki sprawiają, że eksperymenty są bezpieczne i powtarzalne",
     ],
     "Wady", [
         "Niższa wydajność, zwłaszcza operacji wejścia-wyjścia; narzut systemu hosta",
         "Bezpieczeństwo i stabilność zależą od systemu hosta",
         "Maszyny wirtualne konkurują o zasoby z aplikacjami hosta",
         "Słaba skalowalność; brak HA, klastrów i migracji na żywo",
         "Możliwe konflikty z innymi hypervisorami (np. Hyper-V w systemie Windows)",
         "Nie nadaje się do produkcyjnych zadań serwerowych",
     ]),

    # ------------------------------------------------------------------ 4
    ("h1", "4. Różnice między wirtualizatorami typu I i typu II"),
    ("p",
     "Tabela 3 podsumowuje najważniejsze różnice. Podstawowa różnica to miejsce hypervisora w stosie "
     "oprogramowania: **hypervisor typu I sam zarządza sprzętem, a hypervisor typu II prosi o dostęp "
     "do sprzętu system operacyjny hosta**. Z tego wynika większość pozostałych różnic."),
    ("table", "Tabela 3. Porównanie wirtualizatorów typu I i typu II.",
     ["Kryterium", "Typ I (bare-metal)", "Typ II (hostowany)"],
     [
         ["Miejsce w stosie", "Bezpośrednio na sprzęcie; jest systemem operacyjnym dla maszyn wirtualnych",
          "Aplikacja lub proces działający w systemie hosta"],
         ["Dostęp do sprzętu", "Bezpośredni (własne sterowniki lub partycja uprzywilejowana, np. dom0 lub "
          "partycja główna)", "Pośredni – przez sterowniki systemu hosta"],
         ["Wydajność", "Zbliżona do natywnej, mały narzut",
          "Niższa, zwłaszcza operacji wejścia-wyjścia; dodatkowa warstwa i konkurencja o zasoby"],
         ["Zgodność sprzętowa", "Ograniczona – certyfikowany sprzęt (HCL)",
          "Szeroka – wszystko, co obsługuje system hosta"],
         ["Bezpieczeństwo / izolacja", "Wysokie; mała powierzchnia ataku",
          "Zależy od systemu hosta; większa powierzchnia ataku"],
         ["Stabilność", "Niezależny od systemu desktopowego; projektowany do pracy 24/7",
          "Aktualizacja lub awaria hosta zatrzymuje maszyny wirtualne"],
         ["Instalacja", "Instalowany jak system operacyjny na dedykowanej maszynie",
          "Instalowany jak zwykły program"],
         ["Zarządzanie", "Zdalne, scentralizowane (konsola webowa, vCenter, SCVMM, API)",
          "Lokalny interfejs graficzny na tym samym komputerze"],
         ["Skalowalność", "Od kilkudziesięciu do kilkuset maszyn wirtualnych na hoście; klastry",
          "Kilka maszyn wirtualnych; jeden komputer"],
         ["Typowe funkcje", "Migracja na żywo, HA, klastry, replikacja, passthrough, SR-IOV",
          "Migawki, foldery współdzielone, schowek, USB, tryb zintegrowany"],
         ["Koszt", "Często płatna licencja lub subskrypcja (istnieją darmowe opcje)", "Najczęściej darmowy"],
         ["Typowi użytkownicy", "Centra danych, dostawcy chmury, firmy",
          "Studenci, programiści, testerzy, użytkownicy domowi"],
         ["Przykłady", "VMware ESXi, Microsoft Hyper-V, Xen, KVM*",
          "Oracle VirtualBox, VMware Workstation i Fusion, Parallels Desktop, QEMU"],
     ],
     [3.6, 6.2, 6.2]),
    ("p",
     "* **Przypadki graniczne.** **KVM** (Kernel-based Virtual Machine) to moduł jądra Linux. Na pierwszy "
     "rzut oka wygląda jak hypervisor typu II, ponieważ jest ładowany w zwykłym systemie Linux. Zamienia "
     "jednak samo jądro Linuksa w hypervisor, dlatego wiele źródeł (np. Red Hat) klasyfikuje go jako typ I. "
     "Inne źródła, w tym artykuł omawiany na zajęciach, opisują go jako typ II, ponieważ wirtualizację "
     "zapewnia pełny system Linux, a nie tylko jądro [1][6]. **Microsoft Hyper-V** to przypadek odwrotny. "
     "Instaluje się go jako rolę Windows Server lub funkcję systemu Windows, więc wygląda jak aplikacja. "
     "Jednak jego włączenie umieszcza hypervisor pod systemem Windows, który staje się wtedy partycją "
     "główną działającą na hypervisorze. Hyper-V jest zatem hypervisorem typu I [1][5]."),

    # ------------------------------------------------------------------ 5
    ("h1", "5. Kiedy stosować który typ"),
    ("p",
     "Prosta zasada brzmi: **typ I stosujemy, gdy maszyny wirtualne są produktem** (usługi produkcyjne, "
     "które muszą być szybkie, bezpieczne i stale dostępne), a **typ II, gdy maszyny wirtualne są "
     "narzędziem** (do nauki, programowania, testów lub okazjonalnego uruchamiania innego systemu na "
     "własnym komputerze). Tabela 4 przedstawia typowe scenariusze."),
    ("table", "Tabela 4. Zalecany typ wirtualizatora w typowych scenariuszach.",
     ["Scenariusz", "Zalecenie", "Uzasadnienie"],
     [
         ["Firmowe serwery produkcyjne (AD, bazy danych, poczta, ERP)", "Typ I / platforma Server designed",
          "Wydajność, niezawodność 24/7, HA, kopie zapasowe i centralne zarządzanie"],
         ["Dostawca chmury, hosting, VPS", "Typ I (KVM, Xen, Hyper-V) w platformie chmurowej",
          "Bardzo duże zagęszczenie maszyn wirtualnych, wielu klientów, automatyzacja przez API"],
         ["Wirtualne pulpity (VDI) dla pracowników", "Typ I / platforma Server designed",
          "Wiele pulpitów z serwerów centralnych; współdzielenie GPU"],
         ["Konsolidacja starych serwerów fizycznych", "Typ I",
          "Mniej maszyn, niższe koszty zasilania i chłodzenia, łatwiejsze zarządzanie"],
         ["Mały oddział lub lokalizacja brzegowa (2–3 serwery)", "Typ I (Hyper-V, Proxmox VE, małe HCI)",
          "Niezawodność przy niewielkiej ilości sprzętu"],
         ["Student uruchamiający Linuksa na laptopie z Windows na zajęcia z SO",
          "Typ II (VirtualBox, VMware Workstation)",
          "Darmowy, szybka instalacja, host pozostaje w użyciu; migawki pozwalają bezpiecznie "
          "eksperymentować"],
         ["Programista testujący aplikację w wielu systemach", "Typ II",
          "Szybkie tworzenie, klonowanie i przywracanie testowych maszyn wirtualnych"],
         ["Użytkownik komputera Mac potrzebujący aplikacji Windows", "Typ II (Parallels Desktop, VMware Fusion)",
          "Dobra integracja z pulpitem macOS"],
         ["Analiza podejrzanych plików lub złośliwego oprogramowania", "Typ II z migawkami i odizolowaną "
          "siecią (dedykowany host typu I w profesjonalnym laboratorium)",
          "Łatwe przywrócenie stanu; zagrożenie trzymane z dala od hosta"],
         ["Uruchamianie starszego oprogramowania", "Typ II",
          "Stary system w maszynie wirtualnej bez poświęcania całego komputera"],
         ["Emulacja innej architektury procesora (ARM, RISC-V)", "QEMU (emulator typu II)",
          "Tylko emulator może wykonać kod dla innej listy rozkazów"],
         ["Domowe laboratorium do nauki administracji serwerami",
          "Server designed (Proxmox VE, XCP-ng) na zapasowym komputerze",
          "Nauka klastrów, HA i pamięci masowej jak w prawdziwej firmie, bez kosztów"],
     ],
     [5.2, 4.8, 6.0]),

    # ------------------------------------------------------------------ 6
    ("h1", "6. Wirtualizatory typu Server designed"),
    ("h2", "6.1. Definicja"),
    ("p",
     "**Wirtualizatory typu Server designed** (serwerowe lub korporacyjne platformy wirtualizacyjne) to "
     "kompletne rozwiązania wirtualizacyjne zaprojektowane od początku do uruchamiania **zadań "
     "produkcyjnych na serwerach i w centrach danych**, zwykle na **wielu hostach fizycznych zarządzanych "
     "jako jedna pula zasobów**. Oprócz hypervisora zapewniają cały ekosystem: centralne zarządzanie, "
     "klastry, wysoką dostępność, migrację na żywo, współdzieloną lub programowo definiowaną pamięć masową "
     "i sieć, kopie zapasowe, monitorowanie, role i uprawnienia użytkowników oraz API do automatyzacji."),
    ("p",
     "Ta kategoria **nie jest trzecim miejscem w stosie** obok typu I i typu II. Opisuje **przeznaczenie "
     "i zakres** produktu, a nie miejsce hypervisora. W praktyce prawie każda platforma Server designed "
     "jest zbudowana na **hypervisorze typu I** (ESXi, Hyper-V, Xen lub KVM). Różnica polega na tym, że sam "
     "hypervisor typu I wirtualizuje pojedynczą maszynę, a platforma Server designed zarządza całą "
     "infrastrukturą. Przykładowo ESXi to hypervisor, a vSphere (ESXi + vCenter) to platforma serwerowa."),
    ("h2", "6.2. Cechy charakterystyczne"),
    ("bullets", [
        "**Centralne zarządzanie** wieloma hostami i maszynami wirtualnymi z jednej konsoli (vCenter, "
        "System Center VMM / Windows Admin Center, interfejs webowy Proxmox, Xen Orchestra, Nutanix Prism).",
        "**Klastry i wysoka dostępność (HA)**: gdy host ulegnie awarii, jego maszyny wirtualne automatycznie "
        "uruchamiają się na pozostałych hostach.",
        "**Migracja na żywo** działających maszyn wirtualnych i ich dysków między hostami, np. na czas "
        "konserwacji sprzętu bez przestojów.",
        "**Automatyczne równoważenie obciążenia** (np. VMware DRS) oraz pule zasobów z limitami.",
        "**Programowo definiowana pamięć masowa i hiperkonwergencja (HCI)**: vSAN, Storage Spaces Direct, "
        "Ceph lub ZFS – lokalne dyski wielu serwerów połączone we wspólną, nadmiarową pamięć masową.",
        "**Programowo definiowane sieci (SDN)**: przełączniki wirtualne, VLAN i VXLAN, mikrosegmentacja, "
        "zapory sieciowe.",
        "Integracja **kopii zapasowych, replikacji i odtwarzania po awarii**; szablony i szybkie tworzenie "
        "maszyn.",
        "**Bezpieczeństwo i zgodność z przepisami**: kontrola dostępu oparta na rolach (RBAC), dzienniki "
        "audytu, szyfrowane lub chronione (shielded) maszyny wirtualne, emulacja TPM i Secure Boot.",
        "**Automatyzacja**: REST API, PowerShell/PowerCLI, Terraform, Ansible; często wsparcie producenta "
        "i certyfikaty.",
    ]),
    ("procon", "Tabela 5. Zalety i wady wirtualizatorów typu Server designed.",
     "Zalety", [
         "Najwyższa dostępność – HA i migracja na żywo ograniczają przestoje do minimum",
         "Efektywne wykorzystanie całej infrastruktury (konsolidacja, równoważenie obciążenia)",
         "Centralne zarządzanie i automatyzacja setek maszyn wirtualnych",
         "Wbudowana lub zintegrowana pamięć masowa, sieci, kopie zapasowe i DR",
         "Wsparcie producenta, certyfikaty i duży ekosystem",
         "Skalowanie od kilku serwerów do całego centrum danych",
     ],
     "Wady", [
         "Najwyższy koszt produktów komercyjnych (licencje lub subskrypcje, często za rdzeń procesora)",
         "Pełna funkcjonalność wymaga kilku serwerów, współdzielonej pamięci masowej i szybkiej sieci",
         "Duża złożoność; wymaga wykwalifikowanych administratorów",
         "Ryzyko uzależnienia od dostawcy (np. zmiany licencji VMware po 2023 roku)",
         "Zbyt rozbudowane dla jednego komputera lub użytkownika domowego (poza platformami open source "
         "używanymi w domowych laboratoriach)",
     ]),
    ("h2", "6.3. Kiedy stosować"),
    ("p",
     "Platformy Server designed są właściwym wyborem zawsze, gdy firma uruchamia **usługi produkcyjne**, "
     "które muszą być stale dostępne i są rozłożone na **więcej niż jeden serwer fizyczny**. Przykłady to "
     "firmowe centra danych, chmury prywatne, hosting, VDI oraz oddziały wymagające wysokiej dostępności. "
     "Mniejsze organizacje i domowe laboratoria coraz częściej korzystają z platform open source, takich "
     "jak Proxmox VE lub XCP-ng, które oferują klastry i HA bez opłat licencyjnych."),

    # ------------------------------------------------------------------ 7
    ("h1", "7. Przegląd wirtualizatorów dostępnych na rynku"),
    ("p",
     "Poniżej opisano najpopularniejsze produkty, podzielone zgodnie z treścią ćwiczenia na trzy grupy. "
     "Grupa A obejmuje same hypervisory typu I, grupa B produkty typu II (hostowane), a grupa C kompletne "
     "platformy Server designed, z których większość jest zbudowana na hypervisorach z grupy A."),

    ("h2", "7.1. Grupa A – wirtualizatory typu I"),
    ("h3", "VMware ESXi (Broadcom)"),
    ("p",
     "ESXi to dojrzały, szeroko stosowany hypervisor bare-metal z własnym małym jądrem (VMkernel). "
     "Instaluje się go na serwerze i zarządza nim przez webowy Host Client lub centralnie przez vCenter. "
     "Obsługuje bardzo duże maszyny wirtualne, nadsubskrypcję pamięci, PCI passthrough i vGPU. "
     "**Możliwości:** bardzo wysoka wydajność i stabilność oraz ogromny ekosystem narzędzi do kopii "
     "zapasowych i monitorowania. **Ograniczenia:** rygorystyczna lista zgodności sprzętowej. Po przejęciu "
     "VMware przez Broadcom w 2023 roku licencjonowanie zmieniono na pakiety subskrypcyjne, co dla wielu "
     "klientów znacznie podniosło koszty. **Zastosowanie:** korporacyjne centra danych, jako podstawa "
     "platformy vSphere (grupa C)."),
    ("h3", "Microsoft Hyper-V"),
    ("p",
     "Hyper-V to hypervisor typu I firmy Microsoft, dostępny jako rola w Windows Server oraz jako opcjonalna "
     "funkcja systemów Windows 10/11 Pro, Enterprise i Education. Wymaga 64-bitowego procesora z obsługą "
     "SLAT i włączoną wirtualizacją sprzętową. Windows działa w partycji głównej, a maszyny wirtualne "
     "w partycjach podrzędnych. **Możliwości:** maszyny generacji 1 i 2 (UEFI, Secure Boot, wirtualny TPM), "
     "punkty kontrolne (checkpoints), Live Migration, Hyper-V Replica, wirtualizacja zagnieżdżona, Discrete "
     "Device Assignment i partycjonowanie GPU. Jest też podstawą Microsoft Azure, WSL 2, Windows Sandbox "
     "i zabezpieczeń opartych na wirtualizacji. **Ograniczenia:** zarządzanie jest zorientowane na Windows "
     "(Menedżer funkcji Hyper-V, PowerShell, Windows Admin Center, SCVMM), darmowy samodzielny Hyper-V Server "
     "nie był rozwijany po wersji 2019, a edycja Windows Home go nie zawiera. **Zastosowanie:** firmy "
     "oparte na Windows, laboratoria i stacje robocze programistów. Jest głównym tematem zajęć "
     "laboratoryjnych tego kursu."),
    ("h3", "Xen Project (Linux Foundation)"),
    ("p",
     "Xen to hypervisor open source o architekturze mikrojądra, powstały na Uniwersytecie Cambridge "
     "(pierwsze wydanie w 2003 roku). Sam hypervisor jest bardzo mały. Uprzywilejowana domena **dom0** "
     "(zwykle Linux) zapewnia sterowniki i zarządzanie, a goście działają jako domeny **domU**. Xen był "
     "pionierem **parawirtualizacji (PV)**, obsługuje też gości HVM i PVH. **Możliwości:** silna izolacja "
     "i mała zaufana baza kodu; jest używany także w systemach wbudowanych i motoryzacyjnych. "
     "**Ograniczenia:** konfiguracja bez platformy zarządzającej jest wymagająca. **Zastosowanie:** przez "
     "wiele lat AWS EC2, a także XenServer, XCP-ng i Qubes OS (system desktopowy nastawiony na "
     "bezpieczeństwo)."),
    ("h3", "KVM – Kernel-based Virtual Machine"),
    ("p",
     "KVM jest częścią jądra Linux od wersji 2.6.20 (2007). Załadowanie modułu kvm zamienia Linuksa "
     "w hypervisor: każda maszyna wirtualna jest zwykłym procesem Linuksa, którego pracę planuje jądro. "
     "**QEMU** emuluje urządzenia, sterowniki **virtio** zapewniają szybkie parawirtualizowane operacje "
     "wejścia-wyjścia, a **libvirt** / virt-manager / Cockpit służą do zarządzania. **Możliwości:** open "
     "source (GPL), doskonała wydajność, migracja na żywo oraz korzystanie ze wszystkich funkcji Linuksa "
     "(cgroups, SELinux/sVirt, systemy plików). **Ograniczenia:** sam w sobie nie ma centralnego "
     "graficznego zarządzania wieloma hostami i wymaga znajomości Linuksa. **Zastosowanie:** najczęściej "
     "używany hypervisor w chmurach publicznych (Google Cloud, AWS Nitro, OpenStack). Jest też podstawą "
     "Proxmox VE, Nutanix AHV i OpenShift Virtualization."),
    ("h3", "IBM z/VM i PowerVM"),
    ("p",
     "To hypervisory dla komputerów mainframe IBM (IBM Z) i serwerów IBM Power. z/VM wywodzi się z systemów "
     "CP-67 i VM/370 (lata 60. i 70.), pierwszych komercyjnych systemów maszyn wirtualnych, na których "
     "pierwotnie oparto teorię typów I i II. **Możliwości:** wyjątkowa niezawodność i tysiące gości "
     "z Linuksem na jednej maszynie. **Ograniczenia:** działają tylko na sprzęcie IBM i są bardzo drogie. "
     "**Zastosowanie:** banki, ubezpieczyciele i duże przedsiębiorstwa."),

    ("h2", "7.2. Grupa B – wirtualizatory typu II"),
    ("h3", "Oracle VirtualBox"),
    ("p",
     "VirtualBox to darmowy hypervisor hostowany open source (GPLv2) dla hostów z systemem Windows, Linux "
     "i macOS (od wersji 7.1 także z procesorami Apple Silicon). **Możliwości:** obsługuje wiele systemów "
     "gości, migawki, klonowanie, foldery współdzielone, sieci NAT, mostkowane i wewnętrzne, dodatki Guest "
     "Additions do integracji z pulpitem oraz narzędzie wiersza poleceń (VBoxManage). **Ograniczenia:** "
     "niższa wydajność 3D i operacji wejścia-wyjścia niż w produktach komercyjnych, a pakiet rozszerzeń "
     "(Extension Pack: USB 2/3 passthrough, szyfrowanie dysków itd.) jest licencjonowany tylko do użytku "
     "osobistego i edukacyjnego. **Zastosowanie:** najpopularniejszy wybór studentów, w edukacji, wśród "
     "użytkowników domowych i do szybkich testów."),
    ("h3", "VMware Workstation Pro"),
    ("p",
     "Workstation Pro to profesjonalny hypervisor typu II dla systemów Windows i Linux. Od listopada 2024 "
     "roku jest darmowy do użytku osobistego, edukacyjnego i komercyjnego. **Możliwości:** bardzo dobra "
     "wydajność i obsługa 3D, drzewa migawek, klony połączone (linked clones), edytor sieci wirtualnych, "
     "wirtualny TPM i szyfrowane maszyny wirtualne oraz możliwość łączenia się z ESXi/vSphere i przenoszenia "
     "na nie maszyn. **Ograniczenia:** oprogramowanie zamknięte, działa tylko na hostach x86. "
     "**Zastosowanie:** programiści, trenerzy IT i administratorzy przygotowujący maszyny wirtualne dla "
     "vSphere."),
    ("h3", "VMware Fusion Pro"),
    ("p",
     "Fusion Pro to wersja Workstation dla macOS, również darmowa od listopada 2024 roku. Na komputerach "
     "Mac z procesorami Apple Silicon uruchamia gości ARM (Windows 11 on Arm, Linux ARM). **Możliwości:** "
     "tryb Unity, który wyświetla okna aplikacji gościa bezpośrednio na pulpicie macOS, oraz dobra "
     "integracja z ekosystemem VMware. **Ograniczenia:** na Apple Silicon nie uruchamia wydajnie systemów "
     "x86. **Zastosowanie:** użytkownicy komputerów Mac potrzebujący systemu Windows lub Linux."),
    ("h3", "Parallels Desktop"),
    ("p",
     "Parallels Desktop to komercyjny hypervisor dla macOS. Korzysta z Apple Hypervisor.framework, "
     "a Microsoft oficjalnie zatwierdził go do uruchamiania Windows 11 on Arm na komputerach Apple z serii M. "
     "**Możliwości:** bardzo dobra wydajność i grafika, tryb Coherence (aplikacje Windows wyglądają jak "
     "natywne aplikacje Mac) oraz instalacja gości Windows, Linux i macOS jednym kliknięciem. "
     "**Ograniczenia:** płatna subskrypcja, działa tylko w macOS. **Zastosowanie:** użytkownicy komputerów "
     "Mac korzystający z oprogramowania dla Windows (biurowego, inżynierskiego lub gier)."),
    ("h3", "QEMU (oraz nakładki, np. UTM)"),
    ("p",
     "QEMU to emulator i wirtualizator open source stworzony przez Fabrice'a Bellarda w 2003 roku. Bez "
     "akceleracji działa jako czysty **emulator** typu II, który korzysta z dynamicznej translacji binarnej "
     "(TCG), dzięki czemu potrafi wykonywać kod dla **innej architektury procesora** (ARM, RISC-V, PowerPC, "
     "MIPS) na komputerze x86. Z akceleracją (KVM w Linuksie, HVF w macOS, WHPX w Windows) uruchamia gości "
     "z prędkością zbliżoną do natywnej. **Ograniczenia:** czysta emulacja jest wolna, a wiersz poleceń jest "
     "złożony (pomagają nakładki, takie jak virt-manager lub UTM w macOS/iOS). **Zastosowanie:** tworzenie "
     "systemów wbudowanych i jąder systemów operacyjnych, testowanie innych architektur, potoki CI oraz "
     "rola komponentu emulującego urządzenia w KVM."),

    ("h2", "7.3. Grupa C – wirtualizatory typu Server designed"),
    ("h3", "VMware vSphere / VMware Cloud Foundation (Broadcom)"),
    ("p",
     "vSphere składa się z hostów ESXi oraz **vCenter Server**, czyli centralnego systemu zarządzania. "
     "W VMware Cloud Foundation jest rozszerzony o vSAN (hiperkonwergentna pamięć masowa), NSX "
     "(wirtualizacja sieci) i narzędzia automatyzacji. **Możliwości:** vMotion i Storage vMotion, HA, "
     "równoważenie obciążenia DRS, Fault Tolerance (kopia maszyny wirtualnej działająca synchronicznie "
     "w trybie lockstep), przełączniki rozproszone i ogromny ekosystem. **Ograniczenia:** wysoki koszt po "
     "przejściu w 2024 roku wyłącznie na licencje subskrypcyjne oraz uzależnienie od dostawcy. "
     "**Zastosowanie:** duże przedsiębiorstwa, banki, administracja publiczna i dostawcy usług. Od dawna "
     "jest rynkowym punktem odniesienia."),
    ("h3", "Microsoft Hyper-V w Windows Server oraz Azure Local"),
    ("p",
     "Hosty Hyper-V połączone z **klastrem pracy awaryjnej (Failover Clustering)**, **Storage Spaces "
     "Direct** oraz zarządzaniem przez System Center Virtual Machine Manager lub Windows Admin Center tworzą "
     "kompletną platformę serwerową. **Azure Local** (dawniej Azure Stack HCI) to hiperkonwergentny system "
     "Microsoftu zarządzany z chmury Azure. **Możliwości:** HA w klastrze, Live Migration, Hyper-V Replica, "
     "SDN, chronione maszyny wirtualne (shielded VMs) oraz ścisła integracja z Active Directory i Azure. "
     "**Zastosowanie:** organizacje oparte na technologiach Microsoft oraz chmura hybrydowa."),
    ("h3", "Proxmox Virtual Environment (Proxmox VE)"),
    ("p",
     "Proxmox VE to platforma serwerowa open source (AGPLv3) oparta na Debianie, rozwijana przez Proxmox "
     "Server Solutions GmbH (Wiedeń). Łączy maszyny wirtualne **KVM** i kontenery **LXC**, a zarządza się "
     "nią przez interfejs webowy. **Możliwości:** klastry wielowęzłowe, HA, migracja na żywo, wbudowana "
     "pamięć masowa **Ceph** i **ZFS**, zapora sieciowa, SDN oraz integracja z Proxmox Backup Server. "
     "**Ograniczenia:** stabilne repozytorium enterprise i oficjalne wsparcie wymagają płatnej subskrypcji, "
     "a ekosystem jest mniejszy niż w przypadku VMware. **Zastosowanie:** małe i średnie firmy, szkoły "
     "i domowe laboratoria. Po 2024 roku jest popularną alternatywą dla VMware."),
    ("h3", "XenServer i XCP-ng"),
    ("p",
     "XenServer (dawniej Citrix Hypervisor, Cloud Software Group) oraz jego społecznościowy fork **XCP-ng** "
     "(Vates) to platformy serwerowe oparte na hypervisorze **Xen**. XCP-ng zarządza się za pomocą **Xen "
     "Orchestra**. **Możliwości:** pule zasobów, HA, migracja na żywo wraz z pamięcią masową, kopie "
     "zapasowe oraz silna integracja z VDI Citrix (XenServer). **Ograniczenia:** mniejsza społeczność niż "
     "w przypadku rozwiązań opartych na KVM. **Zastosowanie:** VDI (Citrix Virtual Apps and Desktops) oraz "
     "firmy szukające zamiennika vSphere typu open source."),
    ("h3", "Nutanix AHV"),
    ("p",
     "AHV to hypervisor oparty na KVM, wchodzący w skład **hiperkonwergentnej** platformy Nutanix Cloud "
     "Infrastructure i zarządzany przez **Prism**. Moc obliczeniowa i rozproszona pamięć masowa działają "
     "na tych samych węzłach. **Możliwości:** proste aktualizacje jednym kliknięciem, HA, wbudowana "
     "replikacja i DR oraz brak osobnej licencji na hypervisor. **Ograniczenia:** powiązanie ze stosem "
     "oprogramowania Nutanix i certyfikowanym sprzętem. **Zastosowanie:** firmy chcące prostej, "
     "skalowalnej chmury prywatnej. Często wybierany przy migracji z VMware."),
    ("h3", "OpenStack oraz OpenShift Virtualization (KubeVirt)"),
    ("p",
     "**OpenStack** to platforma chmurowa open source (IaaS). Jej komponent Nova zarządza hypervisorami, "
     "najczęściej KVM, na setkach lub tysiącach serwerów, zapewniając samoobsługę, obsługę wielu klientów "
     "i API. **Red Hat OpenShift Virtualization**, oparty na projekcie KubeVirt, uruchamia maszyny wirtualne "
     "obok kontenerów w Kubernetesie. Jest następcą wycofanego Red Hat Virtualization (oVirt). "
     "**Ograniczenia:** oba rozwiązania są bardzo złożone i wymagają dużych zespołów do utrzymania. "
     "**Zastosowanie:** operatorzy telekomunikacyjni, ośrodki badawcze, chmury publiczne i prywatne oraz "
     "firmy modernizujące aplikacje w kierunku kontenerów."),

    ("table", "Tabela 6. Zestawienie opisanych wirtualizatorów.",
     ["Produkt", "Grupa / typ", "Licencja", "Host / platforma", "Główne zastosowanie"],
     [
         ["VMware ESXi", "A – typ I", "Komercyjna", "Serwer x86 (bare-metal)", "Serwery korporacyjne"],
         ["Microsoft Hyper-V", "A – typ I", "Część Windows / Windows Server",
          "Bare-metal (Windows w partycji głównej)", "Serwery Windows, laboratoria, programiści"],
         ["Xen Project", "A – typ I", "Open source (GPLv2)", "Bare-metal + dom0",
          "Chmury, bezpieczeństwo, systemy wbudowane"],
         ["KVM", "A – typ I*", "Open source (GPL)", "Jądro Linux", "Chmury publiczne, podstawa wielu platform"],
         ["IBM z/VM, PowerVM", "A – typ I", "Komercyjna", "IBM Z / Power", "Mainframe, duże przedsiębiorstwa"],
         ["Oracle VirtualBox", "B – typ II", "Open source + pakiet rozszerzeń na licencji PUEL",
          "Windows, Linux, macOS", "Edukacja, użytkownicy domowi, testy"],
         ["VMware Workstation Pro", "B – typ II", "Komercyjna, darmowa", "Windows, Linux",
          "Programiści, trenerzy"],
         ["VMware Fusion Pro", "B – typ II", "Komercyjna, darmowa", "macOS", "Użytkownicy komputerów Mac"],
         ["Parallels Desktop", "B – typ II", "Płatna subskrypcja", "macOS", "Aplikacje Windows na komputerze Mac"],
         ["QEMU / UTM", "B – typ II (emulator)", "Open source", "Linux, Windows, macOS",
          "Emulacja innych architektur"],
         ["VMware vSphere / VCF", "C – Server (ESXi)", "Subskrypcja", "Klastry serwerów",
          "Korporacyjne centra danych"],
         ["Hyper-V + Failover Clustering / Azure Local", "C – Server (Hyper-V)",
          "Windows Server / subskrypcja Azure", "Klastry serwerów, HCI", "Środowiska Microsoft, chmura hybrydowa"],
         ["Proxmox VE", "C – Server (KVM + LXC)", "Open source, opcjonalna subskrypcja", "Klastry serwerów",
          "Małe i średnie firmy, szkoły, domowe laboratoria"],
         ["XenServer / XCP-ng", "C – Server (Xen)", "Komercyjna / open source", "Pule serwerów",
          "VDI, alternatywa dla vSphere"],
         ["Nutanix AHV", "C – Server (KVM, HCI)", "Komercyjna", "Węzły HCI Nutanix", "Chmura prywatna"],
         ["OpenStack, OpenShift Virtualization", "C – Server / chmura (KVM)", "Open source / komercyjna",
          "Duże klastry", "Chmury prywatne i publiczne"],
     ],
     [3.4, 2.8, 3.2, 3.3, 3.3]),

    # ------------------------------------------------------------------ 8
    ("h1", "8. Podsumowanie"),
    ("p",
     "Hypervisory typu I i typu II nie konkurują ze sobą – to narzędzia do różnych zadań. Hypervisor "
     "**typu I** działa bezpośrednio na sprzęcie i oferuje najlepszą wydajność, bezpieczeństwo "
     "i skalowalność, dlatego jest standardem w centrach danych i chmurach. Jego kosztem są ograniczona "
     "obsługa sprzętu i bardziej złożona administracja. Hypervisor **typu II** to aplikacja w zwykłym "
     "systemie operacyjnym. Jest łatwy w instalacji, najczęściej darmowy i działa na prawie każdym "
     "komputerze, dzięki czemu idealnie nadaje się do nauki, programowania i testów. Płaci się za to "
     "niższą wydajnością i zależnością od systemu hosta."),
    ("p",
     "Wirtualizatory **Server designed** to kompletne platformy zbudowane wokół hypervisora typu I. "
     "Przenoszą wirtualizację z pojedynczej maszyny na całą infrastrukturę, dodając centralne zarządzanie, "
     "klastry, wysoką dostępność, migrację na żywo oraz programowo definiowaną pamięć masową i sieć. "
     "Granice między kategoriami się zacierają: KVM i Hyper-V wyglądają jak aplikacje, ale działają jak "
     "hypervisory typu I, a produkty typu II, takie jak VMware Workstation, mogą łączyć się z platformami "
     "serwerowymi. Wybór powinien więc zależeć od tego, do czego służą maszyny wirtualne: **narzędzie na "
     "własnym komputerze (typ II)**, **usługa produkcyjna na dedykowanym serwerze (typ I)** czy **cała "
     "infrastruktura (platforma Server designed)**."),

    # ------------------------------------------------------------------ refs
    ("h1", "Bibliografia"),
    ("refs", [
        "Hypervisor wirtualizacyjny typu 1 oraz typu 2 – co je różni?, magnifier.pl, 6 września 2020, "
        "https://magnifier.pl/hypervisor-typ-1-typ-2-porownanie/",
        "Bilski P., Systemy operacyjne – Ćwiczenia 3: Wirtualizator Hyper-V (materiały z zajęć).",
        "Goldberg R. P., Architectural Principles for Virtual Computer Systems, rozprawa doktorska, Harvard "
        "University, 1973.",
        "Popek G. J., Goldberg R. P., Formal Requirements for Virtualizable Third Generation Architectures, "
        "Communications of the ACM, 17(7), 1974, s. 412–421.",
        "Microsoft Learn, Hyper-V w systemach Windows i Windows Server – dokumentacja, "
        "https://learn.microsoft.com/virtualization/",
        "Red Hat, What is KVM?, https://www.redhat.com/en/topics/virtualization/what-is-KVM",
        "Broadcom, dokumentacja VMware vSphere / ESXi, https://techdocs.broadcom.com/",
        "Xen Project, Xen Project Software Overview, https://xenproject.org/",
        "Oracle, Oracle VirtualBox User Manual, https://www.virtualbox.org/manual/",
        "Proxmox Server Solutions, Proxmox VE Administration Guide, https://pve.proxmox.com/pve-docs/",
        "QEMU Project, dokumentacja QEMU, https://www.qemu.org/docs/master/",
        "Tanenbaum A. S., Bos H., Modern Operating Systems, 4th ed., Pearson, 2015 – rozdział 7: "
        "Virtualization and the Cloud.",
        "Silberschatz A., Galvin P. B., Gagne G., Operating System Concepts, 10th ed., Wiley, 2018 – "
        "rozdział 18: Virtual Machines.",
    ]),
]
