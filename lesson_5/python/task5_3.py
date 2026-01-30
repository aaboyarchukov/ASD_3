import unittest
from task5 import QuickSort

class TestBuildArrayChunk(unittest.TestCase):
    def test_quick_sort(self):
        cases = [
            ("empty array", [], []),
            ("one element", [1], [1]),
            ("many elements 1", [3, 1, 2], [1, 2, 3]),
            ("many elements 2", [40, 13, 4, 1], [1, 4, 13, 40]),
            ("many elements 3", [7, 5, 6, 4, 3, 1, 2], [1, 2, 3, 4, 5, 6, 7]),
            ("many elements 4", [121, 40, 13, 4, 1], [1, 4, 13, 40, 121]),
        ]

        for name, get, want  in cases:
            with self.subTest(name=name, get=get, want=want):
                size = len(get)
                left, right = 0, size - 1
                QuickSort(get, left, right)
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