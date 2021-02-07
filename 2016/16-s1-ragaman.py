import string

s1_ = input()
s2_ = input()

s1 = list(s1_)
s2 = list(s2_)

for letter in string.ascii_lowercase:
    if s1.count(letter) < s2.count(letter):
        print("N")
        break
else:
    print("A")
