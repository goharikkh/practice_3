import math


def is_prime(a):
    for i in range(2, int(math.sqrt(a))+1):
        if a % i == 0:
            return False
    return True


def smallest_prime(n):
    n += 1
    while not is_prime(n):
        n += 1
    return n


print(smallest_prime(23))
