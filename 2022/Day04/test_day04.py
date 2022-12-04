import pytest
from day04 import fully_contains, count_fully_contained, overlaps, count_overlaps


@pytest.mark.parametrize("sections_pair, expected_fully_contains",
                         [
                             ([[2,4], [6,8]], False),
                             ([[2,3], [4,5]], False),
                             ([[5,7], [7,9]], False),
                             ([[2,8], [3,7]], True),
                             ([[6,6], [4,6]], True),
                             ([[2,6], [4,8]], False)
                         ])
def test_given_two_sections_groups_then_check_if_fully_contains(sections_pair, expected_fully_contains):
    assert fully_contains(sections_pair) == expected_fully_contains


@pytest.mark.parametrize("pairs_list, expected_count",
                         [
                             (
                                 [
                                    [[2,4], [6,8]],
                                    [[2,3], [4,5]],
                                    [[5,7], [7,9]],
                                    [[2,8], [3,7]],
                                    [[6,6], [4,6]],
                                    [[2,6], [4,8]]
                                 ]
                                 , 2)
                         ])
def test_given_all_pairs_then_count_fully_contained(pairs_list, expected_count):
    assert count_fully_contained(pairs_list) == expected_count

@pytest.mark.parametrize("sections_pair, expected_overlaps",
                         [
                             ([[2,4], [6,8]], False),
                             ([[2,3], [4,5]], False),
                             ([[5,7], [7,9]], True),
                             ([[2,8], [3,7]], True),
                             ([[6,6], [4,6]], True),
                             ([[2,6], [4,8]], True),
                             ([[1,5], [7,8]], False),
                             ([[1,7], [7,8]], True),
                             ([[1,8], [7,10]], True),
                             ([[1,10], [7,10]], True),
                             ([[1,12], [7,10]], True),
                             ([[7,10], [7,10]], True),
                             ([[5,8], [3,10]], True),
                             ([[5,10], [3,10]], True),
                             ([[5,12], [3,10]], True),
                             ([[10,12], [3,10]], True),
                             ([[11,15], [3,10]], False)
                         ])
def test_given_two_sections_groups_then_check_if_expected_overlaps(sections_pair, expected_overlaps):
    assert overlaps(sections_pair) == expected_overlaps

@pytest.mark.parametrize("pairs_list, expected_count",
                         [
                             (
                                 [
                                    [[2,4], [6,8]],
                                    [[2,3], [4,5]],
                                    [[5,7], [7,9]],
                                    [[2,8], [3,7]],
                                    [[6,6], [4,6]],
                                    [[2,6], [4,8]]
                                 ]
                                 , 4)
                         ])
def test_given_all_pairs_then_count_overlaps(pairs_list, expected_count):
    assert count_overlaps(pairs_list) == expected_count
