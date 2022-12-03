import pytest
from day02 import jokenpo_score, total_score, correct_jokenpo_score, correct_total_score


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

@pytest.mark.parametrize("opponent_hand, expected_end, expected_score",
                         [
                             ("A", "X", 3),
                             ("A", "Y", 4),
                             ("A", "Z", 8),
                             ("B", "X", 1),
                             ("B", "Y", 5),
                             ("B", "Z", 9),
                             ("C", "X", 2),
                             ("C", "Y", 6),
                             ("C", "Z", 7)
                            
                         ])
def test_given_opponent_hand_and_expected_end_then_calculate_score(opponent_hand, expected_end, expected_score):
    assert correct_jokenpo_score(opponent_hand, expected_end) == expected_score
    
@pytest.mark.parametrize("strategy, expected_total_score",
                         [
                             ([["A", "Y"], ["B", "X"], ["C", "Z"]], 12)
                         ])
def test_given_new_strategy_then_return_correct_result(strategy, expected_total_score):
    assert correct_total_score(strategy) == expected_total_score
