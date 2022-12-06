import pytest
from day05 import rearrange_crates, Movement, rearrange_crates_with_new_crane


@pytest.mark.parametrize("crates_stacks, movements, expected_message",
                        [
                            (
                                [["Z","N"],
                                ["M","C","D"],
                                ["P"]],
                                [
                                    Movement("move 1 from 2 to 1"),
                                    Movement("move 3 from 1 to 3"),
                                    Movement("move 2 from 2 to 1"),
                                    Movement("move 1 from 1 to 2")
                                ],
                                "CMZ"
                            )
                        ])
def test_given_stacks_and_movements_then_get_message(crates_stacks, movements, expected_message):
    assert rearrange_crates(crates_stacks, movements) == expected_message

@pytest.mark.parametrize("crates_stacks, movements, expected_message",
                        [
                            (
                                [["Z","N"],
                                ["M","C","D"],
                                ["P"]],
                                [
                                    Movement("move 1 from 2 to 1"),
                                    Movement("move 3 from 1 to 3"),
                                    Movement("move 2 from 2 to 1"),
                                    Movement("move 1 from 1 to 2")
                                ],
                                "MCD"
                            )
                        ])
def test_given_stacks_and_movements_then_get_message_with_new_crane(crates_stacks, movements, expected_message):
    assert rearrange_crates_with_new_crane(crates_stacks, movements) == expected_message

