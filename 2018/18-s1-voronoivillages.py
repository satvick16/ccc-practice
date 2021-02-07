N = int(input())

vis = []

for i in range(N):
    vi = int(input())
    vis.append(vi)

vis.sort()

neighbourhoods = []

for j in range(1, len(vis) - 1):
    ldist = (vis[j] - vis[j - 1]) / 2
    rdist = (vis[j + 1] - vis[j]) / 2
    neighbourhoods.append(float(ldist + rdist))

print(min(neighbourhoods))
