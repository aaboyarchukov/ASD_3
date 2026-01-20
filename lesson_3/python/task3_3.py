import unittest

from task3 import ShellSort, KnuthSequence

class TestKnuthSequence(unittest.TestCase):
    def test_get_sequence(self):
        cases = [
            (0, []),
            (1, [1]),
            (2, [1]),
            (3, [1]),
            (4, [4, 1]),
            (5, [4, 1]),
            (12, [4, 1]),
            (13, [13, 4, 1]),
            (14, [13, 4, 1]),
            (40, [40, 13, 4, 1]),
            (41, [40, 13, 4, 1]),
            (120, [40, 13, 4, 1]),
            (121, [121, 40, 13, 4, 1]),
        ]

        for array_size, expected in cases:
            with self.subTest(array_size=array_size):
                got = KnuthSequence(array_size)
                self.assertEqual(
                    got, expected,
                    msg=(
                        "FAIL: KnuthSequence вернул неверную последовательность.\n"
                        f"array_size={array_size}\n"
                        f"Ожидалось: {expected}\n"
                        f"Получено:  {got}"
                    )
                )

class TestShellSort(unittest.TestCase):
    def test_shell_sort(self):
        cases = [
            ([], []),
            ([1], [1]),
            ([2, 1], [1, 2]),
            ([1, 2, 3], [1, 2, 3]),
            ([3, 2, 1], [1, 2, 3]),
            ([7, 6, 5, 4, 3, 2, 1], [1, 2, 3, 4, 5, 6, 7]),
            ([5, 1, 4, 2, 8], [1, 2, 4, 5, 8]),
            ([2, 2, 1, 3, 1, 0, 0], [0, 0, 1, 1, 2, 2, 3]),
            ([-3, 0, 2, -1, -1, 5], [-3, -1, -1, 0, 2, 5]),
            ([100, -100, 50, 0, 50], [-100, 0, 50, 50, 100]),
        ]

        for arr, expected in cases:
            with self.subTest(arr=arr):
                a = arr.copy()
                ShellSort(a)

                self.assertEqual(
                    a, expected,
                    msg=(
                        "FAIL: ShellSort неверно отсортировал массив.\n"
                        f"Вход:      {arr}\n"
                        f"Ожидалось: {expected}\n"
                        f"Получено:  {a}"
                    )
                )

if __name__ == "__main__":
    unittest.main()