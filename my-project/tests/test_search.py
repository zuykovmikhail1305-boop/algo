import pytest
from my_project.algoritms.search import binary_search

ARR = [-10, -3, 0, 2, 5, 8, 13, 21, 34]


@pytest.mark.parametrize("value", ARR)
def test_finds_every_element(value):
    assert binary_search(ARR, value) == value


@pytest.mark.parametrize("value", [-100, -4, 1, 9, 22, 100])
def test_missing_value_returns_false(value):
    assert binary_search(ARR, value) is False


def test_empty_array():
    assert binary_search([], 1) is False


def test_single_element():
    assert binary_search([7], 7) == 7
    assert binary_search([7], 3) is False


@pytest.mark.parametrize("n", [2, 3, 10, 100, 1000])
def test_all_sizes(n):
    arr = list(range(0, 2 * n, 2))
    for v in arr:
        assert binary_search(arr, v) == v
    for v in range(-1, 2 * n + 1, 2):
        assert binary_search(arr, v) is False
