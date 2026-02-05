import unittest
from task6 import QuickSortTailOptimization

class TestQuickSortTailOptimization(unittest.TestCase):
    def test_quick_sort(self):
        cases = [
            ("empty array", [], []),
            ("one element", [1], [1]),
            ("three elements", [3, 1, 2], [1, 2, 3]),
            ("even length", [8, 6, 4, 2], [2, 4, 6, 8]),
            ("odd length", [9, 7, 5, 3, 1], [1, 3, 5, 7, 9]),
            ("many elements mixed", [7, 5, 6, 4, 3, 1, 2], [1, 2, 3, 4, 5, 6, 7]),
            ("two elements sorted", [1, 2], [1, 2]),
            ("two elements reversed", [2, 1], [1, 2]),
            ("negative numbers", [-5, -1, -3, -2], [-5, -3, -2, -1]),
            ("mixed positive negative", [3, -1, 2, -5, 0], [-5, -1, 0, 2, 3]),
            ("already sorted", [1, 2, 3, 4, 5, 6], [1, 2, 3, 4, 5, 6]),
            ("reverse sorted", [6, 5, 4, 3, 2, 1], [1, 2, 3, 4, 5, 6]),
            ("large numbers", [1000, 500, 750, 250, 100], [100, 250, 500, 750, 1000])
        ]

        for name, get, want  in cases:
            with self.subTest(name=name, get=get, want=want):
                size = len(get)
                left, right = 0, size - 1
                QuickSortTailOptimization(get, left, right)
                self.assertEqual(
                    get, want,
                    msg=(
                        "FAIL: QuickSort неверно отсортировал массив.\n"
                        f"Ожидалось: {want}\n"
                        f"Получено:  {get}"
                    )
                )

if __name__ == "__main__":
    unittest.main()