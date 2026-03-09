import unittest
from task12 import BinarySearch

class TestGallopingSearch(unittest.TestCase):
    def test_galloping_search(self):
        cases = [
            {
                "name": "empty array",
                "array": [],
                "target": 5,
                "result": False
            },
            {
                "name": "one element array true",
                "array": [1],
                "target": 1,
                "result": True
            },
            {
                "name": "one element array false",
                "array": [1],
                "target": 5,
                "result": False
            },
            {
                "name": "odd element array true",
                "array": [1, 2, 3, 4, 5],
                "target": 3,
                "result": True
            },
            {
                "name": "odd element array false",
                "array": [1, 2, 3, 4, 5],
                "target": 7,
                "result": False
            },
            {
                "name": "even element array true",
                "array": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
                "target": 10,
                "result": True
            },
            {
               "name": "even element array false",
                "array": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
                "target": 12,
                "result": False
            },
        ]

        for case in cases:
            with self.subTest(name=case["name"], init_array=case["array"], target_element=case["target"]):
                is_find = BinarySearch.GallopingSearch(case["array"], case["target"])

                self.assertEqual(
                    is_find, case["result"],
                    msg=(
                        f"FAIL: Неверный результат поиска.\n"
                        f"Ожидалось: {case["result"]}\n"
                        f"Получено:  {is_find}"
                    )
                )

if __name__ == "__main__":
    unittest.main()