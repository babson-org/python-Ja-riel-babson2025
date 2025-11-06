def combine(left, right):
    array = []
    l_cur = 0
    r_cur = 0

    cnt = 0

    while l_cur < len(left) and r_cur < len(right):
        if left[l_cur] < right[r_cur]:
            array.append(left[l_cur]) 
            l_cur += 1
        else: 
            array.append(right[r_cur]) 
            r_cur += 1

return array + left[l_cur:] + right[r_cur:]


from combine import combine as cx

def combine_sort(unsorted):
    unsorted = [5, 4, 3, 2, 1]
    size = len(unsorted)
    left = unsorted[0:1]
    for idx in range(1, size):
        right = unsorted[idx : idx + 1]
        left = cx(left, right)
    return left





