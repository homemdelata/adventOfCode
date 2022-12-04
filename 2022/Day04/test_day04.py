import pytest
from day04 import fully_contains, count_fully_contained


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
    assert fully_contains(sections_pair[0], sections_pair[1]) == expected_fully_contains


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
