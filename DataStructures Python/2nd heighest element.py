# if array is not sorted
def unsorted_element(arr, n):
    maxx, second_maxx = arr[0], arr[0]
    flag = 0
    for i in range(1, n):

        if maxx < arr[i]:
            second_maxx = maxx
            maxx = arr[i]
            flag = 1

        elif arr[i] > second_maxx and arr[i] != maxx:
            second_maxx = arr[i]
            flag = 1

    if flag == 1:
        return second_maxx
    return False

# if array is sorted


print(unsorted_element([4, 4, 4, 4, 4], 5))
