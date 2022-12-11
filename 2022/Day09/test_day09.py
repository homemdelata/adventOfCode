import pytest
from day09 import tail_postitions

@pytest.mark.parametrize("motions, expected_tail_positions",
                        [
("""
R 4
U 4
L 3
D 1
R 4
D 1
L 5
R 2
""", 13)
                        ])
def test_motions_then_tail_positions(motions, expected_tail_positions):
    assert tail_postitions(motions) == expected_tail_positions


