def quicksort(arr: list):
    if len(arr) <= 1:
        return arr
    else:
        left = []
        right = []
        pivot = 0
        for i in range(len(arr)):
            if i != pivot:
                if arr[i] <= arr[pivot]:
                    left.append(arr[i])
                else:
                    right.append(arr[i])
        left = quicksort(left)
        right = quicksort(right)
        res = []
        for elem in left:
            res.append(elem)
        res.append(arr[pivot])
        for elem in right:
            res.append(elem)
        return res
