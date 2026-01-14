import unittest

from task2 import InsertionSortStep


class TestInsertionSortStep(unittest.TestCase):

    def test_one_step_sorts_chain_fully(self):
        cases = [
            ([3, 1, 2], 1, 1, [3, 1, 2]),
            ([3, 2, 1], 1, 1, [3, 1, 2]),
            ([7, 6, 5, 4, 3, 2, 1], 3, 0, [1, 6, 5, 4, 3, 2, 7]),
            ([9, 8, 7, 6, 5, 4, 3, 2], 3, 1, [9, 2, 7, 6, 5, 4, 3, 8]),
            ([2, 1, 1, 1], 1, 1, [2, 1, 1, 1]),
        ]

        for arr, step, i, expected in cases:
            with self.subTest(arr=arr, step=step, i=i):
                a = arr.copy()
                InsertionSortStep(a, step, i)
                self.assertEqual(
                    a, expected,
                    msg=(
                        "FAIL: Один шаг (полная сортировка подпоследовательности i, i+step, ...) выполнен неверно.\n"
                        f"Вход:      {arr}\n"
                        f"step={step}, i={i}\n"
                        f"Ожидалось: {expected}\n"
                        f"Получено:  {a}"
                    )
                )

    def test_one_step_does_not_touch_elements_outside_chain(self):
        arr = [7, 6, 5, 4, 3, 2, 1]
        step = 3
        i = 0  # цепочка 0,3,6

        a = arr.copy()
        InsertionSortStep(a, step, i)

        chain = set(range(i, len(arr), step))
        for idx in range(len(arr)):
            if idx not in chain:
                self.assertEqual(
                    a[idx], arr[idx],
                    msg=(
                        "FAIL: Изменён элемент вне сортируемой подпоследовательности.\n"
                        f"Вход: {arr}\n"
                        f"step={step}, i={i}\n"
                        f"Цепочка индексов: {sorted(chain)}\n"
                        f"Индекс {idx}: было {arr[idx]} -> стало {a[idx]}\n"
                        f"Итоговый массив: {a}"
                    )
                )

        self.assertCountEqual(
            a, arr,
            msg=(
                "FAIL: После шага изменилось содержимое массива (потеря/дублирование элементов).\n"
                f"Вход:     {arr}\n"
                f"Получено: {a}"
            )
        )

    def test_n_steps_for_fixed_step_run_i_0_to_step_minus_1(self):
        cases = [
            ([7, 6, 5, 4, 3, 2, 1], 3),
            ([10, 9, 8, 7, 6, 5, 4, 3, 2, 1], 4),
            ([2, 2, 1, 3, 1, 0, 0], 2),
            ([1, 5, 3, 5, 2, 5, 4], 3),
        ]

        for arr, step in cases:
            with self.subTest(arr=arr, step=step):
                a = arr.copy()

                for i in range(min(step, len(a))):
                    InsertionSortStep(a, step, i)

                for r in range(min(step, len(a))):
                    seq = [a[j] for j in range(r, len(a), step)]
                    self.assertEqual(
                        seq, sorted(seq),
                        msg=(
                            "FAIL: После шагов i=0..step-1 подпоследовательность по r не отсортирована.\n"
                            f"Исходный вход: {arr}\n"
                            f"step={step}, r={r}\n"
                            f"Подпоследовательность: {seq}\n"
                            f"Ожидалось:            {sorted(seq)}\n"
                            f"Итоговый массив:      {a}"
                        )
                    )

                self.assertCountEqual(
                    a, arr,
                    msg=(
                        "FAIL: Изменилось содержимое массива (потеря/дублирование элементов) после n шагов.\n"
                        f"Вход:     {arr}\n"
                        f"Получено: {a}"
                    )
                )

    def test_n_steps_for_fixed_step_run_i_0_to_n_minus_1(self):
        cases = [
            ([7, 6, 5, 4, 3, 2, 1], 3),
            ([10, 9, 8, 7, 6, 5, 4, 3, 2, 1], 4),
            ([2, 2, 1, 3, 1, 0, 0], 2),
            ([1, 5, 3, 5, 2, 5, 4], 3),
        ]

        for arr, step in cases:
            with self.subTest(arr=arr, step=step):
                a = arr.copy()

                for i in range(len(a)):
                    InsertionSortStep(a, step, i)

                for r in range(min(step, len(a))):
                    seq = [a[j] for j in range(r, len(a), step)]
                    self.assertEqual(
                        seq, sorted(seq),
                        msg=(
                            "FAIL: После прогона i=0..n-1 подпоследовательность по r не отсортирована.\n"
                            f"Исходный вход: {arr}\n"
                            f"step={step}, r={r}\n"
                            f"Подпоследовательность: {seq}\n"
                            f"Ожидалось:            {sorted(seq)}\n"
                            f"Итоговый массив:      {a}"
                        )
                    )

                self.assertCountEqual(
                    a, arr,
                    msg=(
                        "FAIL: Изменилось содержимое массива (потеря/дублирование элементов) после n шагов.\n"
                        f"Вход:     {arr}\n"
                        f"Получено: {a}"
                    )
                )

    def test_full_array_sorting_shell_like_schedule(self):
        cases = [
            [],
            [1],
            [2, 1],
            [7, 6, 5, 4, 3, 2, 1],
            [5, 1, 4, 2, 8],
            [2, 2, 1, 3, 1, 0, 0],
            [1, 2, 3, 4, 5],
        ]

        for arr in cases:
            with self.subTest(arr=arr):
                a = arr.copy()

                step = len(a) // 2
                while step > 0:
                    for i in range(min(step, len(a))):
                        InsertionSortStep(a, step, i)
                    step //= 2

                self.assertEqual(
                    a, sorted(arr),
                    msg=(
                        "FAIL: Полная сортировка (Shell-подобной схемой через InsertionSortStep) дала неверный результат.\n"
                        f"Вход:      {arr}\n"
                        f"Ожидалось: {sorted(arr)}\n"
                        f"Получено:  {a}"
                    )
                )


if __name__ == "__main__":
    unittest.main(verbosity=2)