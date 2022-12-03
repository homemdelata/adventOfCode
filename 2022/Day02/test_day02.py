import pytest
from day02 import jokenpo_score, total_score


@pytest.mark.parametrize("opponent_hand, your_hand, expected_result",
                         [
                             ("A", "X", 4),
                             ("A", "Y", 8),
                             ("A", "Z", 3),
                             ("B", "X", 1),
                             ("B", "Y", 5),
                             ("B", "Z", 9),
                             ("C", "X", 7),
                             ("C", "Y", 2),
                             ("C", "Z", 6)
                            
                         ])
def test_given_hands_then_score(opponent_hand, your_hand, expected_result):
    assert jokenpo_score(opponent_hand, your_hand) == expected_result


@pytest.mark.parametrize("strategy, expected_total_score",
                         [
                             ([["A", "Y"], ["B", "X"], ["C", "Z"]], 15)
                         ])
def test_given_strategy_then_result(strategy, expected_total_score):
    assert total_score(strategy) == expected_total_score
