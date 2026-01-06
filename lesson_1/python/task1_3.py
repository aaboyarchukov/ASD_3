import unittest

from task1 import SelectionSortStep, BubbleSortStep


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
                for i in range(0, len(arr_copy)):
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

class TestBubbleSortStep(unittest.TestCase):

    def test_one_step_sorting(self):
        cases = [
            # (input_array, expected_array_after_one_pass, expected_return)
            ([3, 2, 1], [2, 1, 3], False),
            ([1, 3, 2], [1, 2, 3], False),
            ([1, 2, 3], [1, 2, 3], True),
            ([2, 2, 1], [2, 1, 2], False),
            ([1], [1], True),
            ([], [], True),
            ([5, 1, 4, 2, 8], [1, 4, 2, 5, 8], False),
        ]

        for arr, expected_arr, expected_flag in cases:
            with self.subTest(arr=arr):
                arr_copy = arr.copy()
                flag = BubbleSortStep(arr_copy)

                self.assertEqual(
                    arr_copy, expected_arr,
                    msg=(
                        "FAIL: Один проход BubbleSortStep дал неверный массив.\n"
                        f"Вход:      {arr}\n"
                        f"Ожидалось: {expected_arr}\n"
                        f"Получено:  {arr_copy}"
                    )
                )
                self.assertEqual(
                    flag, expected_flag,
                    msg=(
                        "FAIL: BubbleSortStep вернул неверный флаг (True если не было обменов).\n"
                        f"Вход:           {arr}\n"
                        f"Ожидался флаг:   {expected_flag}\n"
                        f"Полученный флаг: {flag}\n"
                        f"Состояние a:     {arr_copy}"
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
                sorted_arr = sorted(arr)

                last_flag = None
                for _ in range(k):
                    last_flag = BubbleSortStep(arr_copy)

                self.assertEqual(
                    arr_copy[-k:] if k > 0 else [],
                    sorted_arr[-k:] if k > 0 else [],
                    msg=(
                        f"FAIL: После {k} проходов последние {k} элементов неверны.\n"
                        f"Вход:                 {arr}\n"
                        f"Ожидался суффикс:     {sorted_arr[-k:] if k > 0 else []}\n"
                        f"Полученный суффикс:   {arr_copy[-k:] if k > 0 else []}\n"
                        f"Текущее состояние a:  {arr_copy}\n"
                        f"Последний флаг:       {last_flag}"
                    )
                )

                self.assertCountEqual(
                    arr_copy, arr,
                    msg=(
                        f"FAIL: После {k} проходов изменилось содержимое массива (потеря/дублирование элементов).\n"
                        f"Вход:     {arr}\n"
                        f"Получено: {arr_copy}"
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

                max_passes = max(1, len(arr_copy))
                sorted_expected = sorted(arr)

                finished = False
                for pass_no in range(max_passes):
                    no_swaps = BubbleSortStep(arr_copy)
                    if no_swaps:
                        finished = True
                        break

                self.assertTrue(
                    finished,
                    msg=(
                        "FAIL: BubbleSortStep не сообщил о завершении (True) за ожидаемое число проходов.\n"
                        f"Вход:                 {arr}\n"
                        f"Ожидаемая сортировка: {sorted_expected}\n"
                        f"Текущее состояние a:  {arr_copy}\n"
                        f"Лимит проходов:       {max_passes}"
                    )
                )

                self.assertEqual(
                    arr_copy, sorted_expected,
                    msg=(
                        "FAIL: Полная сортировка пузырьком (повторяя BubbleSortStep) дала неверный результат.\n"
                        f"Вход:      {arr}\n"
                        f"Ожидалось: {sorted_expected}\n"
                        f"Получено:  {arr_copy}"
                    )
                )

if __name__ == "__main__":
    unittest.main()