def partition(arr, low, high):
    pivot = arr[low]
    i, j = low, high

    while i < j:
        while i < j and arr[j] >= pivot:
            j -= 1
        while i < j and arr[i] <= pivot:
            i += 1
        arr[i], arr[j] = arr[j], arr[i]
    arr[low], arr[j] = arr[j], arr[low]
    return j


def quicksort(arr, low, high):
    if low < high:
        pivot = partition(arr, low, high)
        quicksort(arr, low, pivot)
        quicksort(arr, pivot + 1, high)
    return arr


def quick_sort(arr):
    return quicksort(arr, 0, len(arr) - 1)


test_arr = [5, 1, 23, 3, 1, 2, 3, 1, 123, 324, 51123, 23, 1, 1, 2, 3, 4, 5]
test_arr = quick_sort(test_arr)
print(test_arr)

