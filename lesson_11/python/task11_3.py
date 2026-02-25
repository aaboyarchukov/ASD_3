import unittest
from task11 import BinarySearch

def setup(array):
    return BinarySearch(sorted(array))

class TestBinarySearchStep(unittest.TestCase):
    def test_step(self):
        cases = [
            {
                "name": "empty array",
                "array": [],
                "target": 5,
                "tries": 3,
                "init_pointers": [0, 0],
                "init_state": BinarySearch.get_fail(),
                "bounds_pointers": [[0, 0], [0, 0], [0, 0]],
                "bounds_states": [BinarySearch.get_fail(), BinarySearch.get_fail(), BinarySearch.get_fail()]
            },
            {
                "name": "one element array",
                "array": [1],
                "target": 1,
                "tries": 3,
                "init_pointers": [0, 0],
                "init_state": BinarySearch.get_search(),
                "bounds_pointers": [[0, 0], [0, 0], [0, 0]],
                "bounds_states": [BinarySearch.get_success(), BinarySearch.get_success(), BinarySearch.get_success()]
            },
            {
                "name": "odd array not enough tries",
                "array": [1, 2, 3, 4, 5],
                "target": 5,
                "tries": 1,
                "init_pointers": [0, 4],
                "init_state": BinarySearch.get_search(),
                "bounds_pointers": [[3, 4]],
                "bounds_states": [BinarySearch.get_search()]
            },
            {
                "name": "odd array enough tries",
                "array": [1, 2, 3, 4, 5],
                "target": 5,
                "tries": 3,
                "init_pointers": [0, 4],
                "init_state": BinarySearch.get_search(),
                "bounds_pointers": [[3, 4], [3, 4], [3, 4]],
                "bounds_states": [BinarySearch.get_search(), BinarySearch.get_success(), BinarySearch.get_success()]
            },
            {
                "name": "odd array enough tries with fail",
                "array": [1, 2, 3, 4, 5],
                "target": -1,
                "tries": 4,
                "init_pointers": [0, 4],
                "init_state": BinarySearch.get_search(),
                "bounds_pointers": [[0, 1], [0, 1], [0, 1], [0, 1]],
                "bounds_states": [BinarySearch.get_search(), BinarySearch.get_fail(), BinarySearch.get_fail(), BinarySearch.get_fail()]
            },
            {
                "name": "even array not enough tries",
                "array": [1, 2, 3, 4, 5, 6],
                "target": 4,
                "tries": 2,
                "init_pointers": [0, 5],
                "init_state": BinarySearch.get_search(),
                "bounds_pointers": [[3, 5], [3, 3]],
                "bounds_states": [BinarySearch.get_search(), BinarySearch.get_search()]
            },
            {
                "name": "even array enough tries",
                "array": [1, 2, 3, 4, 5, 6],
                "target": 4,
                "tries": 4,
                "init_pointers": [0, 5],
                "init_state": BinarySearch.get_search(),
                "bounds_pointers": [[3, 5], [3, 3], [3, 3], [3, 3]],
                "bounds_states": [BinarySearch.get_search(), BinarySearch.get_search(), BinarySearch.get_success(), BinarySearch.get_success()]
            },
            {
                "name": "even array enough tries with fail",
                "array": [1, 2, 3, 4, 5, 6],
                "target": -1,
                "tries": 4,
                "init_pointers": [0, 5],
                "init_state": BinarySearch.get_search(),
                "bounds_pointers": [[0, 1], [0, 1], [0, 1], [0, 1]],
                "bounds_states": [BinarySearch.get_search(), BinarySearch.get_fail(), BinarySearch.get_fail(), BinarySearch.get_fail()]
            },
        ]

        for case in cases:
            with self.subTest(name=case["name"], init_array=case["array"], target_element=case["target"]):
                setup_binary_search = setup(case["array"])
                
                # проверка начальных состояний указателей
                # и состояние поиска
                self.assertEqual(
                    setup_binary_search.GetState(), case["init_state"],
                    msg=(
                        f"FAIL: Неверное начальное состояние.\n"
                        f"Ожидалось: {case['init_state']}\n"
                        f"Получено:  {setup_binary_search.GetState()}"
                    )
                )

                self.assertEqual(
                    [setup_binary_search.Left, setup_binary_search.Right], case["init_pointers"],
                    msg=(
                        f"FAIL: Неверное начальное состояние указателей.\n"
                        f"Ожидалось: {case['init_pointers']}\n"
                        f"Получено:  {[setup_binary_search.Left, setup_binary_search.Right]}"
                    )
                )

                for i in range(case["tries"]):
                    setup_binary_search.Step(case["target"])

                    target_state = case["bounds_states"][i]
                    state_now = setup_binary_search.GetState()

                    self.assertEqual(
                        state_now, target_state,
                        msg=(
                            f"FAIL: Неверное изменение состояний.\n"
                            f"Ожидалось: {target_state}\n"
                            f"Получено:  {state_now}"
                        )
                    )
                    
                    self.assertEqual(
                        [setup_binary_search.Left, setup_binary_search.Right], case["bounds_pointers"][i],
                        msg=(
                            f"FAIL: Неверное изменение указателей.\n"
                            f"Ожидалось: {case['bounds_pointers'][i]}\n"
                            f"Получено:  {[setup_binary_search.Left, setup_binary_search.Right]}"
                        )
                    )

if __name__ == "__main__":
    unittest.main()