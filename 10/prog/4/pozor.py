def qsort(arr):
    if not arr:
        return arr
    else:
        left = []
        right = []
        pivot = arr[0]
        for elem in arr[1:]:
            if elem < pivot:
                left.append(elem)
            else:
                right.append(elem)
        left = qsort(left)
        right = qsort(right)
        return left + [pivot] + right
