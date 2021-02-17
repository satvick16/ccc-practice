avail = list(map(int, input().split()))
ppl = list(map(int, input().split()))

counter = 0

for i in range(8):
    if avail[i] == ppl[i]:
        x = avail[i]
        avail[i] = 0
        ppl[i] = 0
        counter += x
    elif avail[i] < ppl[i]:
        x = avail[i]
        avail[i] = 0
        ppl[i] -= x
        counter += x
    else:
        x = ppl[i]
        ppl[i] = 0
        avail[i] -= x
        counter += x

def solve(p, a, ppl, avail, counter):
    if ppl[p] == avail[a]:
        x = ppl[p]
        ppl[p] = 0
        avail[a] = 0
        counter += x
    elif ppl[p] < avail[a]:
        x = ppl[p]
        ppl[p] = 0
        avail[a] -= x
        counter += x
    else:
        x = avail[a]
        avail[a] = 0
        ppl[p] -= x
        counter += x

    return ppl, avail, counter

ppl, avail, counter = solve(1, 0, ppl, avail, counter)

ppl, avail, counter = solve(2, 0, ppl, avail, counter)

ppl, avail, counter = solve(3, 2, ppl, avail, counter)
ppl, avail, counter = solve(3, 1, ppl, avail, counter)
ppl, avail, counter = solve(3, 0, ppl, avail, counter)

ppl, avail, counter = solve(4, 0, ppl, avail, counter)

ppl, avail, counter = solve(5, 3, ppl, avail, counter)
ppl, avail, counter = solve(5, 1, ppl, avail, counter)
ppl, avail, counter = solve(5, 0, ppl, avail, counter)

ppl, avail, counter = solve(6, 4, ppl, avail, counter)
ppl, avail, counter = solve(6, 2, ppl, avail, counter)
ppl, avail, counter = solve(6, 0, ppl, avail, counter)

ppl, avail, counter = solve(7, 6, ppl, avail, counter)
ppl, avail, counter = solve(7, 5, ppl, avail, counter)
ppl, avail, counter = solve(7, 4, ppl, avail, counter)
ppl, avail, counter = solve(7, 3, ppl, avail, counter)
ppl, avail, counter = solve(7, 2, ppl, avail, counter)
ppl, avail, counter = solve(7, 1, ppl, avail, counter)
ppl, avail, counter = solve(7, 0, ppl, avail, counter)

print(counter)
