from itertools import combinations
import copy
import sys

S = input()

counter = 1 + len(S)

if len(S) == len(set(S)):
    counter += 1

for i in range(2, len(S)):
    for j in combinations(S, i):
        if len(j) == len(set(j)):
            counter += 1

sys.stdout.write(str(counter % (10 ** 9 + 7)) + "\n")
