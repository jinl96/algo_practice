def insertion_sort(arr):
    for i in range(1, len(arr)):
        cur = arr[i]
        prev_index = i - 1

        while arr[prev_index] > cur and prev_index >= 0:
            arr[prev_index + 1] = arr[prev_index]
            prev_index -= 1

        arr[prev_index + 1] = cur
    return arr

test_arr = [5, 1, 23, 3, 1, 2, 3, 1, 123, 324, 51123, 23, 1, 1, 2, 3, 4, 5]
test_arr = insertion_sort(test_arr)
print(test_arr)
