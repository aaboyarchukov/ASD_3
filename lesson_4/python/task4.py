# t = O(n), n = len(M)
# mem = O(1)
def ArrayChunk(M):
    size = len(M)
    if size < 2:
        return 0
    
    i1, i2 = 0, size-1
    basic_indx = size // 2
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
        basic_indx = ArrayChunk(M)

    if i1 == i2 or (i1 == i2 - 1 and M[i1] < M[i2]):
        return basic_indx

    return basic_indx
        


