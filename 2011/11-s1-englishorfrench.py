N = int(input())

text = []

for i in range(N):
    line = input()
    text.append(line)

s = 0
t = 0

for line in text:
    s += line.count("s")
    s += line.count("S")
    t += line.count("t")
    t += line.count("T")

if s > t or s == t:
    print("French")
else:
    print("English")
