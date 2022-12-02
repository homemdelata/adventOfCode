from enum import Enum


class jokenpo_hand(Enum):
    rock = "1"
    paper = "2"
    scissors = "3"


class jokenpo_result(Enum):
    lost = 0
    draw = 3
    win = 6


def opponent_hand_converter(opponent_hand):
    match opponent_hand:
        case "A":
            return jokenpo_hand.rock
        case "B":
            return jokenpo_hand.paper
        case "C":
            return jokenpo_hand.scissors
        case _:
            raise Exception("Hand not mapped")


def your_hand_converter(your_hand):
    match your_hand:
        case "X":
            return jokenpo_hand.rock
        case "Y":
            return jokenpo_hand.paper
        case "Z":
            return jokenpo_hand.scissors
        case _:
            raise Exception("Hand not mapped")


def jokenpo_score(opponent, you):
    pass


def total_score(strategy):
    pass
