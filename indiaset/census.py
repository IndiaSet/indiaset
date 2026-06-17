"""
indiaset.census — load India's Census 2011 district data.
"""

import pandas as pd
from huggingface_hub import hf_hub_download


def load_census() -> pd.DataFrame:
    """
    Load India's Census 2011 district-level data.

    Returns a pandas DataFrame with 640 rows (one per district)
    and 29 columns covering population, literacy, sex ratio,
    workers, and SC/ST demographics.

    Example
    -------
    >>> from indiaset import load_census
    >>> df = load_census()
    >>> df.shape
    (640, 29)
    """
    path = hf_hub_download(
        repo_id="indiaset/census-2011",
        filename="census_2011_districts_final.parquet",
        repo_type="dataset",
    )
    return pd.read_parquet(path)