def find_position(array, start, stop, step):
    result = start
    while start > stop:
        if array[start - step] < array[start] and array[start] <= array[start + step]:
            return start
        start -= step
    
    return result

def insert_at_position(array, position_from, position_to, step):
    target_value = array[position_from]
    target_position = position_to

    while position_to < position_from:
        array[position_to + step] = array[position_to]
        position_to += step
    
    array[target_position] = target_value

def InsertionSortStep(array, step, i):
    position = find_position(array, i + step, i, step)
    insert_at_position(array, i, position, step)