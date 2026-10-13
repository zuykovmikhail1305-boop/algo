import random

import pytest
from my_project.algoritms.sort import (
    buble_sort,
    choose_sort,
    hairbrush_sort,
    insert_sort,
    quick_sort,
)

SORTS = [buble_sort, hairbrush_sort, choose_sort, insert_sort, quick_sort]

CASES = [
    [],
    [1],
    [2, 1],
    [1, 2, 3, 4, 5],
    [5, 4, 3, 2, 1],
    [3, 1, 2],
    [2, 2, 1],
    [7, 7, 7, 7],
    [-5, 23, 7, 5, 1, 1, 3, -12, -29, 21, 54, 35, 0],
    [0.5, -1.5, 3.25, 0.0],
    [8, 5, 8, 4, 9, 5, 7, 3, 9, 3],
]


@pytest.mark.parametrize("sort", SORTS)
@pytest.mark.parametrize("arr", CASES, ids=repr)
def test_sorts_like_builtin(sort, arr):
    assert sort(list(arr)) == sorted(arr)


@pytest.mark.parametrize("sort", SORTS)
def test_random_arrays(sort):
    rng = random.Random(42)
    for _ in range(300):
        arr = [rng.randint(-50, 50) for _ in range(rng.randint(0, 40))]
        assert sort(list(arr)) == sorted(arr), arr


@pytest.mark.parametrize("sort", SORTS)
def test_keeps_all_elements(sort):
    arr = [3, 1, 3, 2, 1, 3]
    assert len(sort(list(arr))) == len(arr)


@pytest.mark.parametrize("sort", [buble_sort, hairbrush_sort, choose_sort, insert_sort])
def test_in_place_sorts_modify_input(sort):
    arr = [3, 1, 2]
    result = sort(arr)
    assert result is arr
    assert arr == [1, 2, 3]
