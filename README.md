# indiaset

India's open data layer. Clean, versioned datasets across 
government, agriculture, economy, health, and more — one 
pip install away.

## Install

```bash
pip install indiaset
```

## Quick Start

```python
from indiaset import load_census, resolve_district

# load india's census 2011 district data
df = load_census()
print(df.shape)  # (640, 29)

# resolve any district name to its LGD code
resolve_district("Poona")
# {'district_name': 'Pune', 'lgd_code': 490, 
#  'state_name': 'Maharashtra', 'match_score': 100}

resolve_district("Bombay")
# {'district_name': 'Mumbai', 'lgd_code': 482, ...}
```

## Why indiaset

Indian government data is real, official, and complete — but 
it lives in inconsistent formats with no standard naming. The 
same district gets spelled differently across Census, LGD, and 
common usage. `indiaset` fixes that.

- **`load_census()`** — clean Census 2011 district data, validated 
  against official totals
- **`resolve_district()`** — turns any spelling of a district name 
  ("Poona", "Badgam", "Bombay") into its permanent LGD code

## Datasets

| Dataset | Function | Status |
|---------|----------|--------|
| Census 2011 | `load_census()` | ✅ Live |
| Elections | `load_elections()` | 🔜 Coming |
| RBI Series | `get_rbi_series()` | 🔜 Coming |

## Links

- Datasets: [huggingface.co/indiaset](https://huggingface.co/indiaset)
- Source: [github.com/indiaset](https://github.com/indiaset)
- Twitter: [@indiaset_data](https://x.com/indiaset_data)

## License

Code: MIT · Data: CC-BY-4.0

## Citation

```
Jaiswal, Ansuman. (2026). indiaset [Software]. 
https://github.com/indiaset/indiaset
```
