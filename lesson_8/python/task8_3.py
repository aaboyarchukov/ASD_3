import unittest
from task8 import MergeSort, merge

class TestMergeSort(unittest.TestCase):
    def test_merge_sort(self):
        cases = [
            ("empty array", [], []),
            ("one element", [1], [1]),
            ("three elements", [3, 1, 2], [1, 2, 3]),
            ("even length", [8, 6, 4, 2], [2, 4, 6, 8]),
        ]

        for name, array, result  in cases:
            with self.subTest(name=name, array=array, result=result):
                array = MergeSort(array)
                self.assertEqual(
                    array, result,
                    msg=(
                        f"FAIL: MergeSort неверно отсортирована последовательность.\n"
                        f"Ожидалось: {result}\n"
                        f"Получено:  {array}"
                    )
                )

class TestMerge(unittest.TestCase):
    def test_merge(self):
        cases = [
            ("empty arrays", [], [], []),
            ("one element in arrays", [1], [1], [1, 1]),
            ("two sorted arrays", [1, 2, 3], [2, 4, 6], [1, 2, 2, 3, 4, 6]),
            ("two sorted arrays with more values same length", [1, 4, 6, 8, 9], [3, 5, 8, 10, 11], [1, 3, 4, 5, 6, 8, 8, 9, 10, 11]),
            ("two sorted arrays with more values diferent length", [1, 4, 6, 8, 9], [3, 5], [1, 3, 4, 5, 6, 8, 9]),
        ]

        for name, first_array, second_array, result  in cases:
            with self.subTest(name=name, first_array=first_array, second_array=second_array, result=result):
                array = merge(first_array, second_array)
                self.assertEqual(
                    array, result,
                    msg=(
                        f"FAIL: Merge неверно объединил массивы.\n"
                        f"Ожидалось: {result}\n"
                        f"Получено:  {array}"
                    )
                )

if __name__ == "__main__":
    unittest.main()