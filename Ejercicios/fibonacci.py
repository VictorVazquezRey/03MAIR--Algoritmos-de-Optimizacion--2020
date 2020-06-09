def fibonacci(n:int)->int:
    if n < 0:
        raise ValueError('n must be a positive number')
    if n <= 1:
        return n

    return fibonacci(n-1) + fibonacci(n-2)

def dynamic_fibonacci(n:int)->int:
    if n < 0:
        raise ValueError('n must be a positive number')

    fib = []
    # Base cases
    fib.append(0)
    fib.append(1)

    for i in range(2, n + 1):
        fib.append(fib[1] + fib[0])
        fib.pop(0)

    return fib[1]


# El resultado debe ser 610
print(fibonacci(15))

print(dynamic_fibonacci(15))


