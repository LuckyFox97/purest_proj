from utils import arrs
from utils.arrs import get, my_slice

def test_get():
    assert arrs.get([1, 2, 3], 1, "test") == 2
    assert arrs.get([], 0, "test") == "test"


def test_slice():
    assert arrs.my_slice([1, 2, 3, 4], 1, 3) == [2, 3]
    assert arrs.my_slice([1, 2, 3], 1) == [2, 3]

def test_get_existing_index():
    array = [1, 2, 3, 4, 5]
    assert get(array, 2) == 3

def test_get_non_existing_index():
    array = [1, 2, 3]
    assert get(array, 5, 'default') == 'default'

def test_my_slice_full_range():
    coll = [1, 2, 3, 4, 5]
    assert my_slice(coll) == coll

def test_my_slice_with_start():
    coll = [1, 2, 3, 4, 5]
    assert my_slice(coll, 1) == [2, 3, 4, 5]

def test_my_slice_with_end():
    coll = [1, 2, 3, 4, 5]
    assert my_slice(coll, end=3) == [1, 2, 3]
