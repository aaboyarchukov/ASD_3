import unittest
from task11 import BinarySearch

def setup(array):
    return BinarySearch(sorted(array))

class TestBinarySearchStep(unittest.TestCase):
    def test_step(self):
        cases = [
            ["empty array", [], 5, 3, [[0, -1], [0, -1], [0, -1], [0, -1]], [BinarySearch.get_search(), BinarySearch.get_fail(), BinarySearch.get_fail(), BinarySearch.get_fail()]],
            ["one element array", [1], 1, 3, [[0, 0], [0, 0], [0, 0], [0, 0]], [BinarySearch.get_search(), BinarySearch.get_success(), BinarySearch.get_success(), BinarySearch.get_success()]],
            ["odd array not enough tries", [1, 2, 3, 4, 5], 5, 1, [[0, 4], [3, 4]], [BinarySearch.get_search(), BinarySearch.get_search()]],
            ["odd array enough tries", [1, 2, 3, 4, 5], 5, 3, [[0, 4], [3, 4], [3, 3], [3, 3]], [BinarySearch.get_search(), BinarySearch.get_search(), BinarySearch.get_success()]],
            ["odd array enough tries with fail", [1, 2, 3, 4, 5], -1, 3, [[0, 4], [0, 1], [0, 0], [0, 0]], [BinarySearch.get_search(), BinarySearch.get_search(), BinarySearch.get_fail(), BinarySearch.get_fail()]],
            ["even array not enough tries", [1, 2, 3, 4, 5, 6], 4, 2, [[0, 5], [3, 5], [3, 4]], [BinarySearch.get_search(), BinarySearch.get_search(), BinarySearch.get_search()]],
            ["even array enough tries", [1, 2, 3, 4, 5, 6], 4, 4, [[0, 5], [3, 5], [3, 4], [3, 3], [3, 3]], [BinarySearch.get_search(), BinarySearch.get_search(), BinarySearch.get_search(), BinarySearch.get_success(), BinarySearch.get_success()]],
            ["even array enough tries with fail", [1, 2, 3, 4, 5, 6], -1, 4, [[0, 5], [0, 1], [0, 0], [0, 0], [0, 0]], [BinarySearch.get_search(), BinarySearch.get_search(), BinarySearch.get_fail(), BinarySearch.get_fail(), BinarySearch.get_fail()]],
        ]

        for name, init_array, target_element, tries, pointers_states, search_step_states in cases:
                with self.subTest(name=name, init_array=init_array, target_element=target_element):
                    setup_binary_search = setup(init_array)
                    
                    for i in range(tries):
                        target_state = search_step_states[i]
                        state_now = setup_binary_search.GetState()

                        # проверку делаем до шага поиска
                        # чтобы проверить начальное состояние
                        self.assertEqual(
                            state_now, target_state,
                            msg=(
                                f"FAIL: Неверное изменение состояний.\n"
                                f"Ожидалось: {target_state}\n"
                                f"Получено:  {state_now}"
                            )
                        )

                        # проверку делаем до шага поиска
                        # чтобы проверить начальное состояние
                        self.assertEqual(
                            [setup_binary_search.left, setup_binary_search.right], pointers_states[i],
                            msg=(
                                f"FAIL: Неверное изменение указателей.\n"
                                f"Ожидалось: {pointers_states[i]}\n"
                                f"Получено:  {[setup_binary_search.left, setup_binary_search.right]}"
                            )
                        )

                        setup_binary_search.Step(target_element)
                    
                    # проверка на последнее изменение при шаге поиска
                    self.assertEqual(
                        setup_binary_search.GetState(), search_step_states[-1],
                        msg=(
                            f"FAIL: Неверное изменение состояний.\n"
                            f"Ожидалось: {target_state}\n"
                            f"Получено:  {state_now}"
                        )
                    )

                    self.assertEqual(
                        [setup_binary_search.left, setup_binary_search.right], pointers_states[-1],
                        msg=(
                            f"FAIL: Неверное изменение указателей.\n"
                            f"Ожидалось: {pointers_states[-1]}\n"
                            f"Получено:  {[setup_binary_search.left, setup_binary_search.right]}"
                        )
                    )

if __name__ == "__main__":
    unittest.main()