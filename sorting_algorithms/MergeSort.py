def merge(left, right):
    result = []
    while left and right:
        if left[0] < right[0]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))
    # while left:
    #     result.append(left.pop(0))
    # while right:
    #     result.append(right.pop(0))
    arr_non_empty = left if left else right  # equivalent expression vs above
    while arr_non_empty:
        result.append(arr_non_empty.pop(0))
    return result


def merge_sort(arr):
    if len(arr) < 2:
        return arr
    arr_len = int(len(arr) / 2)

    return merge(merge_sort(arr[:arr_len]), merge_sort(arr[arr_len:]))


test_arr = [5, 1, 23, 3, 1, 2, 3, 1, 123, 324, 51123, 23, 1, 1, 2, 3, 4, 5]
test_arr = merge_sort(test_arr)
print(test_arr)
