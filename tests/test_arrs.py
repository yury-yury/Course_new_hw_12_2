from typing import List
import pytest

from utils import arrs


@pytest.fixture
def coll() -> List[int]:
    arr = [x for x in range(1, 5)]
    return arr


def test_get(coll):
    assert arrs.get(coll, 1, "test") == 2
    assert arrs.get([], 0, "test") == "test"
    assert arrs.get(coll, -1, "test") == "test"
    assert arrs.get(coll, 4) is None


def test_slice(coll):
    assert type(arrs.my_slice(coll, 1, 3)) == list
    assert arrs.my_slice([]) == []
    assert arrs.my_slice(coll, 1, 3) == [2, 3]
    assert arrs.my_slice(coll, 1) == [2, 3, 4]
    assert arrs.my_slice(coll) == [1, 2, 3, 4]
    assert arrs.my_slice(coll, -3, -1) == [2, 3]
    assert arrs.my_slice(coll, 1, -1) == [2, 3]
    assert arrs.my_slice(coll, 3, 1) == []
    assert arrs.my_slice(coll, -5, -1) == [1, 2, 3]
