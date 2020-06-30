from collections import deque, defaultdict

# my code


def countWindowDistinct(arr, k):
    queue = deque()
    # inserting first k-1 elements
    for i in range(k-1):
        queue.append(arr[i])
    # appending , print, poping
    i = k-1
    while i < len(arr):
        queue.append(arr[i])
        print(len(set(queue)), end=' ')
        queue.popleft()
        i += 1
    print()


countWindowDistinct([1, 2, 1, 3, 4, 2, 3], 4)


def countDistinct(arr, k, n):

        # Creates an empty hashmap hm
    mp = defaultdict(lambda: 0)

    # initialize distinct element
    # count for current window
    dist_count = 0

    # Traverse the first window and store count
    # of every element in hash map
    for i in range(k):
        if mp[arr[i]] == 0:
            dist_count += 1
        mp[arr[i]] += 1

    # Print count of first window
    print(dist_count, end=' ')

    # Traverse through the remaining array
    for i in range(k, n):

        # Remove first element of previous window
        # If there was only one occurrence,
        # then reduce distinct count.
        if mp[arr[i - k]] == 1:
            dist_count -= 1
        mp[arr[i - k]] -= 1

    # Add new element of current window
    # If this element appears first time,
    # increment distinct element count
        if mp[arr[i]] == 0:
            dist_count += 1
        mp[arr[i]] += 1

        # Print count of current window
        print(dist_count, end=' ')


arr = [1, 2, 1, 3, 4, 2, 3]
n = len(arr)
k = 4
countDistinct(arr, k, n)

# another my code


def countWindowDistinct2(arr, k):
    s = str(map(str, arr))
    base_s = ''
    print(s)
    for i in range(k-1):
        base_s += s[i]

    for i in range(k-1, len(arr)):
        base_s += s[i]
        print(len(set(s)))
        base_s = base_s[i:]


countWindowDistinct2(arr, k)
