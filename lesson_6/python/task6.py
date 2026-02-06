# t = O(n), n = len(M)
# mem = O(1)
def ArrayChunk(M, left, right):
    basic_indx = (left + right) // 2

    if right - left + 1 < 2:
        return basic_indx
    
    i1, i2 = left, right
    N = M[basic_indx]

    while i1 < i2 - 1:
        
        while M[i1] < N:
            i1+=1

        while M[i2] > N:
            i2-=1
        
        if M[i1] == N:
            basic_indx = i1
        
        if M[i2] == N:
            basic_indx = i2
        
        if i1 == i2 - 1:
            break

        M[i1], M[i2] = M[i2], M[i1]
    
    if M[i1] > M[i2]:
        M[i1], M[i2] = M[i2], M[i1]
        basic_indx = ArrayChunk(M, left, right)

    if i1 == i2 or (i1 == i2 - 1 and M[i1] < M[i2]):
        return basic_indx

    return basic_indx

# t = O(n*log(n)), n - len of array
# m = O(log(n))
def QuickSortTailOptimization(array : list[int], left : int, right : int):
    size = len(array)
    if size < 2:
        return

    while left < right:
        basic_indx = ArrayChunk(array, left, right)

        if basic_indx - left < right - basic_indx: # если опорный указатель больше выпал а левую сторону -> идем влево
            QuickSortTailOptimization(array, left, basic_indx-1)
            left = basic_indx + 1 # обновляем, чтобы потом уйти в правую часть
        else: # иначе вправо
            QuickSortTailOptimization(array, basic_indx+1, right)
            right = basic_indx - 1 # здесь чтобы уйти в левую часть