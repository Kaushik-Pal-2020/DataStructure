def binaryToDecimal(arr):
    arr = str(arr)
    arr = arr[::-1]
    length = len(arr)-1
    if int(arr[length]) != 1:
        length -= 1
    count = 0
    for i in range(length,-1,-1):
        count += int(arr[i])*(2**i)

    return count


def binaryToDecimal2(value):
    return  int(str(value),2)


def binaryToDecimal3(value):
    count, i  = 0, 0
    while value>0:
        digit = value%10
        count += (digit << i)
        value //= 10
        i += 1

    return count   





print(binaryToDecimal3(1011001))