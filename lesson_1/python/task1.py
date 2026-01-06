# 1. get func of get min of two element
def index_of_min(a, indx_a, b, indx_b):
    if a < b:
        return indx_a
    return indx_b

# 2. get func of get index of min element
def indx_of_min_in_array(array, start_indx):
    result = start_indx
    while start_indx < len(array) - 1:
        result = index_of_min(array[result], result, array[start_indx + 1], start_indx + 1)
        start_indx += 1
    return result

# 3. get func of selection sort step
# t = O(n), where n = len(array) 
# mem = O(1)
def SelectionSortStep(array : list, i : int):
    indx_min = indx_of_min_in_array(array, i)
    array[i], array[indx_min] = array[indx_min], array[i]

# 4. get func of bubble sort step
# t = O(n), where n = len(array) 
# mem = O(1)
def BubbleSortStep(array):
    default_switches = 0

    amount_switches = default_switches
    for indx in range(0, len(array) - 1):
        if array[indx] > array[indx + 1]:
            array[indx], array[indx + 1] = array[indx + 1], array[indx]
            amount_switches += 1
    
    return amount_switches == default_switches