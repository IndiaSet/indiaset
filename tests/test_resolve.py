"""
Tests for indiaset.resolve
"""

from indiaset import resolve_district


def test_exact_match():
    result = resolve_district("Pune")
    assert result is not None
    assert result["district_name"] == "Pune"
    assert result["lgd_code"] == 490


def test_census_lgd_spelling_mismatch():
    # census says Badgam, LGD says Budgam
    result = resolve_district("Badgam")
    assert result is not None
    assert result["district_name"] == "Budgam"


def test_historical_rename():
    result = resolve_district("Bombay")
    assert result is not None
    assert result["district_name"] == "Mumbai"

    result = resolve_district("Madras")
    assert result is not None
    assert result["district_name"] == "Chennai"


def test_case_insensitive():
    result = resolve_district("poona")
    assert result is not None
    assert result["district_name"] == "Pune"


def test_garbage_input_returns_none():
    result = resolve_district("xyzrandom123")
    assert result is None


def test_returns_expected_keys():
    result = resolve_district("Pune")
    assert set(result.keys()) == {
        "district_name", "lgd_code", "state_name", "match_score"
    }