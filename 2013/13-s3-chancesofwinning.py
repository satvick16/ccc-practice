T = int(input())
G = int(input())

results = []

for i in range(G):
    result = list(map(int, input().split()))
    results.append(result)

games = [[1, 2],
         [1, 3],
         [1, 4],
         [2, 3],
         [2, 4],
         [3, 4]]

scores = {1: 0,
          2: 0,
          3: 0,
          4: 0}

for result in results:
    game = [result[0], result[1]]
    game.sort()
    games.remove(game)
    
    if result[2] == result[3]:
        scores[result[0]] += 1
        scores[result[1]] += 1
    elif result[2] > result[3]:
        scores[result[0]] += 3
    else:
        scores[result[1]] += 3

wins = 0

def search(scores, games, T):
    global wins
    
    if len(games) == 0:
        situation = []
        
        for key, value in scores.items():
            situation.append(value)

        if situation[T-1] == max(situation):
            if situation.count(max(situation)) == 1:
                wins += 1

        return
    
    if T in games[0]:
        for option in ["W", "L", "T"]:
            if option == "W":
                scores[T] += 3
                search(scores, games[1:], T)
                scores[T] -= 3
            elif option == "L":
                if games[0][0] == T:
                    scores[games[0][1]] += 3
                    search(scores, games[1:], T)
                    scores[games[0][1]] -= 3
                else:
                    scores[games[0][0]] += 3
                    search(scores, games[1:], T)
                    scores[games[0][0]] -= 3
            else:
                scores[games[0][0]] += 1
                scores[games[0][1]] += 1
                search(scores, games[1:], T)
                scores[games[0][0]] -= 1
                scores[games[0][1]] -= 1
    else:
        for option in ["W", "L", "T"]:
            if option == "W":
                scores[games[0][0]] += 3
                search(scores, games[1:], T)
                scores[games[0][0]] -= 3
            elif option == "L":
                scores[games[0][1]] += 3
                search(scores, games[1:], T)
                scores[games[0][1]] -= 3
            else:
                scores[games[0][0]] += 1
                scores[games[0][1]] += 1
                search(scores, games[1:], T)
                scores[games[0][0]] -= 1
                scores[games[0][1]] -= 1

    return wins

print(search(scores, games, T))
