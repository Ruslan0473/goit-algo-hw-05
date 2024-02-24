def caching_fibonacci():
    cache=dict()

    def fibonacci(n):
        if n <= 0:
            return 0
        if n == 1:
            return 1
        if n in cache:
            return cache[n]

        cache[n] = fibonacci(n - 1) + fibonacci(n - 2)
        return cache[n]

    return fibonacci


fib=caching_fibonacci()

print(fib(9))
print(fib(15))