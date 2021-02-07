N, X = map(int, input().split())

A = list(map(int, input().split()))

A.sort()

triples = 0

for i in range(0, len(A) - 2):
    for j in range(i+1, len(A) - 1):
        for k in range(j+1, len(A)):
            if A[j] == X and (i<j<k):
                triples += 1

print(triples)
