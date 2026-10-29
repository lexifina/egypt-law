import sys
sys.path.insert(0, r'~\AppData\Local\Temp\claude\C--Users-alany-Documents-lexifina\bf2c37ff-5368-4758-a217-51eee3902b94\scratchpad')
import mkdocs
F = r'~\Documents\lexifina\scripts\egypt-law'
mkdocs.write(F, 'egypt', 'EG', 'Egypt', 'English (the State Information Service translation of the Arabic Constitution)',
 [('`constitution/`', 'Constitution of the Arab Republic of Egypt (2014, as amended 2019)', '1', 'Oldest version available, dated 23 April 2019, the day the result of the referendum on the amendments was announced')],
 [('[State Information Service](https://sis.gov.eg/en/egypt/constitution-of-egypt/)', 'Constitution, English PDF with the 2019 amendments (Part VII, the House of Senates)', 'Official state body, but a translation; the Arabic text is authoritative. No licence stated.')],
 'The text is the English translation of the Constitution published by the State Information Service (sis.gov.eg), a state body. The Arabic text is the authoritative one. This first build holds one version of the Constitution; the amending laws and the other statutes are not yet built.',
 """The legal text is the Constitution of the Arab Republic of Egypt (2014, with the amendments approved by referendum
in April 2019), in the English translation published by the State Information Service
(https://sis.gov.eg/media/67726/dustor-eng.pdf), retrieved 29 October 2026. The PDF states no licence; the
official Arabic text is the authoritative one. The translation's own typing errors are kept as printed.""",
 ['**One version.** The State Information Service publishes only this consolidated text. The Constitution as adopted in January 2014 and the 2019 amending text are not shown as separate versions; the single version is dated 23 April 2019 and is credited to the publisher ("oldest version available").',
  '**English translation.** The Arabic text is authoritative and is not built here.',
  '**Headings and apparatus.** Part and Chapter headings, the table of contents, page numbers and the preamble footnote are left out; paragraph breaks are rebuilt from the PDF line layout.',
  '**Statutes.** No Egyptian statute is included yet; Egypt publishes consolidated laws only in the paid gazette (Al-Waqa\'i al-Misriyya) and in subscription services.'],
 '`parse.py` reads the PDF text layer with PyMuPDF and writes `corpus.json`.')
mkdocs.jur(F, 'egypt', 'EG', 'Egypt', 'first build: Constitution (2014, as amended 2019), English translation by the State Information Service (1 version, oldest available, 2019-04-23)', 1)
