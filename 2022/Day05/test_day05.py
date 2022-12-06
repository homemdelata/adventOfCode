import pytest
from day05 import rearrange_crates


@pytest.mark.parametrize("crates_stacks, movements, expected_message",
                        [
                            (
                                [["Z","N"],
                                ["M","C","P"],
                                ["P"]],
                                [
                                    "move 1 from 2 to 1",
                                    "move 3 from 1 to 3",
                                    "move 2 from 2 to 1",
                                    "move 1 from 1 to 2"
                                ],
                                "CMZ"
                            )
                        ])
def test_given_stacks_and_movements_then_get_message(crates_stacks, movements, expected_message):
    assert rearrange_crates(crates_stacks, movements) == expected_message

