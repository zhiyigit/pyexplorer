from array import array

from algorithms.arrays.array_inversion_counter import count_inverses_in_array


def test_count_inversions_zero():
    sorted_array = array('i', [1, 2, 3, 4, 5, 6, 7, 8])
    assert count_inverses_in_array(sorted_array) == 0


def test_count_inversions_max_size_3():
    full_inversion = array('i', [3, 2, 1])
    assert count_inverses_in_array(full_inversion) == 3


def test_count_inversions_max_size_4():
    full_inversion = array('i', [4, 3, 2, 1])
    assert count_inverses_in_array(full_inversion) == 6


def test_count_inversion_mixed_even_length():
    inversion_mixed = array('i', [1, 6, 2, 4, 5, 3])
    assert count_inverses_in_array(inversion_mixed) == 6


def test_count_inversion_mixed_odd_length():
    inversion_mixed = array('i', [1, 7, 6, 2, 9, 4, 8,  5, 3])
    assert count_inverses_in_array(inversion_mixed) == 17