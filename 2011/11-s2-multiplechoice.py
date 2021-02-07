N = int(input())

responses = []
key = []

for i in range(N):
    response = input()
    responses.append(response)

for j in range(N):
    item = input()
    key.append(item)

correct = 0

for k in range(N):
    if responses[k] == key[k]:
        correct += 1

print(correct)
