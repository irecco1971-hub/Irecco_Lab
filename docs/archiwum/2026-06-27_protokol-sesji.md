# Protokół sesji — Irecco_Vault
*Reguły zarządzania dokumentacją na końcu każdej sesji Claude Code*

---

> **Gdzie mieszka ten plik:** `00-Projekty/_wspolne/protokol-sesji.md`
> **Obowiązuje:** wszystkie projekty (Irecco_Lab, MillWork, TechHub, Thomos) i każdy nowy projekt
> **Język komunikacji:** polski
> **Język projektów:** angielski (pliki projektowe pozostają po angielsku)

---

## Część 1 — Słowa klucze

Wpisujesz jedno z trzech zdań na końcu sesji. Claude rozpoznaje je i uruchamia odpowiedni scenariusz.

---

### 🔴 "koniec etapu"

Znaczenie: ten etap projektu jest zakończony. Możemy zamknąć dokumentację tego etapu.

Kiedy używać:
- skończyłeś fazę / etap / milestone opisany w roadmapie
- zamykasz temat który nie wróci jako aktywna praca (choć może być referencją)
- chcesz świadomie przenieść pliki do archiwum

Co uruchamia: **Scenariusz A** — pełny protokół zamknięcia etapu

---

### 🟡 "przerwa"

Znaczenie: praca nie jest skończona, wracam do tego później — dziś, jutro lub za tydzień.

Kiedy używać:
- musisz wyjść ale etap jest w połowie
- kończysz sesję ale projekt jest otwarty
- nie chcesz żeby cokolwiek było archiwizowane

Co uruchamia: **Scenariusz B** — zapis stanu, bez archiwizacji

---

### 🟢 "koniec dnia"

Znaczenie: kończę pracę na dziś, nie wiem kiedy wrócę, chcę mieć porządek.

Kiedy używać:
- koniec dnia roboczego
- nie jesteś pewny czy to koniec etapu czy przerwa
- chcesz po prostu zamknąć sesję czysto

Co uruchamia: **Scenariusz C** — minimalny protokół, tylko commit i dashboard

---

## Część 2 — Scenariusze

---

### Scenariusz A — "koniec etapu"

Claude wykonuje następujące kroki po kolei:

**Krok 1 — Identyfikacja etapu**
Claude wypisuje: "Zamykamy etap: [nazwa etapu]. Czy to poprawne?"
Czeka na potwierdzenie przed przejściem dalej.

**Krok 2 — Przegląd plików**
Claude skanuje pliki związane z tym etapem i wypisuje listę z propozycją akcji dla każdego:

```
Pliki do przejrzenia:

[ ] current-state.md          → zaktualizować (opisać stan po etapie)
[ ] session-log.md            → dopisać wpis zamknięcia etapu
[ ] [plik etapu].md           → przenieść do archiwum?
[ ] roadmapa.md               → oznaczyć etap jako ✅ zakończony?
```

**Krok 3 — Decyzja per plik**
Przy każdym pliku Claude pyta jednym zdaniem:
"[nazwa pliku] — przenieść do archiwum, zostawić jako historyczny, czy zaktualizować?"

Możliwe odpowiedzi: "archiwum", "zostaw", "zaktualizuj"

**Krok 4 — Archiwizacja**
Claude przenosi wskazane pliki do `archiwum/` z datą w nazwie:
Format: `[nazwa-pliku]-YYYY-MM-DD.md`
Przykład: `architecture-pre-STONE-2026-06-26.md`

Na górze każdego archiwizowanego pliku Claude dopisuje:
```
> Archiwum — zastąpiony przez [[nowy-plik]] — 2026-06-26
> Status: archiwum
```

**Krok 5 — Aktualizacja dashboardu**
Claude aktualizuje `00-dashboard.md` projektu:
- oznacza etap jako zakończony
- wpisuje datę zamknięcia
- aktualizuje "następne kroki"

**Krok 6 — Commit**
Claude wykonuje git commit z wiadomością:
`docs: zamknięcie etapu [nazwa] — archiwizacja dokumentacji`

---

### Scenariusz B — "przerwa"

Claude wykonuje trzy kroki:

**Krok 1 — Zapis stanu**
Claude pyta: "Gdzie jesteśmy? Napisz jedno zdanie co zostało zrobione i co zostało do zrobienia."
Wpisuje to do `session-log.md` jako wpis z datą.

**Krok 2 — Aktualizacja current-state**
Claude pyta: "Czy zaktualizować `current-state.md`?"
Jeśli tak — aktualizuje. Jeśli nie — pomija.

**Krok 3 — Commit**
Claude wykonuje git commit:
`docs: zapis stanu sesji — przerwa [data]`

Nic nie jest przenoszone do archiwum.

---

### Scenariusz C — "koniec dnia"

Claude wykonuje dwa kroki:

**Krok 1 — Aktualizacja dashboardu**
Claude pyta: "Co zrobiliśmy dziś? Jedno zdanie."
Wpisuje do `00-dashboard.md` jako ostatnia aktywność z datą.

**Krok 2 — Commit**
Claude wykonuje git commit:
`chore: koniec dnia [data]`

Nic nie jest analizowane, nic nie jest przenoszone.

---

## Część 3 — Reguły klasyfikacji plików

Reguły obowiązują we wszystkich projektach. Claude stosuje je automatycznie podczas Scenariusza A.

---

### Plik jest AKTYWNY gdy:

- opisuje obecny stan projektu (current-state, dashboard, roadmapa)
- jest używany jako instrukcja w bieżącej pracy (CLAUDE.md, konfiguracja)
- etap który opisuje jest otwarty w roadmapie
- data ostatniej modyfikacji nie ma znaczenia — liczy się status etapu

> Stara data ≠ nieaktualny plik.
> Plik z przed miesiąca który opisuje etap w toku jest AKTYWNY.

---

### Plik jest HISTORYCZNY gdy:

- opisuje etap który jest zakończony, ale decyzje w nim są nadal referencją
- jest to log sesji, changelog lub decisions.md — dokumenty ciągłe
- może być potrzebny do zrozumienia "dlaczego tak zdecydowaliśmy"

Historyczne pliki zostają na miejscu. Nie są przenoszone.
Na górze mają dopisek: `> Status: historyczny — etap [nazwa] zakończony [data]`

---

### Plik idzie do ARCHIWUM gdy:

- opisuje etap który jest zakończony I nie będzie już referencją w codziennej pracy
- jest duplikatem (stara wersja zastąpiona nową)
- ma w nazwie sufix `-v1`, `-old`, `-backup`, `-final`, `-WARNING`
- Ty świadomie decydujesz "to już nie wróci"

Archiwum = `archiwum/` wewnątrz folderu projektu.
Nazwa pliku w archiwum zawsze ma datę: `[nazwa]-YYYY-MM-DD.md`

---

### Plik NIGDY nie jest kasowany

Jedyny wyjątek: pliki tymczasowe (`.tmp`, logi systemowe, pliki testowe bez wartości dokumentacyjnej).
Wszystko inne — archiwum, nie kosz.

---

## Część 4 — Wzorzec dla nowych projektów

Każdy nowy projekt tworzony pod Irecco_Lab dziedziczy ten protokół automatycznie przez:

1. Link w `CLAUDE.md` projektu: `Protokół sesji: [[_wspolne/protokol-sesji]]`
2. Folder `archiwum/` tworzony od pierwszej sesji
3. `session-log.md` zakładany przy inicjalizacji projektu
4. `00-dashboard.md` z polem "ostatnia sesja" i "następne kroki"

Nowy projekt nie wymaga własnych reguł — dziedziczy wszystko z `_wspolne/`.
Wyjątek: projekt może dodać własne słowa klucze specyficzne dla swojej struktury
(np. MillWork może mieć "koniec fazy" jako alias dla "koniec etapu").

---

## Część 5 — Przykład w praktyce

**Sytuacja:** Kończysz PROJECT STONE w MillWork. Wpisujesz "koniec etapu".

Claude odpowiada:

```
Zamykamy etap: PROJECT STONE (MillWork v0.7.x). Czy to poprawne?

Pliki do przejrzenia:

[ ] current-state.md         → zaktualizować — opisać stan po STONE
[ ] session-log.md           → dopisać wpis zamknięcia PROJECT STONE
[ ] ST-01_BACKEND_WINS.md    → przenieść do archiwum?
[ ] ST-02_JS_WINS.md         → przenieść do archiwum?
[ ] roadmapa.md              → oznaczyć PROJECT STONE jako ✅?

Co robimy z ST-01_BACKEND_WINS.md?
```

Ty odpowiadasz: "archiwum"

Claude przenosi do `archiwum/ST-01_BACKEND_WINS-2026-06-26.md`
i dopisuje na górze pliku:
`> Archiwum — PROJECT STONE zakończony 2026-06-26`

I tak dalej, plik po pliku.

---

*Dokument utworzony: 2026-06-26*
*Wersja: 1.0*
*Autor: Irecco_Lab*
*Obowiązuje: wszystkie projekty Irecco_Lab*
