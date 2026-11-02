import pytest

from maths.average_median import median


def test_median_empty_list_raises_value_error() -> None:
    with pytest.raises(ValueError, match="at least one number"):
        median([])


def test_median_odd_length_list() -> None:
    assert median([3, 1, 2]) == 2


def test_median_even_length_list() -> None:
    assert median([4, 1, 3, 2]) == 2.5
