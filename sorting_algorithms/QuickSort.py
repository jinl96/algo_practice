def partition(low, high, arr):
    i, j = low, high

    while i < j:
        while i < j and arr[j] >= arr[low]:
            j -= 1
        while i < j and arr[i] <= arr[low]:
            i += 1
        arr[i], arr[j] = arr[j], arr[i]
    arr[low], arr[j] = arr[j], arr[low]
    return j


def quick_sort(arr, low=None, high=None):
    if len(arr) < 2:
        return arr
    low = 0 if not isinstance(low, (int, float)) else low
    high = 0 if not isinstance(high, (int, float)) else high
    if low < high:
        pivot = partition(low, high, arr)
        quick_sort(arr, low, pivot)
        quick_sort(arr, pivot + 1, high)
    return arr


test_arr = [5, 1, 23, 3, 1, 2, 3, 1, 123, 324, 51123, 23, 1, 1, 2, 3, 4, 5]
test_arr = quick_sort(test_arr)
print(test_arr)