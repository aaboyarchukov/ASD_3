import unittest

from task2 import InsertionSortStep, find_position, insert_at_position

class TestFindPosition(unittest.TestCase):
    # preconditionals
    def test_find_position_preconditionals(self):
        cases = [
            ([1, 2, 3], [2, 0, 1]),
            ([1, 2, 3, 4], [3, 1, 2]),
            ([5], [0, 0, 1]),
        ]

        for case in cases:
            with self.subTest(case=case):
                array, (start, stop, step) = case
                self.assertGreaterEqual(stop, 0, "stop должен быть >= 0")
                self.assertLessEqual(stop, start, "stop должен быть <= start") 
                self.assertLess(start, len(array), "start должен быть < len(array)")
                self.assertGreater(step, 0, "step должен быть > 0")

    # postconditionals
    def test_find_position_postconditions(self):
        cases = [
            ([1, 2, 3], [2, 0, 1]),
            ([5, 3, 1], [2, 0, 1]), 
            ([1, 3, 5], [2, 0, 1]),
            ([2, 2, 2], [1, 0, 1]),
        ]

        for case in cases:
            with self.subTest(case=case):
                array, (start, stop, step) = case
                result = find_position(array, start, stop, step)

                self.assertGreaterEqual(result, stop, 
                    f"Результат {result} должен быть >= stop={stop}")
                self.assertLessEqual(result, start,
                    f"Результат {result} должен быть <= start={start}")

    # edge cases: find_position
    def test_find_position_edge_cases(self):
        cases = [
            ([5], [0, 0, 1], 0),  # Минимальный массив
            ([1, 2, 3], [2, 2, 1], 2),  # start == stop
            ([5, 3, 1], [2, 0, 1], 0),  # Элемент меньше всех
            ([1, 3, 5], [2, 0, 1], 2),  # Элемент больше всех
            ([1, 9, 2, 8, 3, 7], [4, 0, 2], 4),  # Шаг больше 1
        ]

        for case in cases:
            with self.subTest(case=case):
                array, (start, stop, step), expected = case

                result = find_position(array, start, stop, step)
                if isinstance(expected, list):
                    self.assertIn(result, expected)
                else:
                    self.assertEqual(result, expected)
    
class TestInsertAtPosition(unittest.TestCase):
    # preconditionals
    def test_insert_at_position_preconditions(self):
        cases = [
            ([1, 2, 3], [2, 0, 1]),
            ([5], [0, 0, 1]),
            ([1, 2, 3, 4, 5, 6], [4, 2, 2]),
        ]

        for case in cases:
            with self.subTest(case=case):
                array, (position_from, position_to, step) = case

                self.assertGreaterEqual(position_to, 0, "position_to должен быть >= 0")
                self.assertLessEqual(position_to, position_from, "position_to должен быть <= position_from")
                self.assertLess(position_from, len(array), "position_from должен быть < len(array)")
                self.assertGreater(step, 0, "step должен быть > 0")

    # postconditionals
    def test_insert_at_position_postconditions(self):
        cases = [
            ([1, 3, 2], [2, 1, 1]),
            ([2, 3, 4, 1], [3, 0, 1]),
            ([3, 9, 1, 8, 2, 7], [4, 0, 2]),
        ]

        for case in cases:
            with self.subTest(case=case):
                array, (position_from, position_to, step) = case

                original_value = array[position_from]
                original_content = array.copy()
                original_length = len(array)

                insert_at_position(array, position_from, position_to, step)

                # Проверяем постусловия
                self.assertEqual(array[position_to], original_value, 
                    "Элемент не перемещен на целевую позицию")
                self.assertEqual(len(array), original_length,
                    "Изменилось количество элементов")
                self.assertCountEqual(array, original_content,
                    "Изменилось содержимое массива")

    # edge cases: insert_at_position
    def test_insert_at_position_edge_cases(self):
        cases = [
            ([1, 2, 3], [1, 1, 1], [1, 2, 3]),  # Нет перемещения
            ([1, 3, 2], [2, 1, 1], [1, 2, 3]),  # Перемещение на одну позицию
            ([2, 1, 3], [1, 0, 1], [1, 2, 3]),  # Перемещение в начало
            ([2, 3, 4, 1], [3, 0, 1], [1, 2, 3, 4]),  # Максимальное смещение
            ([3, 9, 1, 8, 2, 7], [4, 0, 2], [2, 9, 3, 8, 1, 7]),  # Шаг больше 1
            ([1], [0, 0, 1], [1]),  # Минимальный массив
        ]

        for case in cases:
            with self.subTest(case=case):
                original_array, (position_from, position_to, step), expected = case
                array = original_array.copy()

                insert_at_position(array, position_from, position_to, step)
                self.assertEqual(array, expected)
    

class TestInsertionSortStep(unittest.TestCase):

    # preconditionals
    def test_insertion_sort_step_preconditions(self):
        cases = [
            ([1, 2, 3], [1, 0]),
            ([5], [1, 0]),
            ([1, 2, 3, 4], [2, 1]),
            ([1, 2, 3, 4, 5], [3, 2]),
        ]

        for case in cases:
            with self.subTest(case=case):
                array, (step, i) = case

                self.assertGreaterEqual(i, 0, "i должен быть >= 0")
                self.assertLess(i, len(array), "i должен быть < len(array)")
                self.assertGreater(step, 0, "step должен быть > 0")

    # postconditionals
    def test_insertion_sort_step_postconditions(self):
        cases = [
            ([3, 9, 1, 8, 2, 7], [2, 0]),
            ([4, 5, 2, 6, 1, 7], [3, 1]),
            ([5, 2, 4, 1, 3], [2, 0]),
        ]

        for case in cases:
            with self.subTest(case=case):
                array, (step, i) = case

                original_content = array.copy()
                original_length = len(array)

                # Запоминаем элементы других подпоследовательностей
                other_elements = {}
                for idx in range(len(array)):
                    if idx % step != i % step:
                        other_elements[idx] = array[idx]

                InsertionSortStep(array, step, i)

                # 1. Подпоследовательность отсортирована
                subsequence = [array[j] for j in range(i, len(array), step)]
                self.assertEqual(subsequence, sorted(subsequence),
                    "Подпоследовательность должна быть отсортирована")

                # 2. Элементы других подпоследовательностей не изменены
                for idx, expected_value in other_elements.items():
                    self.assertEqual(array[idx], expected_value,
                        f"Элемент вне подпоследовательности изменен: индекс {idx}")

                # 3. Содержимое массива сохранилось
                self.assertEqual(len(array), original_length,
                    "Изменилось количество элементов")
                self.assertCountEqual(array, original_content,
                    "Изменилось содержимое массива")

    # edge cases: InsertionSortStep
    def test_insertion_sort_step_edge_cases(self):
        """Краевые случаи для InsertionSortStep"""
        cases = [
            ([5], [1, 0], [5]),  # Минимальный массив
            ([1, 2], [1, 0], [1, 2]),  # Два элемента, отсортированы
            ([2, 1], [1, 0], [1, 2]),  # Два элемента, нужна сортировка
            ([3, 1, 2], [2, 1], [3, 1, 2]),  # Один элемент в подпоследовательности
            ([1, 2, 3], [3, 0], [1, 2, 3]),  # Шаг равен длине массива
            ([1, 3, 2, 4], [2, 1], [1, 3, 2, 4]),  # Уже отсортированная подпоследовательность
            ([5, 5, 5, 5], [1, 0], [5, 5, 5, 5]),  # Все элементы одинаковые
            ([4, 9, 3, 8, 2, 7, 1, 6], [2, 0], [1, 9, 2, 8, 3, 7, 4, 6]),  # Worst case
            ([1, 9, 2, 8, 3, 7, 4, 6], [2, 0], [1, 9, 2, 8, 3, 7, 4, 6]),  # Best case
            ([1, 2, 3, 4, 5], [3, 2], [1, 2, 3, 4, 5]),  # Граничный случай
        ]

        for case in cases:
            with self.subTest(case=case):
                original_array, (step, i), expected = case
                array = original_array.copy()

                InsertionSortStep(array, step, i)
                self.assertEqual(array, expected)

class TestFullArraySorting(unittest.TestCase):
    def test_full_array_sorting_edge_cases(self):
        """Краевые случаи для полной сортировки"""
        cases = [
            ([], [], "empty_array"),
            ([1], [1], "single_element"),
            ([2, 1], [1, 2], "two_elements_reversed"),
            ([1, 2], [1, 2], "two_elements_sorted"),
            ([7, 6, 5, 4, 3, 2, 1], [1, 2, 3, 4, 5, 6, 7], "reverse_order_worst_case"),
            ([1, 2, 3, 4, 5], [1, 2, 3, 4, 5], "already_sorted_best_case"),
            ([5, 1, 4, 2, 8], [1, 2, 4, 5, 8], "random_order"),
            ([2, 2, 1, 3, 1, 0, 0], [0, 0, 1, 1, 2, 2, 3], "duplicates_present"),
            ([5, 5, 5, 5], [5, 5, 5, 5], "all_elements_equal"),
            ([3], [3], "single_element_boundary"),
        ]

        for case in cases:
            with self.subTest(test=case[2], original=case[0]):
                original_array, expected, description = case
                array = original_array.copy()

                step = len(array) // 2
                while step > 0:
                    for i in range(min(step, len(array))):
                        if i < len(array):
                            InsertionSortStep(array, step, i)
                    step //= 2

                self.assertEqual(array, expected,
                    f"Сортировка {description} дала неверный результат")

if __name__ == "__main__":
    unittest.main(verbosity=2)