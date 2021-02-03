from itertools import permutations

N = input()
H = input()

perms1 = [''.join(p) for p in permutations(N)]
perms = set(perms1)

counter = 0
seen = []

for i in range(len(H) - len(N) + 1):
    if H[i:i+len(N)] in perms:
        counter += 1
        perms.remove(H[i:i+len(N)])
    if len(perms) == 0:
        break

print(counter)
