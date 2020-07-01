from itertools import permutations


def permu(string):
    p = permutations(string)
    print(*p)


permu("acb")
