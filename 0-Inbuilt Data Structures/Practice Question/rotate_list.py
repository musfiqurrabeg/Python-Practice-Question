def rotate_list(lst, k):
    if not lst or k == 0:
        return lst.copy() if lst else lst
    n = len(lst)
    k = k % n
    rotated = []
    
    for i in range(n - k, n):
        rotated.append(lst[i])
    
    for i in range(n - k):
        rotated.append(lst[i])
    return rotated
