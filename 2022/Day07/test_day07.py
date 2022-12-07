import pytest
from day07 import get_sum_directories_under_100000, get_size_of_directory_to_delete


@pytest.mark.parametrize("input, expected_result",
                        [
("""$ cd /
$ ls
dir a
14848514 b.txt
8504156 c.dat
dir d
$ cd a
$ ls
dir e
29116 f
2557 g
62596 h.lst
$ cd e
$ ls
584 i
$ cd ..
$ cd ..
$ cd d
$ ls
4060174 j
8033020 d.log
5626152 d.ext
7214296 k""", 95437)
                        ])
def test_given_input_then_return_sum(input, expected_result):
    assert get_sum_directories_under_100000(input) == expected_result


@pytest.mark.parametrize("input, expected_result",
                        [
("""$ cd /
$ ls
dir a
14848514 b.txt
8504156 c.dat
dir d
$ cd a
$ ls
dir e
29116 f
2557 g
62596 h.lst
$ cd e
$ ls
584 i
$ cd ..
$ cd ..
$ cd d
$ ls
4060174 j
8033020 d.log
5626152 d.ext
7214296 k""", 24933642)
                        ])
def test_given_input_then_return_min(input, expected_result):
    assert get_size_of_directory_to_delete(input) == expected_result
