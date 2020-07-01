from itertools import permutations


P = permutations("BACDGABCDA", 4)
print(len(P))
x = tuple("ABCD")
for p in P:
    if x == p:
        print("found")
