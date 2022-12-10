import pytest
from day08 import count_visible_trees


@pytest.mark.parametrize("trees_map, expected_visible_count",
                        [
("""
30373
25512
65332
33549
35390
""", 21)
                        ])
def test_given_trees_map_then_count_visible(trees_map, expected_visible_count):
    assert count_visible_trees(trees_map) == expected_visible_count
