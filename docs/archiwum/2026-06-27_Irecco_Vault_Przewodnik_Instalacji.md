# Irecco_Vault — Przewodnik instalacji środowiska
**System:** Windows 11 | **Sync:** Google Drive | **Narzędzia:** Obsidian + Claude Code

---

> **Jak korzystać z tego przewodnika:**
> Wykonuj kroki po kolei. Każdy krok ma tytuł, opis co zrobić, i informację czego się spodziewać.
> Nie przechodź do następnego kroku, dopóki poprzedni nie działa poprawnie.

---

## ETAP 1 — Instalacja Obsidiana

### Krok 1.1 — Pobierz Obsidiana

1. Otwórz przeglądarkę i wejdź na: **https://obsidian.md/download**
2. Kliknij przycisk **"Download for Windows"**
3. Pobierze się plik o nazwie podobnej do: `Obsidian-1.x.x.exe`
4. Zapisz go na Pulpicie lub w folderze Pobrane

### Krok 1.2 — Zainstaluj Obsidiana

1. Kliknij dwukrotnie pobrany plik `.exe`
2. Pojawi się okno instalatora — kliknij **"Install"**
3. Instalacja trwa około 30 sekund
4. Na końcu kliknij **"Finish"**
5. Obsidian uruchomi się automatycznie

**Czego się spodziewać:** Po uruchomieniu zobaczysz ekran powitalny z pytaniem o vault.

---

## ETAP 2 — Tworzenie vaulta na Google Drive

### Krok 2.1 — Znajdź folder Google Drive na dysku

1. Otwórz **Eksplorator plików** (ikona folderu na pasku zadań)
2. W lewym panelu znajdź **Google Drive** (zwykle jako dysk `G:\` lub folder w nawigacji)
3. Wejdź do głównego folderu Google Drive

### Krok 2.2 — Utwórz folder Irecco_Vault

1. Kliknij prawym przyciskiem myszy w pustym miejscu
2. Wybierz **Nowy → Folder**
3. Nazwij folder dokładnie: `Irecco_Vault`
4. Zatwierdź klawiszem Enter

**Ważne:** Folder `Irecco_Vault` siedzi obok istniejącego folderu `Irecco_Lab`, nie wewnątrz niego:

```
Google Drive /
├── Irecco_Lab /       ← istniejący projekt
└── Irecco_Vault /     ← nowe centrum dowodzenia (właśnie utworzony)
```

### Krok 2.3 — Utwórz vault w Obsidianie

1. Wróć do Obsidiana
2. Na ekranie powitalnym zobaczysz trzy opcje — wybierz **"Open folder as vault"**
3. Otworzy się okno wyboru folderu
4. Nawiguj do Google Drive i wejdź do folderu `Irecco_Vault`
5. Kliknij **"Select Folder"**

**Czego się spodziewać:** Obsidian otworzy się z pustym vaultem. Po lewej stronie zobaczysz pusty panel plików.

---

## ETAP 3 — Struktura folderów

### Krok 3.1 — Utwórz główne foldery

W Obsidianie, w lewym panelu (panel plików), kliknij ikonę **nowego folderu** (lub kliknij prawym przyciskiem → New folder) i utwórz kolejno następujące foldery:

**Obszar zawodowy:**
```
00-Projekty
01-Klienci
02-Finanse
03-Marketing
04-Rozwój
```

**Obszar prywatny:**
```
10-Dom
11-Zdrowie
12-Finanse-osobiste
```

**Obszar osobisty:**
```
20-Nauka
21-Inspiracje
22-Dziennik
```

**System pracy (wspólny dla wszystkich obszarów):**
```
90-Inbox
91-Archiwum
92-AI-Zone
93-Szablony
```

**Pliki systemowe:**
```
.claude              ← folder konfiguracyjny Claude Code (ukryty)
```

### Krok 3.2 — Utwórz plik dashboard

1. W lewym panelu kliknij ikonę **nowej notatki**
2. Nazwij ją: `home`
3. Zostaw ją na razie pustą — wypełnimy ją w kolejnym etapie

**Struktura po tym kroku:**
```
Irecco_Vault /
├── .claude /
├── 00-Projekty /
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
└── home.md
```

---

## ETAP 4 — Konfiguracja Obsidiana

### Krok 4.1 — Włącz Community Plugins

1. Kliknij ikonę **zębatki** (Settings) w lewym dolnym rogu
2. W lewym menu znajdź i kliknij **"Community plugins"**
3. Kliknij przycisk **"Turn on community plugins"**
4. Potwierdź klikając **"Turn on"**

**Czego się spodziewać:** Pojawi się sekcja z przyciskiem "Browse" do przeglądania pluginów.

### Krok 4.2 — Zainstaluj plugin Terminal

Terminal pozwoli Ci uruchamiać Claude Code bezpośrednio w Obsidianie.

1. W sekcji Community plugins kliknij **"Browse"**
2. W polu wyszukiwania wpisz: `Terminal`
3. Znajdź plugin o nazwie **"Terminal"** (autor: polyipseity)
4. Kliknij **"Install"**
5. Po instalacji kliknij **"Enable"**

### Krok 4.3 — Skonfiguruj Terminal

1. Wróć do Settings → Community plugins
2. Znajdź Terminal na liście i kliknij ikonę zębatki obok niego
3. W ustawieniach znajdź opcję trybu — ustaw na **"Integrated"**
4. Zamknij ustawienia

**Jak otworzyć Terminal:** Użyj skrótu `Ctrl + Alt + T` lub znajdź ikonę terminala na lewym pasku.

**Ważne:** Po otwarciu terminala — **przypnij go** (kliknij prawym przyciskiem na zakładkę terminala → Pin). Dzięki temu terminal nie zniknie gdy przełączysz się na inną notatkę, a sesja Claude Code nie urwie się.

### Krok 4.4 — Zainstaluj plugin Show Hidden Files

Ten plugin pozwoli Ci widzieć i edytować folder `.claude` bezpośrednio w Obsidianie.

1. W Community plugins kliknij **"Browse"**
2. Wyszukaj: `Show Hidden Files`
3. Zainstaluj i włącz plugin

**Czego się spodziewać:** W panelu plików pojawi się folder `.claude` i `.obsidian`.

---

## ETAP 5 — Plik konfiguracyjny claude.md

### Krok 5.1 — Utwórz plik claude.md

1. W panelu plików wejdź do folderu `.claude`
2. Utwórz nowy plik o nazwie: `claude.md`
3. Wklej do niego poniższą treść i dostosuj pod siebie:

```markdown
# Irecco_Vault — Instrukcje dla Claude

## Persona i język
- Pracuj wyłącznie po polsku.
- Jesteś architektem wiedzy, redaktorem notatek i asystentem projektowym.
- Twoim zadaniem jest porządkować, łączyć i rozwijać informacje w tym vaultcie.

## Cel vaulta
- Irecco_Vault to osobiste centrum dowodzenia dla wszystkich obszarów życia i pracy.
- Jest niezależny od poszczególnych projektów — jest ponad nimi.
- Wszystkie ważne informacje trzymamy w plikach Markdown.
- Vault jest single source of truth.

## Struktura folderów
- `90-Inbox` = wszystko nieprzetworzone, surowe notatki, szybkie myśli
- `00-Projekty` = aktywne projekty zawodowe (Irecco_Lab, MillWork, Tech Hub itd.)
- `01-Klienci` = informacje o klientach
- `02-Finanse` = faktury, budżety, zestawienia zawodowe
- `03-Marketing` = pomysły, kampanie, treści
- `04-Rozwój` = nauka zawodowa, kursy, narzędzia
- `10-Dom` = sprawy domowe
- `11-Zdrowie` = zdrowie, sport, samopoczucie
- `12-Finanse-osobiste` = budżet osobisty, oszczędności
- `20-Nauka` = książki, kursy, notatki ze źródeł
- `21-Inspiracje` = pomysły, cytaty, rzeczy które mnie inspirują
- `22-Dziennik` = codzienne refleksje, logi dnia
- `91-Archiwum` = rzeczy zakończone lub nieaktualne
- `92-AI-Zone` = raporty i analizy generowane przez Claude
- `93-Szablony` = szablony notatek do ponownego użycia

## Linkowanie
- Zawsze używaj wikilinków `[[Nazwa notatki]]` gdy odnosisz się do innej notatki.
- Nowe notatki powinny linkować do istniejących gdy dotyczą tych samych tematów.

## Tagowanie
Używaj wyłącznie tagów z tej listy — nie twórz nowych bez mojej zgody:
- `#projekt`
- `#klient`
- `#finanse`
- `#idea`
- `#zadanie`
- `#research`
- `#inspiracja`
- `#decyzja`
- `#spotkanie`
- `#AI`
- `#weekly`
- `#osobiste`

## Reguły pracy
- Nowe notatki lądują w `90-Inbox` — nie porządkuj ich od razu.
- Raz w tygodniu uruchamiamy brainsweep który porządkuje Inbox.
- Po większych zmianach aktualizuj `home.md`.
- Niczego nie kasuj bez polecenia — przenoś do `91-Archiwum`.
- Twórz krótkie TL;DR dla dłuższych tekstów.

## Aktualizacja tego pliku
- Jeśli proszę o zmianę claude.md:
  - najpierw przeczytaj obecny plik,
  - zaproponuj konkretne zmiany,
  - czekaj na moją akceptację zanim zapiszesz.
```

### Krok 5.2 — Zapisz plik

Obsidian zapisuje pliki automatycznie. Wystarczy że wkleisz treść i przejdziesz do innej notatki.

---

## ETAP 6 — Dashboard home.md

### Krok 6.1 — Wypełnij home.md

Otwórz plik `home.md` który utworzyłeś wcześniej i wklej:

```markdown
# Home — Centrum Dowodzenia

## Status
- Ostatnia aktualizacja: {{data}}
- Ostatni brainsweep: —
- Inbox: sprawdź folder 90-Inbox

## Aktywne projekty
- [[00-Projekty/Irecco_Lab]]
- [[00-Projekty/MillWork]]
- [[00-Projekty/Tech-Hub]]

## Ostatnie analizy AI
- (pojawią się tu po pierwszym brainsweepie)

## Do zrobienia tej semana
- (wpisuj na bieżąco)

## Obszary do pogłębienia
- (pojawią się tu po analizie emerge)
```

---

## ETAP 7 — Instalacja Claude Code

### Krok 7.1 — Sprawdź czy masz Node.js

1. Naciśnij `Windows + R`, wpisz `cmd`, naciśnij Enter
2. W oknie wiersza poleceń wpisz: `node --version`
3. Jeśli widzisz numer wersji (np. `v20.x.x`) — Node.js jest zainstalowany, przejdź do Kroku 7.3
4. Jeśli widzisz błąd — przejdź do Kroku 7.2

### Krok 7.2 — Zainstaluj Node.js (jeśli potrzebne)

1. Wejdź na: **https://nodejs.org**
2. Kliknij przycisk **"LTS"** (wersja stabilna)
3. Pobierz i uruchom instalator `.msi`
4. Klikaj "Next" przez cały instalator, pozostaw domyślne ustawienia
5. Po instalacji uruchom ponownie komputer
6. Sprawdź instalację: w cmd wpisz `node --version`

### Krok 7.3 — Zainstaluj Claude Code

1. Otwórz wiersz poleceń (`Windows + R` → `cmd`)
2. Wpisz i zatwierdź Enterem:
```
npm install -g @anthropic-ai/claude-code
```
3. Poczekaj na zakończenie instalacji (może trwać 1-2 minuty)
4. Sprawdź instalację wpisując: `claude --version`

### Krok 7.4 — Połącz Claude Code z vaultem

1. W wierszu poleceń przejdź do folderu vaulta:
```
cd "G:\Mój dysk\Irecco_Vault"
```
*(dostosuj ścieżkę do swojego Google Drive)*

2. Uruchom Claude Code:
```
claude
```
3. Przy pierwszym uruchomieniu otworzy się przeglądarka z prośbą o zalogowanie — zaloguj się na swoje konto Anthropic
4. Po zalogowaniu wróć do terminala — Claude Code jest gotowy

**Czego się spodziewać:** Zobaczysz znak zachęty `>` — Claude czeka na Twój prompt i widzi wszystkie pliki vaulta.

### Krok 7.5 — Uruchom Terminal w Obsidianie

Zamiast osobnego okna cmd, możesz teraz pracować z Claude Code bezpośrednio w Obsidianie:

1. Otwórz Terminal w Obsidianie (`Ctrl + Alt + T`)
2. Upewnij się że jesteś w folderze vaulta (terminal powinien pokazywać ścieżkę do `Irecco_Vault`)
3. Wpisz `claude` i naciśnij Enter
4. Claude Code uruchomi się wewnątrz Obsidiana

---

## ETAP 8 — Pierwsze uruchomienie i test systemu

### Krok 8.1 — Inicjalny prompt

Po uruchomieniu `claude` w terminalu wpisz:

```
Przeczytaj plik .claude/claude.md i home.md.
Napisz krótkie podsumowanie jak rozumiesz rolę tego vaulta
i jakie działania proponujesz na start.
```

**Czego się spodziewać:** Claude potwierdzi że widzi strukturę vaulta i opisze jak rozumie jego cel.

### Krok 8.2 — Test brainsweep

Gdy masz już kilka notatek w `90-Inbox`, uruchom:

```
Uruchom tygodniowy brainsweep vaulta.

1. Przejrzyj wszystkie pliki w 90-Inbox.
2. Sklasyfikuj każdą notatkę do kategorii:
   - idea-zawodowa, idea-osobista, zadanie, research,
     inspiracja, decyzja, log-dnia
3. Przenieś przetworzone notatki do właściwych folderów.
4. Dodaj wikilinki do powiązanych notatek.
5. Używaj tylko tagów z listy w claude.md.
6. Zaktualizuj home.md.
7. Na końcu wypisz podsumowanie: ile notatek, główne wątki, rekomendacje.
```

---

## ETAP 9 — Komendy operacyjne (codzienna praca)

### `brainsweep` — tygodniowe porządki
Uruchamiaj raz w tygodniu. Czyści Inbox, porządkuje notatki, aktualizuje dashboard.

### `ask` — pytanie do całej bazy wiedzy
```
Odpowiedz na pytanie korzystając wyłącznie z wiedzy w tym vaultcie.
Pytanie: [TWOJE PYTANIE]
Po odpowiedzi wypisz z których plików korzystałeś
i zaproponuj 3 pytania pogłębiające.
```

### `emerge` — analiza całości (co kilka tygodni)
```
Przeprowadź analizę emerge całego vaulta.
1. Zidentyfikuj główne tematy i połączenia między notatkami.
2. Wskaż obszary niedolinkowane.
3. Wykryj luki w dokumentacji.
4. Zaproponuj 3-5 priorytetowych tematów do pogłębienia.
Zapisz raport do 92-AI-Zone/emerge-[data].md i podlinkuj w home.md.
```

### `deepen` — pogłębienie tematu
```
Pogłęb temat: [TEMAT lub [[notatka]]].
1. Przejrzyj powiązane notatki w vaultcie.
2. Wypisz co już wiemy i czego brakuje.
3. Zaproponuj pytania badawcze.
4. Utwórz szkic notatki pojęciowej.
```

---

## Check-lista — system gotowy gdy masz odhaczone wszystko poniżej

- [ ] Obsidian zainstalowany i uruchomiony
- [ ] Vault `Irecco_Vault` utworzony na Google Drive
- [ ] Struktura folderów (00-Projekty, 90-Inbox itd.) gotowa
- [ ] Community plugins włączone
- [ ] Plugin Terminal zainstalowany i przypięty
- [ ] Plugin Show Hidden Files zainstalowany
- [ ] Plik `.claude/claude.md` wypełniony
- [ ] Plik `home.md` wypełniony
- [ ] Node.js zainstalowany (`node --version` działa)
- [ ] Claude Code zainstalowany (`claude --version` działa)
- [ ] Pierwsze uruchomienie `claude` w folderze vaulta — zalogowany
- [ ] Inicjalny prompt wykonany — Claude widzi vault

---

## Następne kroki po uruchomieniu systemu

Gdy całość działa, możesz stopniowo dodawać:

- **Obsidian Web Clipper** — zapisywanie stron internetowych jako `.md` do `90-Inbox`
- **Obsidian Skills** (kepano) — lepsze rozumienie Obsidiana przez Claude Code
- **Szablony notatek** w folderze `93-Szablony` — dla projektów, klientów, spotkań
- **Foldery projektowe** wewnątrz `00-Projekty` — osobny podfolder dla każdego projektu

---

*Dokument utworzony: 2026-06-26*
*Wersja: 1.0*
*Autor: Irecco_Lab*
