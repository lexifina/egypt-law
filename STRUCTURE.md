# Structure of egypt-law

Folder names are in Arabic, the language people search Egyptian law in. Years and numbers use Western digits.
Every folder holds at most 1,000 entries.

| Folder | What | One file is |
| --- | --- | --- |
| `دستور/` | The Constitution of 2014 as amended in 2019, Arabic text (the authoritative one) | one article (`art-001.md`) |
| `constitution/` | Its English translation by the State Information Service (not an official text) | one article |
| `قوانين/<السنة>/<الرقم>-<الموضوع>/` | Laws and codes, by year and number of the law | one article (`مادة-001.md`) |
| `أحكام/المحكمة-الدستورية-العليا/<السنة>/<الشهر>/` | Judgments and decisions of the Supreme Constitutional Court, by the day they were given | one judgment (`<الرقم>-لسنة-<السنة القضائية>-قضائية-<النوع>.md`, the type being دستورية, تنازع, تفسير or منازعة-تنفيذ) |
| `أحكام/محكمة-النقض/<السنة>/<الشهر>/` | Rulings of the Court of Cassation, by session day | one ruling (`<رقم الطعن>-لسنة-<السنة القضائية>-قضائية.md`) |
| `أحكام/مجلس-الدولة/<المحكمة>/<السنة>/<الشهر>/` | Rulings of the Council of State courts (المحكمة-الإدارية-العليا, محكمة-القضاء-الإداري, المحاكم-التأديبية, المحاكم-الإدارية), by the day given | one ruling (`<الرقم>-لسنة-<السنة>.md`) |
| `فتاوى/مجلس-الدولة/<الجهة>/<السنة>/<الشهر>/` | Opinions of the Council of State Fatwa and Legislation departments, by the day given | one opinion |
| `الجريدة-الرسمية/<السنة>/` | Issues of al-Jarida al-Rasmiya (the Official Gazette) | one issue (`العدد-<n>.md`, `العدد-<n>-مكرر.md`, `العدد-<n>-مكرر-أ.md`) |
| `الوقائع-المصرية/<السنة>/` | Issues of al-Waqa'i al-Misriya (the gazette supplement for decrees and decisions) | one issue |
| `data/`, `tools/` | Tables, charts and the tools to read the history | |

## Versions and dates

- One commit per version of a law, per judgment and per gazette issue, in the order the versions took effect.
- The author date is 12:00 Cairo time on the day the version took effect (judgments: the day given; gazette issues:
  the issue date). Before 1970 the date is 1970-01-01 and the real day starts the commit subject.
- Every commit carries the trailers `Kind:` (law, judgment, gazette, publisher, layout, documentation),
  `In-force:` (the day) and `In-force-basis:` (the clause or field the day comes from), and `Source:`.
- A record whose day cannot be read from the source is held, not committed.
- The author is the law, court or publisher that made the record.

## Sources

- Supreme Constitutional Court: the Court's own portal (sccourt.gov.eg), judgment text and metadata.
- Gazette issues: the State Information Service digital repository (mediadr.sis.gov.eg). The source marks these as
  electronic copies, not authoritative for dealings ("صورة إلكترونية لا يعتد بها عند التداول"), and each commit
  says so (`Source-status: unofficial copy`).
- Laws and codes: manshurat.org, an unofficial publisher, until a free official source exists (`Source-status:
  unofficial copy`). Laws are not protected by copyright (Law 82/2002, art. 141).
- Court of Cassation and Council of State rulings and opinions: secondary copies until an open official source exists (the Court of Cassation meters its full text; the Council of State has no open database): manshurat.org and mohamah.net. Every such commit says so (`Source-copy:`, `Source-copy-status: secondary copy; verification against the official text pending`).
- Names of parties in protected cases are not in paths or trailers.

`dustur/` was renamed `دستور/` on 2026-11-26 (a rename only; no text changed).
