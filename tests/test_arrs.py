from utils import arrs
from utils.arrs import get, my_slice

def test_get_with_valid_index():
    assert get([1, 2, 3], 1) == 2


def test_my_slice_with_none_start():
    assert my_slice([1, 2, 3, 4, 5], None, 3) == [1, 2, 3]

def test_get_with_out_of_range_index():
    assert get([1, 2, 3], 10) is None

def test_my_slice_with_valid_range():
    assert my_slice([1, 2, 3, 4, 5], 1, 4) == [2, 3, 4]

def test_my_slice_with_negative_start():
    assert my_slice([1, 2, 3, 4, 5], -3) == [3, 4, 5]

def test_my_slice_with_negative_end():
    assert my_slice([1, 2, 3, 4, 5], 1, -1) == [2, 3, 4]

def test_my_slice_with_out_of_range_start():
    assert my_slice([1, 2, 3, 4, 5], -10) == [1, 2, 3, 4, 5]

def test_my_slice_with_out_of_range_end():
    assert my_slice([1, 2, 3, 4, 5], 10) == []

def test_my_slice_with_empty_list():
    assert my_slice([]) == []