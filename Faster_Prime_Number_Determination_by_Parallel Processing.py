# Pythonのmultiprocessingモジュールを使った並列処理による素数判定の高速化の例
# is_prime()関数で素数判定を行い、find_primes()関数で複数のプロセスを使って素数判定を並列処理する。
# multiprocessing.Pool()を使ってプロセスプールを作成し、pool.map()を使って並列処理を実行する。
# __name__ == '__main__'という条件で、このコードが直接実行された場合にのみ、find_primes()関数が実行される。
# 1から100万までの整数のうち、素数の数を求めることができる。
# 並列処理を使わない場合に比べて、処理時間が大幅に短縮されることがわかる。ただし、実行環境によっては、プロセス数を調整する必要がある場合がある。

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
