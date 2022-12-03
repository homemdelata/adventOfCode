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


def jokenpo_score(opponent, you):
    opponent_hand = opponent_hand_converter(opponent)
    your_hand = your_hand_converter(you)
    result = jokenpo_result.lost
    if opponent_hand == your_hand:
        result = jokenpo_result.draw
    elif opponent_hand == jokenpo_hand.scissors and your_hand == jokenpo_hand.rock:
        result = jokenpo_result.win
    elif opponent_hand == jokenpo_hand.rock and your_hand == jokenpo_hand.scissors:
        result = jokenpo_result.lost
    elif opponent_hand.value < your_hand.value:
        result = jokenpo_result.win
    return result.value + your_hand.value


def total_score(strategy):
    return sum([jokenpo_score(i[0], i[1]) for i in strategy])

def day02_part1(input_name):
    with open(os.path.join(sys.path[0], input_name), 'r') as file:
        input = file.read()
        strategy = [game.split(" ") for game in input.strip().split("\n")]
        score = total_score(strategy)
    print("Day 02 - Part 1 - {}: {}".format(input_name, score))
    
day02_part1("test.txt")
day02_part1("input.txt")