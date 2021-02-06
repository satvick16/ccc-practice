import sys

N = int(input())

s1 = list(input().split())
s2 = list(input().split())

pairs = []

for i in range(len(s1)):
    pairs.append([s1[i], s2[i]])

for j in range(len(pairs)):
    if not([pairs[j][1], pairs[j][0]] in pairs):
        print("bad")
        sys.exit()

    if pairs[j][0] == pairs[j][1]:
        print("bad")
        sys.exit()

print("good")
