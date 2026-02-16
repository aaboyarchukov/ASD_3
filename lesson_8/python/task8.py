# t = O(n), mem = O(n)
def merge(left : list[int],  right : list[int]) -> list[int]:
    result = []
    left_indx = 0
    right_indx = 0

    while left_indx < len(left) and right_indx < len(right):
        if left[left_indx] > right[right_indx]:
            result.append(right[right_indx])
            right_indx += 1
        else:
            result.append(left[left_indx])
            left_indx += 1
    
    while left_indx < len(left):
        result.append(left[left_indx])
        left_indx+=1
    
    while right_indx < len(right):
        result.append(right[right_indx])
        right_indx+=1
    
    return result

# t = O(n * log(n)), mem = O(n) 
def MergeSort(array : list[int]) -> list[int]:
    size = len(array)
    if size < 2:
        return array
    
    left, right = 0, size-1
    middle = (left + right) // 2

    left = MergeSort(array[left:middle+1])
    right = MergeSort(array[middle+1:right+1])

    print(left, right)
    return merge(left, right)

    



