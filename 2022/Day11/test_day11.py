import pytest
from day11 import Monkey, run_rounds

monkeys_list = [
                    Monkey([79,98], "new = old * 19", "divisible by 23", 2, 3),
                    Monkey([54, 65, 75, 74], "new = old + 6", "divisible by 19", 2, 0),
                    Monkey([79, 60, 97], "new = old * old", "divisible by 13", 1, 3),
                    Monkey([74], "new = old + 3", "divisible by 17", 0, 1)
                ]

@pytest.mark.parametrize("monkeys, round, expected_holding_items",
                        [
                            (monkeys_list, 1, [
                                Monkey([20, 23, 27, 26], "new = old * 19", "divisible by 23", 2, 3),
                                Monkey([2080, 25, 167, 207, 401, 1046], "new = old + 6", "divisible by 19", 2, 0),
                                Monkey([], "new = old * old", "divisible by 13", 1, 3),
                                Monkey([], "new = old + 3", "divisible by 17", 0, 1)
                                ]),
                            (monkeys_list, 2, [
                                Monkey([695, 10, 71, 135, 350], "new = old * 19", "divisible by 23", 2, 3),
                                Monkey([43, 49, 58, 55, 362], "new = old + 6", "divisible by 19", 2, 0),
                                Monkey([], "new = old * old", "divisible by 13", 1, 3),
                                Monkey([], "new = old + 3", "divisible by 17", 0, 1)
                                ]),
                            (monkeys_list, 3, [
                                Monkey([16, 18, 21, 20, 122], "new = old * 19", "divisible by 23", 2, 3),
                                Monkey([1468, 22, 150, 286, 739], "new = old + 6", "divisible by 19", 2, 0),
                                Monkey([], "new = old * old", "divisible by 13", 1, 3),
                                Monkey([], "new = old + 3", "divisible by 17", 0, 1)
                                ]),
                            (monkeys_list, 4, [
                                Monkey([491, 9, 52, 97, 248, 34], "new = old * 19", "divisible by 23", 2, 3),
                                Monkey([39, 45, 43, 258], "new = old + 6", "divisible by 19", 2, 0),
                                Monkey([], "new = old * old", "divisible by 13", 1, 3),
                                Monkey([], "new = old + 3", "divisible by 17", 0, 1)
                                ]),
                            (monkeys_list, 5, [
                                Monkey([15, 17, 16, 88, 1037], "new = old * 19", "divisible by 23", 2, 3),
                                Monkey([20, 110, 205, 524, 72], "new = old + 6", "divisible by 19", 2, 0),
                                Monkey([], "new = old * old", "divisible by 13", 1, 3),
                                Monkey([], "new = old + 3", "divisible by 17", 0, 1)
                                ]),
                            (monkeys_list, 6, [
                                Monkey([8, 70, 176, 26, 34], "new = old * 19", "divisible by 23", 2, 3),
                                Monkey([481, 32, 36, 186, 2190], "new = old + 6", "divisible by 19", 2, 0),
                                Monkey([], "new = old * old", "divisible by 13", 1, 3),
                                Monkey([], "new = old + 3", "divisible by 17", 0, 1)
                                ]),
                            (monkeys_list, 7, [
                                Monkey([162, 12, 14, 64, 732, 17], "new = old * 19", "divisible by 23", 2, 3),
                                Monkey([148, 372, 55, 72], "new = old + 6", "divisible by 19", 2, 0),
                                Monkey([], "new = old * old", "divisible by 13", 1, 3),
                                Monkey([], "new = old + 3", "divisible by 17", 0, 1)
                                ]),
                            (monkeys_list, 8, [
                                Monkey([51, 126, 20, 26, 136], "new = old * 19", "divisible by 23", 2, 3),
                                Monkey([343, 26, 30, 1546, 36], "new = old + 6", "divisible by 19", 2, 0),
                                Monkey([], "new = old * old", "divisible by 13", 1, 3),
                                Monkey([], "new = old + 3", "divisible by 17", 0, 1)
                                ]),
                            (monkeys_list, 9, [
                                Monkey([116, 10, 12, 517, 14], "new = old * 19", "divisible by 23", 2, 3),
                                Monkey([108, 267, 43, 55, 288], "new = old + 6", "divisible by 19", 2, 0),
                                Monkey([], "new = old * old", "divisible by 13", 1, 3),
                                Monkey([], "new = old + 3", "divisible by 17", 0, 1)
                                ]),
                            (monkeys_list, 10, [
                                Monkey([91, 16, 20, 98], "new = old * 19", "divisible by 23", 2, 3),
                                Monkey([481, 245, 22, 26, 1092, 30], "new = old + 6", "divisible by 19", 2, 0),
                                Monkey([], "new = old * old", "divisible by 13", 1, 3),
                                Monkey([], "new = old + 3", "divisible by 17", 0, 1)
                                ]),
                            (monkeys_list, 15, [
                                Monkey([83, 44, 8, 184, 9, 20, 26, 102], "new = old * 19", "divisible by 23", 2, 3),
                                Monkey([110, 36], "new = old + 6", "divisible by 19", 2, 0),
                                Monkey([], "new = old * old", "divisible by 13", 1, 3),
                                Monkey([], "new = old + 3", "divisible by 17", 0, 1)
                                ]),
                            (monkeys_list, 20, [
                                Monkey([10, 12, 14, 26, 34], "new = old * 19", "divisible by 23", 2, 3),
                                Monkey([245, 93, 53, 199, 115], "new = old + 6", "divisible by 19", 2, 0),
                                Monkey([], "new = old * old", "divisible by 13", 1, 3),
                                Monkey([], "new = old + 3", "divisible by 17", 0, 1)
                                ]),
                            ([
                                Monkey([695, 10, 71, 135, 350], "new = old * 19", "divisible by 23", 2, 3),
                                Monkey([43, 49, 58, 55, 362], "new = old + 6", "divisible by 19", 2, 0),
                                Monkey([], "new = old * old", "divisible by 13", 1, 3),
                                Monkey([], "new = old + 3", "divisible by 17", 0, 1)
                                ], 1, [
                                Monkey([16, 18, 21, 20, 122], "new = old * 19", "divisible by 23", 2, 3),
                                Monkey([1468, 22, 150, 286, 739], "new = old + 6", "divisible by 19", 2, 0),
                                Monkey([], "new = old * old", "divisible by 13", 1, 3),
                                Monkey([], "new = old + 3", "divisible by 17", 0, 1)
                                ]),
                            ([
                                Monkey([15, 17, 16, 88, 1037], "new = old * 19", "divisible by 23", 2, 3),
                                Monkey([20, 110, 205, 524, 72], "new = old + 6", "divisible by 19", 2, 0),
                                Monkey([], "new = old * old", "divisible by 13", 1, 3),
                                Monkey([], "new = old + 3", "divisible by 17", 0, 1)
                                ], 1, [
                                Monkey([8, 70, 176, 26, 34], "new = old * 19", "divisible by 23", 2, 3),
                                Monkey([481, 32, 36, 186, 2190], "new = old + 6", "divisible by 19", 2, 0),
                                Monkey([], "new = old * old", "divisible by 13", 1, 3),
                                Monkey([], "new = old + 3", "divisible by 17", 0, 1)
                                ])
                        ])
def test_given_starting_monkeys_then_check_rounds(monkeys, round, expected_holding_items):
    list_of_monkeys = run_rounds(monkeys, round)
    for i in len(list_of_monkeys):
        assert list_of_monkeys[i] == expected_holding_items[i]