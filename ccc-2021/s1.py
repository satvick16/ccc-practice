N = int(input())

hs = list(map(int, input().split()))
ws = list(map(int, input().split()))

a = 0

for i in range(len(ws)):
    a += ws[i] / 2 * (hs[i] + hs[i+1])

print(a)
