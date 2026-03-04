# Additional problem of finding 
# the longest strictly monotonous sequence

# [7, 1, 2, 3, 0, 4, 5, 6, 5] -> [1, 2, 3, 4, 5, 6]

def StrictlyMonotonousSequence(array : list[int]) -> list[int]:
    if len(array) <= 1:
        return array
    
    return