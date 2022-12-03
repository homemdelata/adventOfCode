from enum import Enum
import os
import sys


class jokenpo_hand(Enum):
    rock = 1
    paper = 2
    scissors = 3


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


def expected_end_converter(expected_end):
    match expected_end:
        case "X":
            return jokenpo_result.lost
        case "Y":
            return jokenpo_result.draw
        case "Z":
            return jokenpo_result.win
        case _:
            raise Exception("End not mapped")


def get_winning_hand(opponent_hand):
    if opponent_hand == jokenpo_hand.scissors:
        return jokenpo_hand.rock
    else:
        return jokenpo_hand(opponent_hand.value + 1)


def get_losing_hand(opponent_hand):
    if opponent_hand == jokenpo_hand.rock:
        return jokenpo_hand.scissors
    else:
        return jokenpo_hand(opponent_hand.value - 1)


def jokenpo_score(opponent, you):
    opponent_hand = opponent_hand_converter(opponent)
    your_hand = your_hand_converter(you)
    result = jokenpo_result.lost
    if opponent_hand == your_hand:
        result = jokenpo_result.draw
    elif opponent_hand == jokenpo_hand.scissors and your_hand == jokenpo_hand.rock or opponent_hand.value == your_hand.value - 1:
        result = jokenpo_result.win
    return result.value + your_hand.value


def total_score(strategy):
    return sum([jokenpo_score(i[0], i[1]) for i in strategy])


def correct_jokenpo_score(opponent, expected_end):
    opponent_hand = opponent_hand_converter(opponent)
    expected_end_result = expected_end_converter(expected_end)
    match expected_end_result:
        case jokenpo_result.lost:
            your_hand = get_losing_hand(opponent_hand)
        case jokenpo_result.draw:
            your_hand = opponent_hand
        case jokenpo_result.win:
            your_hand = get_winning_hand(opponent_hand)
        case _:
            raise Exception("Result not mapped")
    return expected_end_result.value + your_hand.value


def correct_total_score(strategy):
    return sum([correct_jokenpo_score(i[0], i[1]) for i in strategy])


def day02_part1(input_name):
    with open(os.path.join(sys.path[0], input_name), 'r') as file:
        input = file.read()
        strategy = [game.split(" ") for game in input.strip().split("\n")]
        score = total_score(strategy)
    print("Day 02 - Part 1 - {}: {}".format(input_name, score))


def day02_part2(input_name):
    with open(os.path.join(sys.path[0], input_name), 'r') as file:
        input = file.read()
        strategy = [game.split(" ") for game in input.strip().split("\n")]
        score = correct_total_score(strategy)
    print("Day 02 - Part 2 - {}: {}".format(input_name, score))


if __name__ == "__main__":
    day02_part1("test.txt")
    day02_part1("input.txt")

    day02_part2("test.txt")
    day02_part2("input.txt")
