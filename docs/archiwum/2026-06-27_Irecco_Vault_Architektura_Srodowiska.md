# Irecco_Vault — Architektura środowiska
*Gdzie co mieszka i dlaczego*

---

## Decyzja architektoniczna

**Dwie warstwy. Zero Drive.**

```
Dysk C (lokalny)   ← tu pracujesz
GitHub             ← tu backupujesz i wersjonujesz
```

Google Drive nie jest potrzebny do ekosystemu Irecco_Lab.
Jeśli jest zainstalowany — można go odinstalować lub zostawić tylko do innych celów (faktury, skany, dokumenty biurowe).

---

## Warstwa 1 — Dysk C (praca lokalna)

Tu mieszka wszystko co aktywne. Tu pracujesz na co dzień.

```
C:/Users/Irecco71/Documents/
│
├── Mill_Work/          ← kod projektu MillWork
│   └── .git/           ← lokalne repozytorium Git
│
├── TechHub/            ← kod projektu TechHub
│   └── .git/
│
├── Thomos/             ← kod projektu Thomos (dawna Ostoja)
│   └── .git/
│
├── Irecco_Lab/         ← kod platformy Irecco_Lab
│   └── .git/
│
└── Irecco_Vault/       ← vault Obsidiana
    └── .git/           ← vault też jest repozytorium Git
```

Każdy projekt ma swój własny folder i swoje własne `.git`.
Vault Obsidiana jest traktowany jak projekt — też ma `.git`.

---

## Warstwa 2 — GitHub (backup i wersjonowanie)

Tu trafiają commity z dysku C. GitHub to jedyny backup.

```
GitHub /
│
├── repo: millwork          ← kod MillWork
├── repo: irecco-lab        ← kod platformy Irecco_Lab
├── repo: techhub           ← kod TechHub
├── repo: thomos            ← kod Thomos
└── repo: irecco-vault      ← vault Obsidiana (dokumentacja)
```

**Dlaczego GitHub wystarczy:**
- każdy commit to kopia z historią zmian
- dostępne z każdego komputera przez przeglądarkę
- bezpieczniejsze niż Drive
- wersjonowanie — wiesz co zmieniłeś i kiedy

---

## Vault Obsidiana jako repozytorium Git

Vault traktujemy jak projekt techniczny — ma swoje repo na GitHubie.

Commity vaulta według protokołu sesji (`protokol-sesji.md`):
- `docs: zamknięcie etapu [nazwa]` — po "koniec etapu"
- `docs: zapis stanu sesji — przerwa` — po "przerwa"
- `chore: koniec dnia [data]` — po "koniec dnia"

Dzięki temu historia vaulta jest tak samo śledzona jak historia kodu.

---

## Co z plikami tymczasowymi na Google Drive?

Podczas sesji 2026-06-26 powstały cztery dokumenty wgrane na Drive jako miejsce tymczasowe:

- `Irecco_Vault_Przewodnik_Instalacji.md`
- `Irecco_Vault_Struktura_Projektow.md`
- `protokol-sesji.md`
- `Irecco_Vault_Architektura_Srodowiska.md` (ten plik)

**Co zrobić przy pierwszym uruchomieniu:**
Skopiować te cztery pliki z Drive do:
`C:/Users/Irecco71/Documents/Irecco_Vault/00-Projekty/_wspolne/`

Po skopiowaniu — Drive nie jest już potrzebny dla tych plików.

---

## Schemat przepływu pracy

```
Piszesz kod lub dokumentację
        ↓
Dysk C — zmiany lokalne
        ↓
Git commit (według protokołu sesji)
        ↓
Git push → GitHub
        ↓
Backup gotowy, historia zachowana
```

Zero Drive w tym przepływie.

---

## Praca z innego komputera (np. z pracy)

Jeśli chcesz pracować z innego komputera:

```
Git clone [repo] → dysk lokalny → praca → commit → push
```

Nie potrzebujesz Drive. Potrzebujesz tylko Git i dostępu do GitHuba.

Jedyny przypadek gdzie Drive ma sens: komputer gdzie nie możesz nic zainstalować i masz tylko przeglądarkę. Wtedy Drive daje podgląd plików — ale tylko podgląd, nie pracę.

---

## Checklist przy pierwszym uruchomieniu

- [ ] Utworzyć folder `Irecco_Vault` na dysku C
- [ ] Zainicjować Git w tym folderze (`git init`)
- [ ] Założyć repo `irecco-vault` na GitHubie
- [ ] Połączyć lokalne repo z GitHubem (`git remote add origin`)
- [ ] Skopiować cztery dokumenty z Drive do `_wspolne/`
- [ ] Wykonać pierwszy commit: `chore: inicjalizacja vaulta`
- [ ] Sprawdzić czy wszystkie projekty mają repo na GitHubie

---

*Dokument utworzony: 2026-06-26*
*Wersja: 1.0*
*Autor: Irecco_Lab*
*Lokalizacja docelowa: `Irecco_Vault/00-Projekty/_wspolne/`*
