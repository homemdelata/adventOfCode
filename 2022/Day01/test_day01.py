import pytest
from day01 import parse_elves, calculate_total_calories


@pytest.mark.parametrize("test_input, expected",
                         [(
                             """
1000
2000
3000

4000

5000
6000

7000
8000
9000

10000
                                """,
                             [[1000, 2000, 3000],
                              [4000],
                                 [5000, 6000],
                                 [7000, 8000, 9000],
                                 [10000]])])
def test_given_input_parse_elves(test_input, expected):
    assert parse_elves(test_input) == expected


@pytest.mark.parametrize("test_elf, expected_sum",
                         [
                             ([1000, 2000, 3000], 6000),
                             ([4000], 4000),
                             ([5000, 6000], 11000),
                             ([7000, 8000, 9000], 24000),
                             ([10000], 10000)
                         ])
def test_given_elf_then_return_total_calories(test_elf, expected_sum):
    assert calculate_total_calories(test_elf) == expected_sum
