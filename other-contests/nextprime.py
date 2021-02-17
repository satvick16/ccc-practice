import sys

N = int(sys.stdin.readline())

def is_prime(N):
    if N < 2:
        return False

    for i in range(2, int(N**0.5)+1):
        if N % i == 0:
            return False

    return True

while True:
    if is_prime(N):
        print(N)
        sys.exit()
    else:
        N += 1
