def partition(low, high, arr):
    i, j = low, high
    while i < j:
        while arr[j] >= arr[low] and i < j:
            j -= 1
        while arr[i] <= arr[low] and i < j:
            i += 1
        arr[i], arr[j] = arr[j], arr[i]
    arr[low], arr[j] = arr[j], arr[low]
    return j

def quick_sort(arr, low=None, high=None, dsc=False):
    if len(arr) < 2:
        return arr
    low = 0 if not isinstance(low, (int, float)) else low
    high = len(arr) - 1 if not isinstance(high, (int, float)) else high
    if low < high:
        if dsc:
            pivot = des_partition(low, high, arr)
            quick_sort(arr, low, pivot, dsc=True)
            quick_sort(arr, pivot + 1, high, dsc=True)
        else:
            pivot = partition(low, high, arr)
            quick_sort(arr, low, pivot)
            quick_sort(arr, pivot + 1, high)
    return arr


def des_partition(high, low, arr):
    i, j = high, low

    while i < j:
        while i < j and arr[j] <= arr[high]:
            j -= 1
        while i < j and arr[i] >= arr[high]:
            i += 1
        arr[i], arr[j] = arr[j], arr[i]
    arr[high], arr[j] = arr[j], arr[high]
    return j


def des_quick_sort(arr, high=None, low=None):
    if len(arr) < 2:
        return arr
    high = 0 if not isinstance(high, (int, float)) else high
    low = len(arr) - 1 if not isinstance(low, (int, float)) else low
    if low > high:
        pivot = des_partition(high, low, arr)
        des_quick_sort(arr, high, pivot)
        des_quick_sort(arr, pivot + 1, low)
    return arr


test_arr = [5, 1, 23, 3, 1, 2, 3, 1, 123, 324, 51123, 23, 1, 1, 2, 3, 4, 5]
# test_arr = quick_sort(test_arr)
des_arr = quick_sort(test_arr)
# print(test_arr)
print(des_arr)

