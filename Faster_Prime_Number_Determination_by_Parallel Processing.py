import multiprocessing

def is_prime(n):
    if n <= 1:
        return 
    elif n <= 3:
        return n
    elif n % 2 == 0 or n % 3 == 0:
        return 
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return 
        i += 6
    return n

def find_primes(numbers):
    with multiprocessing.Pool() as pool:
        return pool.map(is_prime, numbers)

if __name__ == '__main__':
    numbers = list(range(1, 1000001))
    primes = find_primes(numbers)
    filtered_primes = [x for x in primes if x]
    print(filtered_primes)
    print(len(filtered_primes))
    # print(sum(primes))
