import unittest
from task9 import HeapSort

def build_heap_sort(array) -> HeapSort:
    heap = HeapSort()
    heap.HeapSort(array)

    return heap

class TestHeapSort(unittest.TestCase):
    def test_build_heap_sort(self):
        cases = [
            ["empty heap", [], build_heap_sort([])],
            ["one element heap", [1], build_heap_sort([1])],
            ["even elements heap", [1, 2, 4, 3], build_heap_sort([1, 2, 4, 3])],
            ["odd elements heap", [1, 2, 4, 3, 8], build_heap_sort([1, 2, 4, 3, 8])],
        ]
        
        for name, init_array, heap in cases:
             with self.subTest(name=name, array=init_array):
                heap_elements = []
                while heap.HeapObject.size > 0:
                    heap_elements.append(heap.HeapObject.GetMax())
                
                self.assertEqual(
                    sorted(heap_elements), sorted(init_array),
                    msg=(
                        f"FAIL: HeapSort неверно построено дерево.\n"
                        f"Ожидалось: {init_array}\n"
                        f"Получено:  {heap_elements}"
                    )
                )

class TestGetNextMax(unittest.TestCase):
    def test_get_max(self):
        cases = [
            ["get max empty heap", [], build_heap_sort([]), [-1]],
            ["get max one element heap", [1], build_heap_sort([1]), [1]],
            ["get max even elements heap", [1, 2, 4, 3], build_heap_sort([1, 2, 4, 3]), [4]],
            ["get max odd elements heap", [1, 2, 4, 3, 8], build_heap_sort([1, 2, 4, 3, 8]), [8]],
            ["consecutively get max elements", [1, 2, 4, 3, 8], build_heap_sort([1, 2, 4, 3, 8]), [8, 4, 3, 2, 1]],
            ["consecutively get max elements with ending", [1, 2, 4, 3, 8], build_heap_sort([1, 2, 4, 3, 8]), [8, 4, 3, 2, 1, -1]],
        ]
        
        for name, init_array, heap, elements in cases:
             with self.subTest(name=name, array=init_array, max_elements=elements):
                max_elements = []
                for _ in range(len(elements)):
                    max_elements.append(heap.HeapObject.GetMax())
                
                self.assertEqual(
                    max_elements, elements,
                    msg=(
                        f"FAIL: HeapSort неверно построено дерево.\n"
                        f"Ожидалось: {elements}\n"
                        f"Получено:  {max_elements}"
                    )
                )

if __name__ == "__main__":
    unittest.main()