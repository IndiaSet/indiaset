"""
indiaset.resolve — fuzzy match district and state names to LGD codes.
"""

import os
import pandas as pd
from rapidfuzz import process, fuzz

_DATA_PATH = os.path.join(os.path.dirname(__file__), "data", "district_aliases.csv")
_aliases = None

# known historical/colonial renames that fuzzy matching can't catch
# because the old and new names share little spelling overlap
_MANUAL_ALIASES = {
    "bombay": "Mumbai",
    "poona": "Pune",
    "madras": "Chennai",
    "calcutta": "Kolkata",
    "bangalore": "Bengaluru",
    "trivandrum": "Thiruvananthapuram",
    "cochin": "Kochi",
    "mysore": "Mysuru",
    "baroda": "Vadodara",
    "allahabad": "Prayagraj",
    "gurgaon": "Gurugram",
}


def _load_aliases() -> pd.DataFrame:
    global _aliases
    if _aliases is None:
        _aliases = pd.read_csv(_DATA_PATH)
    return _aliases


def resolve_district(name: str, threshold: int = 80) -> dict | None:
    """
    Resolve a district name (any spelling) to its LGD code.

    Handles spelling variations across Census, LGD, and common
    usage — e.g. "Badgam" -> Budgam — as well as known historical
    renames — e.g. "Bombay" -> Mumbai, "Poona" -> Pune.

    Parameters
    ----------
    name : str
        District name in any common spelling.
    threshold : int, default 80
        Minimum match confidence (0-100). Lower = more lenient.

    Returns
    -------
    dict or None
        {'district_name': str, 'lgd_code': int, 'state_name': str,
         'match_score': int} or None if no good match found.

    Example
    -------
    >>> from indiaset import resolve_district
    >>> resolve_district("Poona")
    {'district_name': 'Pune', 'lgd_code': 521, 'state_name': 'Maharashtra', 'match_score': 100}
    """
    aliases = _load_aliases()

    # check manual aliases first for known historical renames
    name_lower = name.strip().lower()
    if name_lower in _MANUAL_ALIASES:
        name = _MANUAL_ALIASES[name_lower]

    # build a combined search pool from both census and lgd spellings
    choices = {}
    for _, row in aliases.iterrows():
        choices[row["district_name"]] = row
        choices[row["district_name_lgd"]] = row

    match = process.extractOne(
        name, choices.keys(), scorer=fuzz.WRatio
    )

    if match is None or match[1] < threshold:
        return None

    matched_name, score, _ = match
    row = choices[matched_name]

    return {
        "district_name": row["district_name_lgd"],
        "lgd_code": int(row["lgd_code"]),
        "state_name": row["state_name"],
        "match_score": int(score),
    }