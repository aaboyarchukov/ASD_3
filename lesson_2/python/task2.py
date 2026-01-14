# t = O(n // step), where n = len(array) 
# mem = O(1)
def find_position(array, start, stop, step):
    init_pos = start
    while start > stop and array[start - step] > array[init_pos]:
        start -= step

    return start

# t = O(n // step), where n = len(array) 
# mem = O(1)
def insert_at_position(array, position_from, position_to, step):
    target_value = array[position_from]
    target_position = position_to

    while position_to < position_from:
        array[position_from] = array[position_from - step]
        position_from -= step
    
    array[target_position] = target_value
    print(array)

# t = O(((n - i) // step) ^ 2), where n = len(array) 
# mem = O(1)
def InsertionSortStep(array, step, i):
    for indx in range(i + step, len(array), step):
        target_position = find_position(array, indx, i, step)
        insert_at_position(array, indx, target_position, step)


