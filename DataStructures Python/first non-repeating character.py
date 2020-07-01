from collections import Counter


def allNonRepeating(string):
    char = set(string[0])
    for i in range(len(string)):
        char ^= set(string[i])

    print(char)


def firstNonRepeating(string):
    c = Counter(string)
    for s in string:
        if c[s] == 1:
            print(s)
            return


firstNonRepeating("geeksforgeeks")
