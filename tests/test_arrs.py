from utils import arrs


def test_get():
    assert arrs.get([1, 2, 3], 1, "test") == 2
    assert arrs.get([], 0, "test") == "test"
    assert arrs.get([], -1, "test") == "test"
    assert arrs.get([1, 2, 3], 3) is None


def test_slice():
    assert type(arrs.my_slice([1, 2, 3, 4], 1, 3)) == list
    assert arrs.my_slice([]) == []
    assert arrs.my_slice([1, 2, 3, 4], 1, 3) == [2, 3]
    assert arrs.my_slice([1, 2, 3], 1) == [2, 3]
    assert arrs.my_slice([1, 2, 3]) == [1, 2, 3]
    assert arrs.my_slice([1, 2, 3, 4], -3, -1) == [2, 3]
    assert arrs.my_slice([1, 2, 3, 4], 1, -1) == [2, 3]
    assert arrs.my_slice([1, 2, 3, 4], 3, 1) == []
    assert arrs.my_slice([1, 2, 3, 4], -5, -1) == [1, 2, 3]
