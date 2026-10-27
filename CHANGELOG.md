# Changelog

## Mirror note (27 October 2026)

build_dataset.py here carries the model year in its de-duplication key, so the code matches the stated rule "once per make, model and model year". In the 2026-08-25 copy no complaint sits under two model years, so the CSV it writes is byte-identical to revision 2 (sha256 bd6a35c7...). The Zenodo revision 2 deposit keeps its original script.

## 2026-Q3, revision 2 (27 October 2026)

Corrections after an independent audit of the report and data. Same NHTSA copy (dated 2026-08-25), same rules; no complaint count and no ranking changed.

- CSV now carries every component for each make, model and model year (90,254 rows, 678 component labels). Revision 1 kept only the six components named most per vehicle (24,365 rows). Totals unchanged: 625,987 complaints across 4,087 make, model and model year combinations.
- Component shares in the report are now the share of the 625,987 complaints that name each component (Engine 20.5%). Revision 1 used mentions from the six-component file with "unknown or other" removed from the denominator (Engine 22.0%).
- Only the category "Unknown or other" is left out of the "named most" pick and the component chart. Revision 1 also dropped 29 real categories whose names contain "other" (for example "Fuel system, other" and "Seat belts, rear/other"); no vehicle's "named most" component changed.
- Model names stay exactly as NHTSA records them (for example "Silverado" and "Silverado 1500" are separate rows). The Oil & Miles complaints lookup merges a few such variants, so its counts can be slightly higher.
- The 2012 Dodge Dart row carries a note: NHTSA files these complaints under model year 2012; Dodge sold the modern Dart from model year 2013.
- PDF reprinted (revision 2): the full top 100 is printed, the BibTeX entry wraps, wording corrected (scope, method, comparisons with other studies).
- Added build_dataset.py (rebuilds the CSV byte for byte from the 2026-08-25 flat file) and MANIFEST.json (input and output checksums).

## 2026-Q3, revision 1 (26 October 2026)

First deposit: CSV (top six components per vehicle), top-100 JSON, report PDF.
