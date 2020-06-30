from collections import Counter


def firstRepeating(string):
    c = Counter(string)
    if len(string) < 2:
        return -1
    for s in string:
        if c[s] > 1:
            return s
    return -1


s = "abcd"
value = firstRepeating(s)
print(value)
