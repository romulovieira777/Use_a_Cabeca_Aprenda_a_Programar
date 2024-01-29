import time


cache = {}


def fibonacci(n):
    global cache

    if n in cache:
        return cache[n]

    if n == 0:
        result = 0
    elif n == 1:
        result = 1
    else:
        result = fibonacci(n - 1) + fibonacci(n - 2)

    cache[n] = result
    return result


start = time.time()

for number in range(0, 101):
    result = fibonacci(number)
    print(number, result)

finish = time.time()
duration = finish - start
print(f'Computed all 100 in {duration:.2f} seconds')
