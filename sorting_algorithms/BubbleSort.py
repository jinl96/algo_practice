def bubble_sort(arr):
    swapped = True

    while swapped:
        prev = arr[0]
        swapped = False
        for i in range(1, len(arr)):
            if arr[i] < prev:
                arr[i - 1], arr[i] = arr[i], arr[i - 1]
                swapped = True
            prev = arr[i]
    return arr


test_arr = [5, 1, 23, 3, 1, 2, 3, 1, 123, 324, 51123, 23, 1, 1, 2, 3, 4, 5]
test_arr = bubble_sort(test_arr)
print(test_arr)
