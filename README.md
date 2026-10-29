# Egypt: law history in git

The law of Egypt as a git history: one file per provision, one commit per law or decision on the day it took effect, and the law that made each change as the commit's author. `git blame` names the law behind every paragraph; `git log` lists every change to a provision; `tools/on.py` gives the text in force on any day.

It follows the shared design of [lexifina/global-law](https://github.com/lexifina/global-law), which places it at `eg/`.

> **First build.** The text is the English translation of the Constitution published by the State Information Service (sis.gov.eg), a state body. The Arabic text is the authoritative one. This first build holds one version of the Constitution; the amending laws and the other statutes are not yet built.

Language: the text is in English (the State Information Service translation of the Arabic Constitution), English first in this README.

**What is in it now**

| Folder | Act | Versions | History |
| --- | --- | ---: | --- |
| `constitution/` | Constitution of the Arab Republic of Egypt (2014, as amended 2019) | 1 | Oldest version available, dated 23 April 2019, the day the result of the referendum on the amendments was announced |

## Questions as git commands

| Question | Command |
| --- | --- |
| The whole act on a date | `python tools/on.py 2024-01-01 constitution` |
| One provision on a date | `python tools/on.py 2024-01-01 constitution <unit>` (unit = file name without `.md`) |
| Which law wrote each line of a provision? | `git blame constitution/<unit>.md` |
| Every change to a provision, word by word | `git log -p --word-diff constitution/<unit>.md` |
| Every law in the record, in order | `git log --reverse --format="%ad %an" --date=short main` |

After a rebuild, refresh tags with `git fetch --force --tags`: a plain fetch keeps stale tags.

## What it does not show

- **One version.** The State Information Service publishes only this consolidated text. The Constitution as adopted in January 2014 and the 2019 amending text are not shown as separate versions; the single version is dated 23 April 2019 and is credited to the publisher ("oldest version available").
- **English translation.** The Arabic text is authoritative and is not built here.
- **Headings and apparatus.** Part and Chapter headings, the table of contents, page numbers and the preamble footnote are left out; paragraph breaks are rebuilt from the PDF line layout.
- **Statutes.** No Egyptian statute is included yet; Egypt publishes consolidated laws only in the paid gazette (Al-Waqa'i al-Misriyya) and in subscription services.

## How it is built

Lexifina reads the sources listed here and records each act's dated versions, and the laws that made each change, in one corpus file. `tools/build.py` writes this repository from that file, and the same corpus always gives the same commit hashes; `REPRODUCE.md` gives the details and the checks. A model (Claude) wrote Lexifina's code; it wrote no legal text, and no model runs when the history is built.

Lexifina's code reads the PDF text layer with PyMuPDF and writes `corpus.json`. The shared builder turns `corpus.json` into the commits; `REPRODUCE.md` lists the sources, commands and decisions, and the result of the checks (every version read back from git on its in-force day and the day before, trailers parsed, no merge commits, dates never going backwards).

## Sources

| Source | What | Notes |
| --- | --- | --- |
| [State Information Service](https://sis.gov.eg/en/egypt/constitution-of-egypt/) | Constitution, English PDF with the 2019 amendments (Part VII, the House of Senates) | Official state body, but a translation; the Arabic text is authoritative. No licence stated. |

See `LICENSE` for the attribution.
