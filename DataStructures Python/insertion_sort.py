def insertionSort(arr):
    i,j =0, 0
    for i in range(len(arr)):
        key = arr[i]
        j = i-1
        while arr[j] > key and j>=0:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key


arr = [9,8,7,6,5,4,3,2,1]
insertionSort(arr)
print(arr)