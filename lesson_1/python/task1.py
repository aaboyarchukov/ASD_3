# 1. get func of get min of two element
def index_of_min(a, indx_a, b, indx_b):
    if a < b:
        return indx_a
    return indx_b

# 2. get func of get index of min element
def indx_of_min_in_array(array, start_indx):
    result = start_indx
    while start_indx < len(array):
        result = index_of_min(array[result], result, array[result + 1], result + 1)
        start_indx += 1
    return result

# 3. get fnuc if selection sort step
def SelectionSortStep(array : list, i : int):
    indx_min = indx_of_min_in_array(array, i)
    array[i], array[indx_min] = array[indx_min], array[i]