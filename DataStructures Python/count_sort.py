def countSort(arr):
    maxx = max(arr)
    Hash = [0]*(maxx+1)
    for value in arr:
        Hash[value] += 1
    i, j = 0, 0
    while i <= maxx:
        if Hash[i] > 0:
            arr[j] = i
            Hash[i] -= 1
            j += 1
        else:
            i += 1


base_arr = [-5, -10, 0, -3, 8, 5, -1, 10]
countSort(base_arr)
print(base_arr)
