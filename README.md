# US vehicle owner complaints by model, 2010-2025

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.23662820.svg)](https://doi.org/10.5281/zenodo.23662820)
[![License: CC BY 4.0](https://img.shields.io/badge/License-CC%20BY%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by/4.0/)

Every owner complaint filed with the US National Highway Traffic Safety Administration (NHTSA) for model years 2010 to 2025, counted per make, model and model year and split by the component owners named. 24,365 rows covering 4,087 vehicles from 84 makes.

This repository is a mirror. The permanent, citable copy is the Zenodo record [10.5281/zenodo.23662820](https://doi.org/10.5281/zenodo.23662820). The full write-up, with charts and a per-vehicle lookup, is the [most complained-about cars report](https://oilandmiles.com/reports/most-complained-cars) on [Oil & Miles](https://oilandmiles.com).

## Files

| File | Contents |
|---|---|
| [`nhtsa-complaints-by-model-2010-2025.csv`](nhtsa-complaints-by-model-2010-2025.csv) | One row per vehicle and component (24,365 rows) |
| [`most-complained-2026-q3.json`](most-complained-2026-q3.json) | Top 100 vehicles by complaint count, with the component named most |

## CSV columns

| Column | Type | Meaning |
|---|---|---|
| `make` | string | Make as NHTSA records it |
| `model` | string | Model |
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
- Each complaint number is counted once per vehicle, which removes NHTSA's double filing of tire complaints.
- Vehicles with fewer than 10 complaints are left out.
- A complaint can name several components, so a vehicle's component rows add up to more than its `year_total`.

## Limits

- These are counts, not failure rates. There are no sales figures, so models that sell well collect more complaints.
- Complaints are voluntary and not verified by NHTSA. Recalls and news coverage cause spikes.
- Older model years have had longer on the road to collect complaints.

## Also available on

- Zenodo (canonical, DOI): https://doi.org/10.5281/zenodo.23662820
- Kaggle: https://www.kaggle.com/datasets/iqbaltaherom/us-vehicle-owner-complaints-by-model-2010-2025
- Hugging Face: https://huggingface.co/datasets/iqbaltaher/us-vehicle-owner-complaints-by-model-2010-2025

## Citation

Please cite the Zenodo DOI. GitHub's "Cite this repository" button reads [`CITATION.cff`](CITATION.cff).

> Taher, I. (2026). *Most Complained-About Vehicles: NHTSA Owner Complaints by Make, Model and Model Year, 2010-2025 (Q3 2026 Edition)* [Data set]. Oil & Miles. https://doi.org/10.5281/zenodo.23662820

## License

The tables are released under [CC BY 4.0](LICENSE). The underlying complaint records are US government data from NHTSA.

Maintained by Iqbal Taher, [Oil & Miles](https://oilandmiles.com) ([ORCID 0009-0000-5745-9451](https://orcid.org/0009-0000-5745-9451)).
