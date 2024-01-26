import time


def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


for number in range(20, 55, 5):
    start = time.time()
    result = fibonacci(number)
    end = time.time()
    duration = end - start
    print(number, result, duration)
