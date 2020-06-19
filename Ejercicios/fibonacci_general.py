from math import sqrt, modf

def fibonacci(n: int) -> int:
    sqrt_5 = sqrt(5)
    phi = (1+sqrt_5) / 2
    to_return = phi**n/sqrt_5
    return to_return

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

for i in range(15):
    entero , decimal =  modf(fibonacci(i))
    dynamic =  dynamic_fibonacci(i)
    comp =  abs(entero - dynamic)
    if comp:
        print(i, entero, decimal, dynamic) 


print('%.0f'% fibonacci(7))
print(dynamic_fibonacci(7))
