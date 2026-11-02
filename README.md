# Egypt: law history in git

The law of Egypt as a git history: one file per provision, one commit per law or decision on the day it took effect, and the law that made each change as the commit's author. `git blame` names the law behind every paragraph; `git log` lists every change to a provision; `tools/on.py` gives the text in force on any day.

It follows the shared design of [lexifina/global-law](https://github.com/lexifina/global-law), which places it at `eg/`.

> **Constitution only.** The Constitution in its official Arabic text (`dustur/`) and in the English translation (`constitution/`), both as published by the State Information Service (sis.gov.eg), a state body. The Arabic text is the authoritative one. Each holds one version, the 2014 Constitution as amended in April 2019; the statutes are not yet built.

Language: Arabic (`dustur/`, authoritative) and English (`constitution/`, the State Information Service translation); English first in this README.

**What is in it now**

| Folder | Act | Versions | History |
| --- | --- | ---: | --- |
| `dustur/` | دستور جمهورية مصر العربية (2014، بتعديلات 2019), the Arabic text | 1 | Oldest version available, dated 23 April 2019, the day the result of the referendum on the amendments was announced |
| `constitution/` | Constitution of the Arab Republic of Egypt (2014, as amended 2019), English translation | 1 | Oldest version available, dated 23 April 2019 |

## Questions as git commands

| Question | Command |
| --- | --- |
| The whole act on a date | `python tools/on.py 2024-01-01 dustur` |
| One provision on a date | `python tools/on.py 2024-01-01 dustur art-102` (unit = file name without `.md`) |
| Which law wrote each line of a provision? | `git blame dustur/<unit>.md` |
| Every change to a provision, word by word | `git log -p --word-diff dustur/<unit>.md` |
| Every law in the record, in order | `git log --reverse --format="%ad %an" --date=short main` |

After a rebuild, refresh tags with `git fetch --force --tags`: a plain fetch keeps stale tags.

## What it does not show

- **One version.** The State Information Service publishes only the consolidated text. The Constitution as adopted in January 2014 and the 2019 amending text are not shown as separate versions; the single version of each act is dated 23 April 2019 and is credited to the publisher ("oldest version available"). The Arabic page's footnotes, left out here, name the articles substituted or added in April 2019.
- **Two texts.** `dustur/` is the authoritative Arabic text; `constitution/` is the English translation, which has no separate files for articles 150 bis, 241 bis and 244 bis: their text sits at the end of articles 150, 241 and 244.
- **Headings and apparatus.** Part, Chapter and Section headings, the table of contents, page numbers and footnotes are left out. Arabic paragraphs follow the web page; English paragraph breaks are rebuilt from the PDF line layout.
- **Statutes.** No Egyptian statute is included yet. The official consolidated legislation databases (the Court of Cassation's and the Cabinet's) and the gazette give the full text only to subscribers.

## How it is built

Lexifina reads the sources listed here and records each act's dated versions, and the laws that made each change, in one corpus file. `tools/build.py` writes this repository from that file, and the same corpus always gives the same commit hashes; `REPRODUCE.md` gives the details and the checks. A model (Claude) wrote Lexifina's code; it wrote no legal text, and no model runs when the history is built.

Lexifina reads the sources listed here and records each act's dated versions, and the laws that made each change, in one corpus file. `REPRODUCE.md` gives the details and the checks. A model (Claude) wrote Lexifina's code; it wrote no legal text, and no model runs when the history is built.

Lexifina's code reads the Arabic web page and the English PDF text layer (PyMuPDF) and writes `corpus.json`. The shared builder turns `corpus.json` into the commits; `REPRODUCE.md` lists the sources, commands and decisions, and the result of the checks (every version read back from git on its in-force day and the day before, trailers parsed, no merge commits, dates never going backwards).

## Sources

| Source | What | Notes |
| --- | --- | --- |
| [State Information Service](https://sis.gov.eg/ar/%D9%85%D8%B5%D8%B1/%D8%A7%D9%84%D8%AF%D8%B3%D8%AA%D9%88%D8%B1-%D8%A7%D9%84%D9%85%D8%B5%D8%B1%D9%89/) | Constitution, Arabic text with the 2019 amendments | Official state body; authoritative text. Official documents are excluded from copyright (Law 82/2002 art. 141). |
| [State Information Service](https://sis.gov.eg/en/egypt/constitution-of-egypt/) | Constitution, English PDF with the 2019 amendments (Part VII, the House of Senates) | Official state body, but a translation. |

See `LICENSE` for the attribution.
