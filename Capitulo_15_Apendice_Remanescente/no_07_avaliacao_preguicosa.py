def nth_prime(n):
    count = 0

    for prime in list_of_primes():
        count += 1
        if count == n:
            return prime


def get_prime(n):
    if n == 1:
        return 2

    count = 1
    number = 1
    while count < n:
        number += 2
        if is_prime(number):
            count += 1
    return number


def is_prime(n):
    if n == 2:
        return True
    if n == 1 or n % 2 == 0:
        return False
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True


def list_of_primes():
    next = 1
    while True:
        next_prime = get_prime(next)
        next = next + 1
        yield next_prime
