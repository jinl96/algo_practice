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


def quickSort(arr, low, high):
    if low < high:
        pivot = partition(arr, low, high)
        quickSort(arr, low, pivot)
        quickSort(arr, pivot + 1, high)
    return arr

arr_test = quickSort([5,12312,123,12,1,33,2], 0, 6)
print(arr_test)