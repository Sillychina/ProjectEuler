import math
num = 600851475143
largestFact = 0
while(num != 1):
    for i in range (2, num):
        if(num % i == 0):
            num = num /i
            if i > largestFact:
                largestFact = i
            break
print largestFact
