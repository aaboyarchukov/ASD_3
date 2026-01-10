import unittest

from task2 import InsertionSortStep


class TestInsertionSortStep(unittest.TestCase):

    def test_one_insertion_places_element_correctly(self):
        cases = [
            ([3, 1, 2], 1, 1, [1, 3, 2]),
            ([3, 1, 2], 1, 2, [1, 2, 3]),
            ([7, 6, 5, 4, 3, 2, 1], 3, 6, [1, 6, 5, 7, 3, 2, 4]),
            ([9, 8, 7, 6, 5, 4, 3, 2], 3, 7, [9, 2, 7, 6, 8, 4, 3, 5]),
            ([2, 1, 1, 1], 1, 3, [1, 1, 1, 2]),
        ]

        for arr, step, i, expected in cases:
            with self.subTest(arr=arr, step=step, i=i):
                a = arr.copy()
                InsertionSortStep(a, step, i)

                self.assertEqual(
                    a, expected,
                    msg=(
                        "FAIL: Один шаг (одна вставка) выполнен неверно.\n"
                        f"Вход:      {arr}\n"
                        f"step={step}, i={i}\n"
                        f"Ожидалось: {expected}\n"
                        f"Получено:  {a}"
                    )
                )

    def test_one_insertion_does_not_touch_other_mod_classes(self):
        arr = [7, 6, 5, 4, 3, 2, 1]
        step = 3
        i = 6

        a = arr.copy()
        InsertionSortStep(a, step, i)

        touched = set(range(i % step, len(arr), step))
        other_indices = [idx for idx in range(len(arr)) if idx not in touched]

        for idx in other_indices:
            self.assertEqual(
                a[idx], arr[idx],
                msg=(
                    "FAIL: Изменён элемент другого класса по mod step.\n"
                    f"Вход: {arr}\n"
                    f"step={step}, i={i}\n"
                    f"Индекс {idx} (класс {idx % step}) не должен был меняться.\n"
                    f"Было: {arr[idx]} -> Стало: {a[idx]}\n"
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

    def test_n_steps_for_fixed_step_gives_gap_sorted(self):
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
                            "FAIL: После полного прогона по i массив не стал step-отсортированным.\n"
                            f"Исходный вход: {arr}\n"
                            f"step={step}, проверяем r={r}\n"
                            f"Подпоследовательность: {seq}\n"
                            f"Ожидалось:            {sorted(seq)}\n"
                            f"Итоговый массив a:    {a}"
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
                    for i in range(len(a)):
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