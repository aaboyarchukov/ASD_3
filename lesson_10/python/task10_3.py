import unittest
from task10 import ksort

def setup() -> ksort:
    return ksort()

def filter_items_of_nones(items : list[str]) -> list[str]:
    return list(filter(lambda row: row is not None, items))

class TestValidateRow(unittest.TestCase):
    def test_validate_row(self):
        cases = [
            ["empty row", "", False],
            ["one element row", "1", False],
            ["two elements row", "a1", False],
            ["three wrong elements row 1", "123", False],
            ["three wrong elements row 2", "ab3", False],
            ["three wrong elements row 3", "1ab", False],
            ["three wrong elements row 4", "p11", False],
            ["three wrong elements row 4", "W11", False],
            ["three right elements row", "a11", True],
            ["many elements row", "a11123asd", False],
        ]

        for name, init_row, result in cases:
                with self.subTest(name=name, init_row=init_row, result=result):
                    ksort_setup = setup()
                    valid_row = ksort_setup.valid_row(init_row)
                    self.assertEqual(
                        valid_row, result,
                        msg=(
                            f"FAIL: KSort неверно валидировал строки.\n"
                            f"Ожидалось: {result}\n"
                            f"Получено:  {valid_row}"
                        )
                    )

class TestIndex(unittest.TestCase):
    def test_hash(self):
        cases = [
            ["empty row", "", 5, -1],
            ["one element row", "1", 5, -1],
            ["two elements row", "a1", 5, -1],
            ["three wrong elements row 1", "123", 5, -1],
            ["three wrong elements row 2", "ab3", 5, -1],
            ["three wrong elements row 3", "1ab", 5, -1],
            ["three wrong elements row 4", "p11", 5, -1],
            ["three wrong elements row 4", "W11", 5, -1],
            ["three right elements row 1", "a11", 5, 11],
            ["three right elements row 2", "b64", 5, 164],
            ["three right elements row 3", "g12", 5, 612],
            ["many elements row", "a11123asd", 5, -1],
        ]

        for name, init_row, tries, result_hash in cases:
                with self.subTest(name=name, init_row=init_row, result_hash=result_hash):
                    ksort_setup = setup()

                    hash = ksort_setup.hash(init_row)
                    self.assertEqual(
                        result_hash, hash,
                        msg=(
                            f"FAIL: KSort неверно посчитал хеш.\n"
                            f"Ожидалось: {result_hash}\n"
                            f"Получено:  {hash}"
                        )
                    )

                    for _ in range(tries):
                        repeat_hash = ksort_setup.hash(init_row)
                        self.assertEqual(
                            repeat_hash, hash,
                            msg=(
                                f"FAIL: KSort неверно посчитал хеш повторно.\n"
                                f"Ожидалось: {hash}\n"
                                f"Получено:  {repeat_hash}"
                            )
                        )

                

class TestAdd(unittest.TestCase):
    def test_add(self):
        cases = [
            ["empty rows", [""], [False]],
            ["one element row", ["1"], [False]],
            ["two elements row", ["a1"], [False]],
            ["three wrong elements row 1", ["123"], [False]],
            ["three wrong elements row 2", ["ab3"], [False]],
            ["three wrong elements row 3", ["1ab"], [False]],
            ["three wrong elements row 4", ["p11"], [False]],
            ["three wrong elements row 4", ["W11"], [False]],
            ["three right elements row 1", ["a11"], [True]],
            ["three right elements row 2", ["a11", "b64", "g12"], [True, True, True]],
            ["three right elements row 3", ["a55", "a00", "b12"], [True, True, True]],
            ["three right elements row 3", ["a55", "a00", "123"], [True, True, False]],
            ["three right elements row 3", ["a55", "a00", "123", "b12", "g12", "H12"], [True, True, False, True, True, False]],
            ["many elements row", ["a11123asd"], [False]],
        ]

        for name, init_row_array, results in cases:
                with self.subTest(name=name, init_row_array=init_row_array, results=results):
                    ksort_setup = setup()
                    op_results = []
                    for value in init_row_array:
                        hash = ksort_setup.hash(value)
                        op_result = ksort_setup.add(value)
                        op_results.append(op_result)
                        
                        if hash == -1:
                            continue

                        
                        self.assertEqual(
                            ksort_setup.items[hash], value,
                            msg=(
                                f"FAIL: KSort неверно вставил строку.\n"
                                f"Ожидалось: {value}\n"
                                f"Получено:  {ksort_setup.items[hash]}"
                            )
                        )


                    self.assertEqual(
                        op_results, results,
                        msg=(
                            f"FAIL: KSort неверно вставил элементы.\n"
                            f"Ожидалось: {results}\n"
                            f"Получено:  {op_results}"
                        )
                    )

class TestSort(unittest.TestCase):
    def test_sort(self):
        cases = [
            ["empty rows", [""], []],
            ["one element row", ["1"], []],
            ["two elements row", ["a1"], []],
            ["three wrong elements row 1", ["123"], []],
            ["three wrong elements row 2", ["ab3"], []],
            ["three wrong elements row 3", ["1ab"], []],
            ["three wrong elements row 4", ["p11"], []],
            ["three wrong elements row 4", ["W11"], []],
            ["three right elements row 1", ["a11"], ["a11"]],
            ["three right elements row 2", ["a11", "b64", "g12"], ["a11", "b64", "g12"]],
            ["three right elements row 3", ["a55", "a00", "b12"], ["a00", "a55", "b12"]],
            ["three right elements row 3", ["a55", "a00", "123"], ["a00", "a55"]],
            ["three right elements row 3", ["a55", "a00", "123", "b12", "g12", "H12"], ["a00", "a55", "b12", "g12"]],
            ["many elements row", ["a11123asd"], []],
        ]

        for name, init_row_array, result_array in cases:
                with self.subTest(name=name, init_row_array=init_row_array, result_array=result_array):
                    ksort_setup = setup()
                    for value in init_row_array:
                        ksort_setup.add(value)

                    filter_result_array = filter_items_of_nones(ksort_setup.items)
                    self.assertEqual(
                        filter_result_array, result_array,
                        msg=(
                            f"FAIL: KSort неверно вставил элементы.\n"
                            f"Ожидалось: {result_array}\n"
                            f"Получено:  {filter_result_array}"
                        )
                    )

if __name__ == "__main__":
    unittest.main()