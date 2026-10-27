#!/usr/bin/env python3
"""Rebuild nhtsa-complaints-by-model-2010-2025.csv from NHTSA's complaint flat file.

    python3 build_dataset.py FLAT_CMPL.txt [out.csv]

Input: NHTSA's consumer complaint flat file (FLAT_CMPL.txt, tab separated,
inside FLAT_CMPL.zip at https://www.nhtsa.gov/nhtsa-datasets-and-apis).
The Q3 2026 edition used the copy dated 2026-08-25; its sha256 is in
MANIFEST.json. NHTSA updates and adds records over time, so a later copy
gives slightly different counts.

Rules, exactly as in the published file:
- vehicle records only (PROD_TYPE "V"), model years 2010 to 2025;
- one complaint (ODINO) is counted once per make, model and model year
  (the model year is part of the dedupe key since 27 October 2026; in the
  2026-08-25 copy no complaint sits under two model years, so the output
  is byte-identical to the Zenodo revision 2 script);
- a complaint counts once under each distinct component it names, so a
  vehicle's component rows can add up to more than its year_total;
- make, model and model year groups with fewer than 10 complaints are left out;
- model names are kept as NHTSA records them (no merging of name variants);
- every component is kept; rows are ordered by make and model as printed,
  model year, then complaints (high to low) and component name;
- names are re-cased for reading (FORD FUSION -> Ford Fusion; components
  lower-cased with ":" written ", "). Python 3 standard library only.
"""
import collections, csv, io, sys

ODINO, MAKE, MODEL, YEAR, COMP, PROD_TYPE = 1, 3, 4, 5, 11, 45
YEAR_MIN, YEAR_MAX, FLOOR = 2010, 2025, 10
CAPS = {"BMW", "GMC", "RAM", "MINI", "KIA", "FIAT", "MG"}
BRAND = {"KIA": "Kia", "RAM": "Ram", "FIAT": "Fiat", "MERCEDES-BENZ": "Mercedes-Benz", "LAND ROVER": "Land Rover"}


def nice(w):
    if w in BRAND:
        return BRAND[w]
    out = []
    for tok in w.split(" "):
        if tok in CAPS or any(c.isdigit() for c in tok) or len(tok.replace("-", "")) <= 3:
            out.append(tok)
        else:
            out.append("-".join(p[:1].upper() + p[1:].lower() for p in tok.split("-")))
    return " ".join(out)


def comp(name):
    t = name.lower().replace(":", ", ")
    return t[:1].upper() + t[1:]


def main(src, dst):
    complaints = collections.Counter()
    components = collections.defaultdict(collections.Counter)
    seen, seen_c = set(), set()
    with io.open(src, encoding="utf-8", errors="ignore") as fh:
        for line in fh:
            c = line.rstrip("\n").split("\t")
            if len(c) <= PROD_TYPE or c[PROD_TYPE].strip() != "V":
                continue
            try:
                yr = int(c[YEAR])
            except ValueError:
                continue
            if not YEAR_MIN <= yr <= YEAR_MAX:
                continue
            mk, md = c[MAKE].strip(), c[MODEL].strip()
            if not mk or not md:
                continue
            key = (mk, md, yr)
            if (c[ODINO], mk, md, yr) not in seen:
                seen.add((c[ODINO], mk, md, yr))
                complaints[key] += 1
            cp = c[COMP].strip()
            if cp and (c[ODINO], mk, md, yr, cp) not in seen_c:
                seen_c.add((c[ODINO], mk, md, yr, cp))
                components[key][cp] += 1
    rows = []
    for key in sorted(complaints, key=lambda k: (nice(k[0]), nice(k[1]), k[2])):
        n = complaints[key]
        if n < FLOOR:
            continue
        for cp, k in sorted(components[key].items(), key=lambda x: (-x[1], x[0])):
            rows.append((nice(key[0]), nice(key[1]), key[2], comp(cp), k, n))
    with io.open(dst, "w", encoding="utf-8", newline="") as out:
        w = csv.writer(out, lineterminator="\n")
        w.writerow(["make", "model", "model_year", "component", "complaints", "year_total"])
        w.writerows(rows)
    groups = len({r[:3] for r in rows})
    total = sum(n for (mk, md, yr), n in complaints.items() if n >= FLOOR)
    print("%s rows, %s make/model/year groups, %s complaints -> %s" % (format(len(rows), ","), format(groups, ","), format(total, ","), dst))


if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    main(sys.argv[1], sys.argv[2] if len(sys.argv) > 2 else "nhtsa-complaints-by-model-2010-2025.csv")
