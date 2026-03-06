# Additional problem of finding 
# the longest strictly monotonous sequence

# [7, 1, 2, 3, 0, 4, 5, 6, 5] -> [1, 2, 3, 4, 5, 6]
def BinarySearch():
    pass

def StrictlyMonotonousSequence(array : list[int]) -> list[int]:
    if len(array) <= 1:
        return array
    
    return []


import unittest

class TestStrictlyMonotonousSequence(unittest.TestCase):
    def test_strictly_monotonous_sequence(self):
        cases = [
            {
                "name": "empty array",
                "array": [],
                "result": []
            },
            {
                "name": "one element array",
                "array": [1],
                "result": [1]
            },
            {
                "name": "odd elements array",
                "array": [7, 1, 2, 3, 0, 4, 5, 6, 5],
                "result": [1, 2, 3, 4, 5, 6]
            },
            {
                "name": "even elements array",
                "array": [7, 1, 2, 3, 0, 4, 5, 6, 5, 9],
                "result": [1, 2, 3, 4, 5, 6, 9]
            },
        ]

        for case in cases:
            with self.subTest(name=case['name'], array=case['array'], result=case['result']):
                result = StrictlyMonotonousSequence(case['array'])
                self.assertEqual(
                    result, case["result"],
                    msg=(
                        f"FAIL: Неверный результат поиска монотонной последовательности.\n"
                        f"Ожидалось: {case["result"]}\n"
                        f"Получено:  {result}"
                    )
                )
                

if __name__ == "__main__":
    unittest.main()