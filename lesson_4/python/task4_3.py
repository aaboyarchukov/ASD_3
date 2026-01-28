import unittest
from task4 import ArrayChunk

class TestBuildArrayChunk(unittest.TestCase):
    def test_build_array_chunk(self):
        cases = [
            ("empty array", [], [], 0),
            ("one element", [1], [1], 0),
            ("many elements 1", [3, 1, 2], [1, 2, 3], 1),
            ("many elements 2", [40, 13, 4, 1], [1, 4, 13, 40], 2),
            ("many elements 3", [7, 5, 6, 4, 3, 1, 2], [2, 1, 3, 4, 6, 5, 7], 3),
            ("many elements 4", [121, 40, 13, 4, 1], [1, 4, 13, 40, 121], 2),
        ]

        for name, get, want, want_indx in cases:
            with self.subTest(name=name, get=get, want=want, want_indx=want_indx):
                indx = ArrayChunk(get)
                self.assertEqual(
                    get, want,
                    msg=(
                        "FAIL: ArrayChunk неверно разделил массив на группы.\n"
                        f"Ожидалось: {want}\n"
                        f"Получено:  {get}"
                    )
                )

                self.assertEqual(
                    indx, want_indx,
                    msg=(
                        "FAIL: ArrayChunk неверно вернул индекс опорного элемента.\n"
                        f"Ожидалось: {want_indx}\n"
                        f"Получено:  {indx}"
                    )
                )

if __name__ == "__main__":
    unittest.main()