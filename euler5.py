def otherFactor(num, jackson):
    largestFact = 0
    for i in range (jackson, 0, -1):
        if jackson%i == 0 and num%i == 0:
            return jackson/i

product = 1
for i in range (1, 20):
    product = product * otherFactor(product, i)

print product
