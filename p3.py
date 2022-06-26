# Finds the largest prime factor of a given number.
import math
def largestPrimeFactor(num):
    largestPrime = -1
    # First we will remove all even factors by repetetively dividing by 2. 
    while num % 2 == 0:
        largestPrime = 2
        num /= 2
    # We then divide by 3 repetetively
    while num % 3 == 0:
        largestPrime = 3
        num /= 3
    # We can then divide by factrs between 5 and the square root of the original number, since the largest prime factor cannot be greater than the square root of the number itself.
    # We can also increment our loop by 6 each time because we have already removed all factors of 2 and 3 and therefore 6.
    # The code will record the largest prime during this process.
    for i in range(5, int(math.sqrt(num)) + 1, 6):
        while num % i == 0:
            largestPrime = i
            num /= i
        while num % (i+2) == 0:
            largestPrime = i+2
            num /= i+2
    # Either the remaining factor will be the largest prime or the largest prime will already have been recorded.
    if num > 4:
        largestPrime = num
    return largestPrime

print(largestPrimeFactor(600851475143))
