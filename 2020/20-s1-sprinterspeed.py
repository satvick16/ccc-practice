N = int(input())

obs = []

for i in range(N):
    t, x = input().split()
    obs.append([t, x])

observations = sorted(obs, key=lambda obs:int(obs[0]))

speeds = []

for j in range(len(observations) - 1):
    time_diff = int(observations[j+1][0]) - int(observations[j][0])
    distance = int(observations[j+1][1]) - int(observations[j][1])
    speeds.append(abs(distance / time_diff))

print(max(speeds))
