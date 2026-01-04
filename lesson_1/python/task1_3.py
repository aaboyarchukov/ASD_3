import unittest

from task1 import SelectionSortStep


class TestSelectionSortStep(unittest.TestCase):

    def test_one_step_sorting(self):
        cases = [
            ([3, 1, 2], 0, [1, 3, 2]),
            ([3, 1, 2], 1, [3, 1, 2]),
            ([5, 4, 3, 2, 1], 0, [1, 4, 3, 2, 5]),
            ([2, 2, 1], 0, [1, 2, 2]),
            ([1, 2, 3], 0, [1, 2, 3]),
        ]

        for arr, i, expected in cases:
            with self.subTest(arr=arr, i=i):
                arr_copy = arr.copy()
                SelectionSortStep(arr_copy, i)
                
                self.assertNotEqual(
                    arr, arr_copy,
                    msg=(
                        f"FAIL: Один шаг сортировки (i={i}) выполнен неверно. Данные идентичны\n"
                        f"Вход:      {arr}\n"
                        f"Получено:  {arr_copy}"
                    )
                )

                self.assertEqual(
                    arr_copy, expected,
                    msg=(
                        f"FAIL: Один шаг сортировки (i={i}) выполнен неверно.\n"
                        f"Вход:      {arr}\n"
                        f"Ожидалось: {expected}\n"
                        f"Получено:  {arr_copy}"
                    )
                )

    def test_n_steps_sorting(self):
        cases = [
            ([3, 1, 2, 5, 4], 2),
            ([5, 4, 3, 2, 1], 3),
            ([2, 2, 1, 3, 1], 4),
            ([1, 2, 3, 4], 1),
        ]

        for arr, k in cases:
            with self.subTest(arr=arr, k=k):
                arr_copy = arr.copy()
                expected_prefix = sorted(arr)[:k] # trusted

                for i in range(k):
                    SelectionSortStep(arr_copy, i)

                self.assertEqual(
                    arr_copy[:k], expected_prefix,
                    msg=(
                        f"FAIL: После {k} шагов первые {k} элементов неверны.\n"
                        f"Вход:                 {arr}\n"
                        f"Ожидался префикс:     {expected_prefix}\n"
                        f"Полученный префикс:   {arr_copy[:k]}\n"
                        f"Текущее состояние arr_copy:  {arr_copy}"
                    )
                )
                
                self.assertCountEqual(
                    arr_copy, arr,
                    msg=(
                        f"FAIL: После {k} шагов изменилось содержимое массива (потеря/дублирование элементов).\n"
                        f"Вход:     {arr}\n"
                        f"Получено: {arr_copy}"
                    )
                )

                self.assertNotEqual(
                    arr, arr_copy,
                    msg=(
                        f"FAIL: Один шаг сортировки (i={i}) выполнен неверно. Данные идентичны\n"
                        f"Вход:      {arr}\n"
                        f"Получено:  {arr_copy}"
                    )
                )

    def test_full_array_sorting(self):
        cases = [
            [],
            [1],
            [2, 1],
            [3, 1, 2],
            [5, 4, 3, 2, 1],
            [2, 2, 1, 3, 1],
            [1, 2, 3, 4, 5],
        ]

        for arr in cases:
            with self.subTest(arr=arr):
                arr_copy = arr.copy()
                for i in range(max(0, len(arr_copy) - 1)):
                    SelectionSortStep(arr_copy, i)

                    self.assertEqual(
                        arr_copy, sorted(arr),
                        msg=(
                            "FAIL: Полная сортировка массива шагами selection sort дала неверный результат.\n"
                            f"Вход:      {arr}\n"
                            f"Ожидалось: {sorted(arr)}\n"
                            f"Получено:  {arr_copy}"
                        )
                    )


if __name__ == "__main__":
    unittest.main()