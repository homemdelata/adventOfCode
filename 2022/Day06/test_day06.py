import pytest
from day06 import get_starter_marker, get_starter_message


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
    
@pytest.mark.parametrize("message, expected_start",
                        [
                            ("mjqjpqmgbljsphdztnvjfqwrcgsmlb", 19),
                            ("bvwbjplbgvbhsrlpgdmjqwftvncz", 23),
                            ("nppdvjthqldpwncqszvftbrmjlhg", 23),
                            ("nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg", 29),
                            ("zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw", 26)
                        ])
def test_given_message_then_return_starter_message(message, expected_start):
    assert get_starter_message(message) == expected_start