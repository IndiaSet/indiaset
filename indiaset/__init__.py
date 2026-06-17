"""
indiaset — India's open data layer.

Clean, versioned Indian government datasets,
one import away.
"""

from indiaset.census import load_census
from indiaset.resolve import resolve_district

__version__ = "0.1.0"
__all__ = ["load_census", "resolve_district"]