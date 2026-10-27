# US vehicle owner complaints by model, 2010-2025

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.23662819.svg)](https://doi.org/10.5281/zenodo.23662819)
[![License: CC BY 4.0](https://img.shields.io/badge/License-CC%20BY%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by/4.0/)

Owner complaints filed with the US National Highway Traffic Safety Administration (NHTSA) for model years 2010 to 2025, counted per make, model and model year and split by every component owners named. Every make, model and model year with at least 10 complaints: 90,254 rows covering 4,087 make, model and year combinations from 84 makes (625,987 complaints).

This repository is a mirror. The permanent, citable copy is the Zenodo record [10.5281/zenodo.23685716](https://doi.org/10.5281/zenodo.23685716) (revision 2; all versions: [10.5281/zenodo.23662819](https://doi.org/10.5281/zenodo.23662819)). The full write-up, with charts and a per-vehicle lookup, is the [most complained-about cars report](https://oilandmiles.com/reports/most-complained-cars) on [Oil & Miles](https://oilandmiles.com).

## Key findings

From the [most complained-about cars report](https://oilandmiles.com/reports/most-complained-cars), Q3 2026 edition (NHTSA file dated 2026-08-25, model years 2010-2025):

1. The 2010 Ford Fusion has the most complaints of any vehicle: 5,126, with steering named most (1,640 of them).
2. Ford holds 17 of the 25 most complained-about vehicles, and 45 of the top 100.
3. Ford accounts for 20.8% of all 625,987 complaints in the file; Chevrolet is next at 9.3%.
4. Power train is the component named most in 9 of the top 25 vehicles; steering in 6.
5. The only vehicle from model year 2023 or newer in the top 100 is the 2023 Tesla Model Y, with 1,134 complaints.

New to the data? [`quickstart.ipynb`](quickstart.ipynb) loads the CSV, lists the top 10 vehicles and charts the components for one model.

## Files

| File | Contents |
|---|---|
| [`nhtsa-complaints-by-model-2010-2025.csv`](nhtsa-complaints-by-model-2010-2025.csv) | Every make, model and model year in the file with at least 10 complaints, model years 2010-2025, one row per component (all components, 90,254 rows) |
| [`most-complained-2026-q3.json`](most-complained-2026-q3.json) | Top 100 vehicles by complaint count, with the component named most |
| [`build_dataset.py`](build_dataset.py) | Rebuilds the CSV byte for byte from NHTSA's flat file (Python 3, standard library) |
| [`MANIFEST.json`](MANIFEST.json) | Input file date and sha256, rules, output checksums |
| [`CHANGELOG.md`](CHANGELOG.md) | What changed between revisions |
| [`latest.json`](latest.json) | The current edition, its dates, both DOIs and the file list, for scripts that check for a new edition |
| [`quickstart.ipynb`](quickstart.ipynb) | Load the CSV, list the top 10 vehicles, chart one vehicle's components (pandas, matplotlib) |

## CSV columns

| Column | Type | Meaning |
|---|---|---|
| `make` | string | Make as NHTSA records it |
| `model` | string | Model as NHTSA records it (name variants are not merged) |
| `model_year` | integer | 2010 to 2025 |
| `component` | string | System named in the complaint, in NHTSA's wording |
| `complaints` | integer | Complaints for this vehicle that name this component |
| `year_total` | integer | All complaints for this make, model and model year |

## Quick start

```python
import pandas as pd

url = "https://raw.githubusercontent.com/oilandmiles/us-vehicle-complaints-data/main/nhtsa-complaints-by-model-2010-2025.csv"
df = pd.read_csv(url)
vehicles = df.drop_duplicates(["make", "model", "model_year"])
print(vehicles.nlargest(10, "year_total")[["model_year", "make", "model", "year_total"]])
```

## Method

- Source: NHTSA's public consumer complaint file, copy dated 2026-08-25.
- A complaint can appear on several rows of NHTSA's file, one per component or product. Each complaint number is counted once per make, model and model year, and once per component.
- Make, model and model year combinations with fewer than 10 complaints are left out.
- Model names are kept exactly as NHTSA records them; name variants are not merged.
- The file covers every vehicle type NHTSA takes complaints for, so a few motorcycles, RVs and trailers sit among the cars, SUVs and pickups.
- A complaint can name several components, so a vehicle's component rows can add up to more than its `year_total`.

## Rebuild it

```bash
python3 build_dataset.py FLAT_CMPL.txt
```

FLAT_CMPL.txt comes inside FLAT_CMPL.zip at https://www.nhtsa.gov/nhtsa-datasets-and-apis. The published CSV was built from the copy dated 2026-08-25 (sha256 in MANIFEST.json). NHTSA updates and adds records, so a later copy gives slightly different counts.

## Limits

- These are counts, not failure rates. There are no sales figures, so a model that sells well can collect more complaints than a rarer one with a worse record.
- Filing is voluntary, and NHTSA doesn't confirm each owner's diagnosis. Recalls and news coverage cause spikes.
- Older model years have had longer on the road to collect complaints.

## Also available on

- Zenodo (canonical, DOI): https://doi.org/10.5281/zenodo.23685716 (all versions: https://doi.org/10.5281/zenodo.23662819)
- Kaggle: https://www.kaggle.com/datasets/iqbaltaherom/us-vehicle-owner-complaints-by-model-2010-2025
- Hugging Face: https://huggingface.co/datasets/iqbaltaher/us-vehicle-owner-complaints-by-model-2010-2025

## Citation

Please cite the Zenodo DOI. GitHub's "Cite this repository" button reads [`CITATION.cff`](CITATION.cff).

> Taher, I. (2026). *Most Complained-About Vehicles: NHTSA Owner Complaints by Make, Model and Model Year, 2010-2025 (Q3 2026 Edition)* [Data set]. Oil & Miles. https://doi.org/10.5281/zenodo.23685716

## License

The tables are released under [CC BY 4.0](LICENSE). The underlying complaint records are US government data from NHTSA.

Maintained by Iqbal Taher, [Oil & Miles](https://oilandmiles.com) ([ORCID 0009-0000-5745-9451](https://orcid.org/0009-0000-5745-9451)).
