# How this repository was made (Egypt)

This file is written by the build on 2026-11-02, the day the source data was retrieved.

## Sources

| Source | Address | Retrieved | Licence |
| --- | --- | --- | --- |
| State Information Service: Constitution of the Arab Republic of Egypt (English PDF) | <https://sis.gov.eg/media/67726/dustor-eng.pdf> | 2026-10-29 | no licence stated; official English text of a constitution published by a state body |
| State Information Service: دستور جمهورية مصر العربية (Arabic web page) | <https://sis.gov.eg/ar/%D9%85%D8%B5%D8%B1/%D8%A7%D9%84%D8%AF%D8%B3%D8%AA%D9%88%D8%B1-%D8%A7%D9%84%D9%85%D8%B5%D8%B1%D9%89/> | 2026-11-02 | official text; Law 82/2002 art. 141 excludes laws and official documents from copyright protection |

Every word of law in this repository comes from these sources. Lexifina reads them and records each act's dated versions, and the laws that made each change, in one corpus file. This repository is built from that file.

## What is in it

| Act | Title | Versions | Span |
| --- | --- | ---: | --- |
| `constitution` | Constitution of the Arab Republic of Egypt (2014, as amended 2019) | 1 | 2019-04-23 to 2019-04-23 |
| `dustur` | دستور جمهورية مصر العربية (2014، بتعديلات 2019) | 1 | 2019-04-23 to 2019-04-23 |

The build made 2 commits:

| Commits | Kind |
| ---: | --- |
| 2 | first version of an act |
| 0 | one law on its in-force day |
| 0 | changes no amendment note explains, credited to the publisher |

Other counts:
- 0 commits on the branch `future`: laws not yet in force on 2026-11-02.
- 0 commits dated 1 January 1970: in force before 1970, with the real day in their `In-force` trailer.
- 0 laws in the record.
- 2 tags.

## Dates

Each commit is dated at noon (Africa/Cairo) on the day the change took effect. The other dates, enacted and published, are trailers.

When a law gives no date of its own, the default rule applies: Constitution art. 247 (2014): the Constitution takes effect when the approval of the people in a referendum is announced; the 2019 amendments took effect when the referendum result of 20-22 April 2019 was announced on 23 April 2019. https://sis.gov.eg/en/egypt/constitution-of-egypt/

## How the history is built

`tools/build.py` turns the corpus into this history in one pass: one commit per law, on the day it took effect. The same corpus always gives the same commit hashes. `tools/check_repo.py` reads every version back from git and compares it with the corpus. `tools/on.py` shows the law as it stood on any date. The corpus format is described in `tools/SCHEMA.md`.

- Corpus: sha256 `eed210a0813f897fe64be0c311c0941c439bbe110f9caac6645d2e3e583ca273` (354632 bytes).
- Builder blob hashes (`git hash-object`): `build.py` `a4faa25af85facb64b956b372f6b528aafdd7ec1`, `check.py` `3d00541d258745461ab52b1b0cb4e1716a27a95d`, `on.py` `644a6c0857fbcc72562032b58d57aa113fee0641`.
- Python 3.12.10; git version 2.46.0.windows.1.

## Checks

Not yet run for this build.

No second build of this corpus has been compared yet.

## Decisions made by hand

- English is the official translation published by the State Information Service; the official Arabic text is the authoritative one and is not built here.
- One version, the oldest available (first_law null), credited to the State Information Service. The PDF states no date; it is the consolidated text including the 2019 amendments (it contains Part VII, the House of Senates), so it is dated 2019-04-23, the day the referendum result was announced and the amendments took effect.
- The 2014 text as first adopted (in force 18 January 2014) and the individual amending acts are not built: the SIS publishes only this consolidated text.
- Unit files: the preamble and one per article (art-NNN, 1-254); Part and Chapter headings, the table of contents, page numbers and the preamble footnote are left out. Paragraph breaks are rebuilt from the PDF line layout (a short line ending in . : or ; ends a paragraph; list items start new lines), so a few paragraph joins may differ from print.
- Arabic (act dustur): the authoritative text, from the State Information Service Arabic constitution page. One version dated 2019-04-23 and credited to the publisher (oldest version available): the page gives only the consolidated text, with footnotes naming the articles substituted or added in April 2019 (among them 185, 189, 190, 193, 200, 204, 234, 241 bis, 243, 244, 244 bis and Part VII).
- Arabic units: the preamble and one file per article (art-001 to art-254, plus art-150-bis, art-241-bis and art-244-bis). Paragraphs are the page's <p> and <br> breaks. Left out: the document title, Part, Chapter and Section headings, the Part VII heading, footnotes (everything after the underscore rule) and their markers, and the page's essay on earlier Egyptian constitutions.
- Arabic typesetting: tatweel (U+0640, letter stretching), non-breaking spaces and runs of spaces are removed or collapsed, and curly quotes become straight quotes; letters and digits are kept as printed (the page mixes Arabic-Indic and Western digits). Article headings are written in one form, مادة N, with Western digits.

## What AI did and did not do

The scripts that read the sources and build this repository were written by Claude Code running Claude Opus 5.5 (`claude-opus-5-5`) under Lexifina's direction.

No model wrote, translated or corrected legal text. No model runs at build time. Every word of law in this repository comes from the official sources above.

The commit messages are written by `build.py` from the source data.

Model use at data-build time:
- Claude Code wrote the code and chose the source; it did not write or alter any legal text. The code is deterministic and runs no model.
