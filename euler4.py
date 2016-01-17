def makePalindrome(n):
    strPal = str(n)
    strPal = strPal + strPal[::-1]
    return int(strPal)

def isPal(n):
    string = str(n)
    if len(string) < 6:
        return False
    for i in range(0, 3):
        if(string[i] != string[5-i]):
            return False
    return True



numFound = 111
iVal = 0
jVal = 0
prePal = 0
for i in range(999, numFound, -1):
    for j in range(999, numFound, -1):
        if isPal(i*j) and prePal < i*j:
            prePal = i*j
            numFound = pow(i*j, 1/2)
            iVal = i
            jVal = j
print prePal
