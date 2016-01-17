sumOfSquares = 0
squareOfSums = 0

sum = 0
for i in range (101):
    sum+= i

squareOfSums = pow(sum, 2)

for i in range (101):
    sumOfSquares += pow(i, 2)

print sumOfSquares - squareOfSums

