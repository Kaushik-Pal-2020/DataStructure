from collections import deque

# Find subarray with given sum for -ve and +ve numbers
def subArray(arr, m):
    q = deque([arr[0]])
    start_index, stop_index = 0, 0
    i = 1
    while i < len(arr):
        if sum(q) == m:
            print(f"Sum found between indexes : {start_index} -> {stop_index}")
            return

        elif sum(q) < m:
            q.append(arr[i])
            stop_index += 1
            i += 1

        else:
            q.popleft()
            start_index += 1
    print("No subarray found")


# Python3 implementation to find the length 
# of longest subArray having sum k 
  
# function to find the longest 
# subarray having sum k
def lenOfLongSubarr(arr, m):
    q = deque([arr[0]])
    start_index, stop_index = 0, 0
    i = 1
    max_subarray = []
    while i < len(arr):
        if sum(q) == m:
            max_subarray.append(stop_index-start_index)
            q.clear()
            start_index = stop_index
            i -= 1

        elif sum(q) < m:
            q.append(arr[i])
            stop_index += 1
            i += 1

        else:
            q.popleft()
            start_index += 1


    print(f"Maximum length = {max(max_subarray)}")






subArray([10, 5, 2, 7, 1, 9],15)