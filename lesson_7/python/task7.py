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

# t = O(n), n = len(M)
# mem = O(1)
def KthOrderStatisticsStep(array : list[int], l : int, r : int, k : int) -> list[int, int]:
    size = len(array)
    if size == 0:
        return []
    
    if size == 1:
        return [l, r]
    
    basic_indx = ArrayChunk(array, l, r)
    
    if basic_indx == k:
        return [l, r]
    if basic_indx < k:
        return [basic_indx + 1, r]
    
    return [l, basic_indx-1] 