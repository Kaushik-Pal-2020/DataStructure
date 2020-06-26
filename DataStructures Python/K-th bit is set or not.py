# Using Left shift
"""
1) Left shift given number 1 by k-1 to create 
   a number that has only set bit as k-th bit.
    temp = 1 << (k-1)
2) If bitwise AND of n and temp is non-zero, 
   then result is SET else result is NOT SET.


 n = 75 and k = 4
 temp = 1 << (k-1) = 1 << 3 = 8 
 Binary Representation of temp = 0...00001000 
 Binary Representation of n =    0...01001011 
                            &(X)
                            -----------------
                                 0...00001000      
 Since bitwise AND of n and temp is non-zero,
 result is SET.
"""


def isKthBitSet(n, k):
    if n & (1 << (k - 1)):
        print("SET")
    else:
        print("NOT SET")


# Driver code
n = 5
k = 1
isKthBitSet(n, k)

# Using Right Shift
"""
temp = num >> (k-1)
if temp & 1 == 1 :
    yes
else:
    No
"""


def isKthBitSet2(n, k):
    if ((n >> (k - 1)) and 1):
        print("SET")
    else:
        print("NOT SET")


# Driver code
n, k = 5, 1
isKthBitSet2(n, k)
