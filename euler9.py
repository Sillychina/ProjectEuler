import math

def prime(n):
    if n == 2:
        return True
    for i in range (2, int(n/2)):
        if(n%i == 0):
            return False
    return True

sum = 0
for i in range (2000000):
    if(prime(i)):
        sum+=i

print sum
