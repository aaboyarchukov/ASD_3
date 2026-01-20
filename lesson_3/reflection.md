# Рефлексия

### Сортировка Шелла:

Данный вид сортировки быстрее базовых, которые мы проходили раннее, и в худшем случае выполняется:
#### **$O\left(n\cdot\log\left(n\right)^2\right)$**

Выполняется он за такую сложность благодаря формированию последовательности шагов сдвига - последовательность Кнута. С помощью данной последовательности мы до иссекания массива, будем сортировать диапазон значений через каждые `step` шагов, как до этого мы делали в сортировке вставками.

### Последовательность Кнута:

Для достижения нужной алгоритмической сложности, а также корректности сортировки необходимо выбрать нужную последовательность, такой выступает последовательность Кнута -- 

#### ..., 364, 121, 40, 13, 4, 1. 

Эта последовательность генерируется по формуле

#### **$N\left(i\right)=3\cdot N\left(i-1\right)+1$**

где **$N\left(0\right)$** - это самый первый шаг, единица.

## Задания

1. Дополните предыдущее задание функцией, которая по параметру n >= 0 (размер массива) вычислит нужную интервальную последовательность целых чисел (список для Python, List для C#, ArrayList для Java).

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

# t = O(((n - i) // step) ^ 2), where n = len(array) 
# mem = O(1)
def InsertionSortStep(array, step, i):
    for indx in range(i + step, len(array), step):
        target_position = find_position(array, indx, i, step)
        insert_at_position(array, indx, target_position, step)

# t = O(log(array_size))
# mem = O(log(array_size))
# because of the growth of geometric progression
def KnuthSequence(array_size):
    def N(n, storage):
        if n > array_size:
            return storage
        
        storage.append(n)

        return N(3 * n + 1, storage)

    result = N(1, [])

    return result[::-1]

# t = O(n * (log n)^2)
# mem = O(log(array_size)) - because of KnuthSequence
def ShellSort(array):
    size = len(array)
    sequence = KnuthSequence(size)
    for step in sequence:
        for indx in range(0, size):
            InsertionSortStep(array, step, indx)


```