import sys

G = int(input())
P = int(input())

gates = [i for i in range(1, G+1)]

planes = []

for i in range(P):
    gi = int(input())
    planes.append(gi)

planes.sort()
