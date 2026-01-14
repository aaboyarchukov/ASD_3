# Рефлексия

Виды базовых сортировок:

1. Сортировка выбором

```
алогоритм:
- идем от i-го элемента до n и меняем его с минмальном на данном отрезке, начиная с i+1 элемента (то есть идет поиск минимума)
- повторяем алгоритм до тех пор, пока не понадобится менять элементы местами
```

Минус: выполнение поиска минимального элемента

2. Пузырьковая сортировка

```
алогоритм:
- идем от i-го элемента до n-1 и меняем его каждый раз с меньшим элементом, то есть если текущий элемент больше
- повторяем алгоритм до тех пор, пока не понадобится менять элементы местами
```

Минус: большое количество итераций

3. Сортировка вставками

```
алгоритм:
- проходим от i-го элемента до n-1 и вставляем его на нужное место в предыдущей последовательности, то есть между двумя объектами с сохранением упорядоченности
- повторяем алгоритм до тех пор, пока не понадобится вставлять элементы в нужные места
```

Данные алгоритмы сортировки являются базовыми, так как применяют простые и неоптимизированные алгоритмы для сортировки структуры, из-за этого сложность данных алгоритмов квадратичная $O^2$ в худшем случае.

**Важность использования эффективных алгоритмов** заключается в том, что мы можем оптимизировать работу или увеличить производительность алгоритма даже на железе, которое будет сильно обрезанным в плане ресурсов.
## Задания

1. Реализуйте функцию для одного шага сортировки выбором, которая получает на вход массив целых чисел (передаётся по ссылке) и номер элемента i (i >= 0), и меняет в этом массиве i-й элемент местами с минимальным элементом в оставшейся части массива, начиная с элемента i+1.

```python
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
```

2. Реализуйте функцию для одного шага сортировки пузырьком, которая получает на вход массив целых чисел (передаётся по ссылке), и выполняет один пробег по массиву от начала к концу, меняя местами каждые два элемента i и i+1, если i-й элемент больше i+1-го. Функция возвращает true, если по окончании пробега не было ни одного обмена элементов.

```python
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
```

3. Реализуйте предварительный алгоритм для сортировки вставками с дополнительным параметром -- шагом сортировки - реализуйте функцию для одного шага сортировки вставкой (по возрастанию), которая получает на вход массив целых чисел (передаётся по ссылке), размер шага (>= 1) и номер элемента i (i >= 0), с которого выполняется один шаг сортировки.

```python
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
```

На данном занятии мы познакомились с основными видами базовых сортировок.