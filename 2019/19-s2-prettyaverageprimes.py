def is_prime(n):
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

T = int(input())

nis = []

for i in range(T):
    ni = int(input())
    nis.append(ni)

for ni in nis:
    asbs = []
    
    twoni = 2 * ni
    
    for k in range(2, twoni//2):
        if is_prime(k) and is_prime(twoni - k):
            print(k, twoni - k)
            break
