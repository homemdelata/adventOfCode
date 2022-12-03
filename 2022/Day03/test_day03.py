import pytest
from day03 import get_duplicate_item, get_item_priority, sum_priorities, group_badge, sum_group_priorities


@pytest.mark.parametrize("rucksack, duplicate_item",
                         [
                             ("vJrwpWtwJgWrhcsFMMfFFhFp", "p"),
                             ("jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL", "L"),
                             ("PmmdzqPrVvPwwTWBwg", "P"),
                             ("wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn", "v"),
                             ("ttgJtRGJQctTZtZT", "t"),
                             ("CrZsJsPPZsGzwwsLwLmpwMDw", "s")
                         ])
def test_given_rucksack_then_return_duplicate_item(rucksack, duplicate_item):
    assert get_duplicate_item(rucksack) == duplicate_item


@pytest.mark.parametrize("item, expected_priority",
                         [
                             ("p", 16),
                             ("L", 38),
                             ("P", 42),
                             ("v", 22),
                             ("t", 20),
                             ("s", 19)
                         ])
def test_given_strategy_then_result(item, expected_priority):
    assert get_item_priority(item) == expected_priority


@pytest.mark.parametrize("rucksack_list, expected_total",
                         [(
                             ["vJrwpWtwJgWrhcsFMMfFFhFp",
                              "jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL",
                              "PmmdzqPrVvPwwTWBwg",
                              "wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn",
                              "ttgJtRGJQctTZtZT",
                              "CrZsJsPPZsGzwwsLwLmpwMDw"], 157
                         )])
def test_given_rucksack_list_then_get_total_priorities(rucksack_list, expected_total):
    assert sum_priorities(rucksack_list) == expected_total


@pytest.mark.parametrize("elves_groups, expected_badge",
                         [(
                             ["vJrwpWtwJgWrhcsFMMfFFhFp",
                              "jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL",
                              "PmmdzqPrVvPwwTWBwg"],
                             "r"),
                          (
                              
                              ["wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn",
                              "ttgJtRGJQctTZtZT",
                              "CrZsJsPPZsGzwwsLwLmpwMDw"],
                              "Z"
                           )])
def test_given_elves_groups_then_find_badge(elves_groups, expected_badge):
    assert group_badge(elves_groups) == expected_badge

@pytest.mark.parametrize("rucksack_list, expected_total",
                         [(
                             ["vJrwpWtwJgWrhcsFMMfFFhFp",
                              "jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL",
                              "PmmdzqPrVvPwwTWBwg",
                              "wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn",
                              "ttgJtRGJQctTZtZT",
                              "CrZsJsPPZsGzwwsLwLmpwMDw"], 70
                         )])
def test_given_rucksack_list_then_get_total_priorities(rucksack_list, expected_total):
    assert sum_group_priorities(rucksack_list) == expected_total
