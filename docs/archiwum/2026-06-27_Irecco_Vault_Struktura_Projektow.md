# Irecco_Vault — Struktura projektów
*Gdzie co siedzi w vaultcie i dlaczego*

---

## Zasada nadrzędna

Każdy projekt ma swój własny folder wewnątrz `00-Projekty/`.
Każdy folder projektu ma identyczną strukturę wewnętrzną — różni się tylko treścią.
Narzędzia wspólne dla kilku projektów mieszkają w `00-Projekty/_wspolne/` i są linkowane wikilinkiem.

---

## Struktura główna vaulta

```
Irecco_Vault /
│
├── 00-Projekty /                ← wszystkie projekty zawodowe
│   ├── _wspolne /               ← narzędzia i decyzje wspólne dla kilku projektów
│   ├── Irecco_Lab /             ← projekt 1 — studio / platforma
│   ├── MillWork /               ← projekt 2 — plugin SketchUp CNC
│   ├── TechHub /                ← projekt 3 — narzędzie szkoleń Aluprof
│   └── Thomos /                 ← projekt 4 — platforma zdrowotna
│
├── 01-Klienci /
├── 02-Finanse /
├── 03-Marketing /
├── 04-Rozwój /
├── 10-Dom /
├── 11-Zdrowie /
├── 12-Finanse-osobiste /
├── 20-Nauka /
├── 21-Inspiracje /
├── 22-Dziennik /
├── 90-Inbox /
├── 91-Archiwum /
├── 92-AI-Zone /
├── 93-Szablony /
├── .claude /
└── home.md
```

---

## Struktura każdego projektu (szablon)

Każdy z czterech projektów ma identyczny układ folderów:

```
00-Projekty / [Nazwa-Projektu] /
│
├── 00-dashboard.md              ← stan projektu, aktywne zadania, ostatnie decyzje
├── 01-cel-i-kontekst.md         ← czym jest projekt, dla kogo, jaki problem rozwiązuje
│
├── docs /                       ← dokumentacja projektowa (przeniesiona z Google Drive)
│   ├── architektura.md
│   ├── decyzje.md
│   ├── roadmapa.md
│   └── current-state.md
│
├── sesje /                      ← logi sesji Claude Code
│   └── session-log.md
│
├── ekosystem /                  ← narzędzia i środowisko tego projektu
│   ├── ekosystem-mapa.md        ← główny dokument ekosystemu (co zainstalowane, co potrzebne)
│   ├── stos-technologiczny.md   ← stack, wersje, zależności
│   └── konfiguracja.md         ← jak uruchomić, zmienne środowiskowe, porty
│
├── beta-i-uzytkownicy /         ← (jeśli dotyczy)
│   ├── beta-program.md
│   └── feedback.md
│
├── marketing /                  ← (jeśli dotyczy)
│   ├── pozycjonowanie.md
│   └── kanaly.md
│
└── archiwum /                   ← nieaktualne wersje, stare decyzje
```

---

## Folder `_wspolne` — narzędzia dzielone między projektami

```
00-Projekty / _wspolne /
│
├── narzedzia-dev.md             ← Node.js, Python, Git, Docker — wspólna baza
├── claude-code-workflow.md      ← jak pracować z Claude Code (wspólne zasady)
├── github-workflow.md           ← Git, commity, wersjonowanie
├── google-drive-sync.md         ← jak działa sync, co gdzie trzymamy
└── anthropic-api.md             ← klucze, modele, koszty, limity
```

Każdy projekt linkuje do tych plików wikilinkiem:
`[[_wspolne/narzedzia-dev]]` zamiast kopiować tę samą treść cztery razy.

---

## Szczegółowy plan per projekt

### Projekt 1 — Irecco_Lab

```
00-Projekty / Irecco_Lab /
│
├── 00-dashboard.md
│   Zawiera: faza projektu (sesja 1 ukończona), moduły core, następne kroki
│
├── 01-cel-i-kontekst.md
│   Zawiera: umbrella studio, open-source-first, Python modular monolith
│
├── docs /
│   ├── architektura.md          ← przeniesiony z Drive: docs/architecture.md
│   ├── decyzje.md               ← przeniesiony z Drive: docs/decisions.md
│   ├── current-state.md         ← przeniesiony z Drive: docs/current-state.md
│   ├── backend-structure.md     ← przeniesiony z Drive: docs/backend-structure.md
│   ├── product-map.md           ← przeniesiony z Drive: docs/product-map.md
│   └── core-vs-product.md      ← przeniesiony z Drive: docs/core-vs-product.md
│
├── sesje /
│   └── session-log.md           ← historia sesji Claude Code
│
└── ekosystem /
    ├── ekosystem-mapa.md
    │   Stack: Python 3.12, FastAPI, SQLAlchemy, PostgreSQL,
    │   Docker Compose, Alembic, pytest, ruff
    │   → linkuje do: [[_wspolne/narzedzia-dev]]
    │   → linkuje do: [[_wspolne/claude-code-workflow]]
    ├── stos-technologiczny.md
    └── konfiguracja.md
        Zawiera: docker compose up, make migrate, make test, porty
```

---

### Projekt 2 — MillWork

```
00-Projekty / MillWork /
│
├── 00-dashboard.md
│   Zawiera: v0.6.x, fazy 0–8 (0–8 ukończone), PROJECT STONE następny,
│   cel: v1.0 wiosna 2027, aktywne zadania
│
├── 01-cel-i-kontekst.md
│   Zawiera: plugin SketchUp dla stolarzy CNC, DXF export,
│   parametric joints, integracja z OpenCutList
│
├── docs /
│   ├── architektura.md          ← UI teleskopowy (3 panele), moduły
│   ├── decyzje.md               ← kluczowe decyzje projektowe
│   ├── roadmapa.md              ← fazy, wersje, harmonogram
│   ├── current-state.md         ← aktualny stan implementacji
│   ├── ui-architektura.md       ← panel 0/1/2, tiery Free/Pro/Team
│   └── wersjonowanie.md        ← SemVer, changelog, format
│
├── sesje /
│   └── session-log.md
│
├── beta-i-uzytkownicy /
│   ├── beta-program.md          ← fazy beta, testerzy
│   ├── feedback.md              ← zbieranie feedbacku
│   └── social-proof.md         ← case studies, cytaty
│
├── marketing /
│   ├── pozycjonowanie.md        ← "missing link between SketchUp and CNC"
│   ├── pricing.md               ← Free/Pro/Team, analiza konkurencji
│   ├── kanaly.md                ← LinkedIn, YouTube, Reddit, Product Hunt
│   └── lokalizacja.md          ← EN/PL/DE/FR/JA, harmonogram
│
└── ekosystem /
    ├── ekosystem-mapa.md
    │   Stack: Ruby (SketchUp API), JavaScript/HTML5 (panel UI),
    │   Python (Irecco_Lab backend), SketchUp 2026
    │   Narzędzia: SketchUp, deploy.bat/deploy.sh, Git
    │   → linkuje do: [[_wspolne/narzedzia-dev]]
    │   → linkuje do: [[_wspolne/github-workflow]]
    ├── stos-technologiczny.md
    └── konfiguracja.md
        Zawiera: deploy.bat, ścieżki Plugins, reload Ruby Console
```

---

### Projekt 3 — TechHub

```
00-Projekty / TechHub /
│
├── 00-dashboard.md
│   Zawiera: fazy 1–7 ukończone, Studio AI gotowe,
│   następne: test Studio z kluczem API, powiadomienia email
│
├── 01-cel-i-kontekst.md
│   Zawiera: narzędzie dla Aluprof S.A., produkcja materiałów szkoleniowych,
│   konwersja PPTX→PDF/SCORM/Flipbook, Brand Guardian, LMS: HCM DECK
│
├── docs /
│   ├── roadmapa.md              ← fazy 1–8, priorytety
│   ├── current-state.md         ← stan po sesji 9
│   └── it-deployment.md        ← przewodnik wdrożenia dla IT Aluprof
│
├── sesje /
│   └── session-log.md           ← przeniesiony z Drive: session-log.md
│
└── ekosystem /
    ├── ekosystem-mapa.md
    │   Stack: Python 3.12, FastAPI, SQLite, HTML5/JS (frontend),
    │   Claude API (claude-sonnet-4), python-pptx, pikepdf
    │   Narzędzia: start.bat, .venv, port 8765, przeglądarka
    │   → linkuje do: [[_wspolne/narzedzia-dev]]
    │   → linkuje do: [[_wspolne/anthropic-api]]
    ├── stos-technologiczny.md
    └── konfiguracja.md
        Zawiera: start.bat, .env (ANTHROPIC_API_KEY, port 8765),
        pip install -r requirements.txt, localhost:8765/docs
```

---

### Projekt 4 — Thomos

```
00-Projekty / Thomos /
│
├── 00-dashboard.md
│   Zawiera: Faza 0 MVP w toku, cel: beta publiczna Q4 2026,
│   decyzja: PocketBase jako backend, aktywne zadania
│
├── 01-cel-i-kontekst.md
│   Zawiera: platforma zdrowotna dla pacjentów, tłumacz dokumentów medycznych AI,
│   historia badań, alerty trendów (incidental findings),
│   model: darmowe dla pacjenta / płatne dla instytucji
│
├── docs /
│   ├── architektura-ui.md       ← 5 zakładek, mobile + web, mapa ekranów
│   ├── roadmapa-modulowa.md     ← warstwy W1–W7, harmonogram faz
│   ├── current-state.md         ← MVP beta, co jest / czego brakuje
│   ├── model-biznesowy.md       ← B2B: szpitale, pracodawcy, ubezpieczyciele
│   ├── decyzja-pocketbase.md   ← uzasadnienie wyboru backendu
│   └── onboarding-nawyk.md     ← filozofia pierwszego użycia, retencja
│
├── sesje /
│   └── session-log.md
│
├── beta-i-uzytkownicy /
│   ├── beta-program.md
│   └── feedback.md
│
└── ekosystem /
    ├── ekosystem-mapa.md
    │   Stack: Next.js (React), Tailwind CSS, PocketBase (backend + auth + storage),
    │   Claude API / Bielik (AI), TypeScript
    │   Hosting: VPS Hetzner EU (Finlandia), RODO
    │   → linkuje do: [[_wspolne/narzedzia-dev]]
    │   → linkuje do: [[_wspolne/anthropic-api]]
    │   → linkuje do: [[_wspolne/google-drive-sync]]
    ├── stos-technologiczny.md
    └── konfiguracja.md
        Zawiera: npm install, PocketBase setup, zmienne środowiskowe,
        localhost:8090 (PocketBase admin), npm run dev
```

---

## Plik `_wspolne/narzedzia-dev.md` — wspólna baza

To jest plik który wszystkie cztery projekty linkują. Zawiera:

```
# Wspólna baza narzędzi deweloperskich

## Zawsze potrzebne (każdy projekt)
- Git (kontrola wersji)
- Node.js LTS (JavaScript, npm)
- Python 3.12 (backend, skrypty)
- Claude Code (terminal w Obsidianie lub osobny)

## Potrzebne zależnie od projektu
- Docker Desktop → Irecco_Lab
- SketchUp 2026 → MillWork
- Python .venv → TechHub
- PocketBase → Thomos

## Linki do instalacji
- Git: https://git-scm.com/download/win
- Node.js: https://nodejs.org (LTS)
- Python: https://python.org/downloads
- Docker Desktop: https://docker.com/products/docker-desktop
- SketchUp: https://sketchup.com
- PocketBase: https://pocketbase.io
```

---

## Szablon pliku `ekosystem-mapa.md` per projekt

Każdy projekt ma swój plik `ekosystem/ekosystem-mapa.md` według tego szablonu:

```markdown
# [Nazwa Projektu] — Mapa ekosystemu narzędzi

## Stack technologiczny
(lista języków, frameworków, bibliotek)

## Narzędzia deweloperskie
- Co zainstalowane na dysku
- Co potrzebne do zainstalowania
- Co jest wspólne → [[_wspolne/narzedzia-dev]]

## Uruchomienie projektu
(krok po kroku jak odpalić lokalnie)

## Zmienne środowiskowe
(jakie klucze, porty, pliki .env)

## Repozytoria i pliki
(gdzie siedzi kod, gdzie Drive, gdzie GitHub)

## Status środowiska
- [ ] Zainstalowane
- [ ] Skonfigurowane
- [ ] Uruchomione i przetestowane
```

---

## Następny krok

Po zainstalowaniu Obsidiana (wg przewodnika `Irecco_Vault_Przewodnik_Instalacji.md`):

1. Utwórz foldery projektów wg tej struktury
2. Zacznij od wypełnienia `00-dashboard.md` dla każdego projektu
3. Następnie `ekosystem/ekosystem-mapa.md` — to jest właśnie ta "mapa narzędzi" której szukasz

---

*Dokument utworzony: 2026-06-26*
*Wersja: 1.0*
*Autor: Irecco_Lab*
