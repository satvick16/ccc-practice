J = int(input())
A = int(input())

# [size, number]

available = []

for i in range(J):
    size = input()

    if size == "S":
        available.append([1, i+1])
    elif size == "M":
        available.append([2, i+1])
    else:
        available.append([3, i+1])

requests = []

for j in range(A):
    request = list(input().split())

    if request[0] == "S":
        requests.append([1, int(request[1])])
    elif request[0] == "M":
        requests.append([2, int(request[1])])
    else:
        requests.append([3, int(request[1])])

total = 0

for request in requests:
    things = [item[1] for item in available]
    
    if request[1] in things:
        if request[0] <= things[things.index(request[1])]:        
            total += 1
            available.pop(things.index(request[1]))

print(total)
