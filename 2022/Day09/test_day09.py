import pytest
from day09 import tail_postitions, longer_rope_tail_postitions

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
""", 1),
("""
R 5
U 8
L 8
D 3
R 17
D 10
L 25
U 20
""", 36)
                        ])
def test_motions_then_tail_positions_longer_rope(motions, expected_tail_positions):
    assert longer_rope_tail_postitions(motions) == expected_tail_positions