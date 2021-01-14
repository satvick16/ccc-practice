import sys

K = int(input())

friends = [i for i in range(1, K + 1)]

m = int(input())

rounds = []

for i in range(m):
    round_ = int(input())
    rounds.append(round_)

def removal(friends, rounds):
    if len(rounds) == 0:
        for friend in friends:
            print(friend)
        sys.exit()

    to_del = []

    for i in range(len(friends)):
        if (i + 1) % rounds[0] == 0:
            to_del.append(friends[i])
    
    for j in to_del:
        friends.remove(j)

    rounds.pop(0)
    
    removal(friends, rounds)

friends = removal(friends, rounds)
