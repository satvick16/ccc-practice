def ways(friends, n, x):
    answer = 1

    for y in range(n-1):
        if friends[y] == x:
            answer = answer * (1 + ways(friends, n, y+1))

    return answer

n = int(input())

friends = []

for i in range(1, n):
    friends.append(int(input()))
    
print(ways(friends,n,n))
