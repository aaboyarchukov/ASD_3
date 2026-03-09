# Additional problem of finding 
# the longest strictly monotonous sequence

# [7, 1, 2, 3, 0, 4, 5, 6, 5] -> [1, 2, 3, 4, 5, 6]
def BinarySearchLeft(array, target):
    size = len(array)
    left, right = 0, size

    while left < right:
        middle = (left + right) // 2

        if array[middle] >= target:
            right = middle
        if array[middle] < target:
            left = middle + 1
    
    return left

def StrictlyMonotonousSequence(array : list[int]) -> list[int]:
    if len(array) <= 1:
        return array
    
    return []


import unittest

# class TestStrictlyMonotonousSequence(unittest.TestCase):
#     def test_strictly_monotonous_sequence(self):
#         cases = [
#             {
#                 "name": "empty array",
#                 "array": [],
#                 "result": []
#             },
#             {
#                 "name": "one element array",
#                 "array": [1],
#                 "result": [1]
#             },
#             {
#                 "name": "odd elements array",
#                 "array": [7, 1, 2, 3, 0, 4, 5, 6, 5],
#                 "result": [1, 2, 3, 4, 5, 6]
#             },
#             {
#                 "name": "even elements array",
#                 "array": [7, 1, 2, 3, 0, 4, 5, 6, 5, 9],
#                 "result": [1, 2, 3, 4, 5, 6, 9]
#             },
#         ]

#         for case in cases:
#             with self.subTest(name=case['name'], array=case['array'], result=case['result']):
#                 result = StrictlyMonotonousSequence(case['array'])
#                 self.assertEqual(
#                     result, case["result"],
#                     msg=(
#                         f"FAIL: Неверный результат поиска монотонной последовательности.\n"
#                         f"Ожидалось: {case["result"]}\n"
#                         f"Получено:  {result}"
#                     )
#                 )

class TestBinarySearchLeft(unittest.TestCase):
    def test_binary_search_left(self):
        cases = [
            {
                "name": "empty array",
                "array": [],
                "target": 1,
                "result": 0
            },
            {
                "name": "one element array -> switch",
                "array": [1],
                "target": 0,
                "result": 0
            },
            {
                "name": "one element array -> append",
                "array": [1],
                "target": 2,
                "result": 1
            },
            {
                "name": "even elements array -> switch",
                "array": [1, 2, 4, 5],
                "target": 3,
                "result": 2
            },
            {
                "name": "even elements array -> append",
                "array": [1, 2, 4, 5],
                "target": 6,
                "result": 4
            },
        ]

        for case in cases:
            with self.subTest(name=case['name'], array=case['array'], target=case['target'], result=case['result']):
                result = BinarySearchLeft(case['array'], case['target'])
                self.assertEqual(
                    result, case["result"],
                    msg=(
                        f"FAIL: Неверный результат поиска места для вставки.\n"
                        f"Ожидалось: {case["result"]}\n"
                        f"Получено:  {result}"
                    )
                )
                

if __name__ == "__main__":
    unittest.main()