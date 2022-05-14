def merge(left, right):
    result = []

    while left and right:
        if left[0] <= right[0]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))
    while left:
        result.append(left.pop(0))
    while right:
        result.append(right.pop(0))
    return result


def merge_sort(arr):
    if len(arr) < 2:
        return arr
    arr_length = int(len(arr)/2)

    left = arr[:arr_length]
    right = arr[arr_length:]

    return merge(merge_sort(left), merge_sort(right))


test_arr = [5, 1, 23, 3, 1, 2, 3, 1, 123, 324, 51123, 23, 1, 1, 2, 3, 4, 5]
test_arr = merge_sort(test_arr)
print(test_arr)
