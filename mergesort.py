def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    result = []
    while left and right:
        result.append(left.pop(0) if left[0] < right[0]
                      else right.pop(0))

    return result + left + right

arr = [5, 2, 8, 1, 3]
print("Sorted array:", merge_sort(arr))