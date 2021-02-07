N = int(input())

swifts = list(map(int, input().split()))
semaphores = list(map(int, input().split()))

swiftssum = 0
semaphoressum = 0
verdict = [0]

for i in range(len(swifts)):
    swiftssum += swifts[i]
    semaphoressum += semaphores[i]
    if swiftssum == semaphoressum:
        verdict.append(i+1)

print(max(verdict))
