import pytest
from day06 import get_starter_marker


@pytest.mark.parametrize("message, expected_start",
                        [
                            ("mjqjpqmgbljsphdztnvjfqwrcgsmlb", 7),
                            ("bvwbjplbgvbhsrlpgdmjqwftvncz", 5),
                            ("nppdvjthqldpwncqszvftbrmjlhg", 6),
                            ("nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg", 10),
                            ("zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw", 11)
                        ])
def test_given_message_then_return_starter_marker(message, expected_start):
    assert get_starter_marker(message) == expected_start