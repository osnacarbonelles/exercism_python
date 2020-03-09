from math import ceil, log

def sieve(xs):
    primes = []
    while xs:
        primes += [xs[0]]
        xs = list(filter(lambda x: x % xs[0], xs))
    return primes

def nth_prime(n):
    if n < 1:
        raise ValueError
    return sieve(range(2, (30 if n < 10 else ceil(n * log(n) + n * log(log(n)))) + 1))[n - 1]
