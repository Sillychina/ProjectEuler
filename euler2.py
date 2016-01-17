sum = 0
fib1 = 1
fib2 = 2
fib3 = 3
while (fib2 < 4000000):
    sum+=fib2
    fib1 = fib2 + fib3
    fib2 = fib1 + fib3
    fib3 = fib2 + fib1
print sum
