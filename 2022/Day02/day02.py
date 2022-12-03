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
    

def jokenpo_score(opponent, you):
    opponent_hand = opponent_hand_converter(opponent)
    your_hand = your_hand_converter(you)
    result = jokenpo_result.lost
    if opponent_hand == your_hand:
        result = jokenpo_result.draw
    elif opponent_hand == jokenpo_hand.scissors and your_hand == jokenpo_hand.rock or opponent_hand.value == your_hand.value - 1:
        result = jokenpo_result.win
    return result.value + your_hand.value

def correct_jokenpo_score(opponent, expected_end):
    pass


def total_score(strategy):
    return sum([jokenpo_score(i[0], i[1]) for i in strategy])

def correct_total_score(strategy):
    pass

def day02_part1(input_name):
    with open(os.path.join(sys.path[0], input_name), 'r') as file:
        input = file.read()
        strategy = [game.split(" ") for game in input.strip().split("\n")]
        score = total_score(strategy)
    print("Day 02 - Part 1 - {}: {}".format(input_name, score))
    
day02_part1("test.txt")
day02_part1("input.txt")