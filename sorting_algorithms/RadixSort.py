def radix_sort(arr):
    # n = digit size of largest number
    n = len(str(max(arr)))
    for i in range(0, n):
        temp = [[] for _ in range(0, 10)]
        after_arr = []
        for j in arr:
            temp[j // (10 ** i) % 10].append(j)
        arr = [j for i in temp for j in i]
        # expression below equals to the line above
        # for sub_arr in temp:
        #     for ele in sub_arr:
        #         after_arr.append(ele)
        # arr = after_arr
    return arr

test_arr = [5, 1, 23, 3, 1, 2, 3, 1, 123, 324, 51123, 23, 1, 1, 2, 3, 4, 5]
test_arr = radix_sort(test_arr)
print(test_arr)
