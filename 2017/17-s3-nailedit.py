import sys
import copy

N = int(input())

Ls = list(input().split())

for i in range(len(Ls)):
    Ls[i] = int(Ls[i])

Ls.sort()
heights = []

for i in range(len(Ls)-1):
    for j in range(1, len(Ls)):
        heights.append(Ls[i]+Ls[j])

setheights = set(heights)

dictheights = {}

for i in setheights:
    dictheights[i] = []

for i in range(len(Ls)-1):
    for j in range(1, len(Ls)):
        x = [Ls[i], Ls[j]]
        x.sort()
        if x not in dictheights[Ls[i]+Ls[j]]:
            dictheights[Ls[i]+Ls[j]].append(x)

max_occurences = max([len(i) for i in dictheights.values()])

temp_dictheights = copy.deepcopy(dictheights)

for i, j in temp_dictheights.items():
    if len(j) == max_occurences:
        del temp_dictheights[i]
        break

