import math
def largestPrimeFactor(num):
    largestPrime = -1
    while num % 2 == 0:
        largestPrime = 2
        num /= 2
    while num % 3 == 0:
        largestPrime = 3
        num /= 3
    for i in range(5, int(math.sqrt(num)) + 1, 6):
        while num % i == 0:
            largestPrime = i
            num /= i
        while num % (i+2) == 0:
            largestPrime = i+2
            num /= i+2
    if num > 4:
        largestPrime = num
    return largestPrime

print(largestPrimeFactor(600851475143))