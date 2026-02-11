import unittest
from task7 import KthOrderStatisticsStep

class TestKthOrderStatisticsStep(unittest.TestCase):
    def test_quick_sort(self):
        cases = [
            ("empty array", [], 0, []),
            ("one element", [1], 1, [0, 0]),
            ("three elements", [3, 1, 2], 1, [0, 2]),
            ("even length", [8, 6, 4, 2], 2, [2, 3]),
        ]

        for name, array, k, result  in cases:
            with self.subTest(name=name, array=array, k=k, result=result):
                size = len(array)
                left, right = 0, size - 1
                bounds = KthOrderStatisticsStep(array, left, right, k)
                self.assertEqual(
                    bounds, result,
                    msg=(
                        f"FAIL: KthOrderStatisticsStep неверно вычислил границы для {k}-ой статистики.\n"
                        f"Ожидалось: {bounds}\n"
                        f"Получено:  {result}"
                    )
                )

if __name__ == "__main__":
    unittest.main()