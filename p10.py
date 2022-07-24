import math
import time
from traceback import format_exc

def sieveOfEratosthenes(upperBound):
    # creating a list of booleans to indicate whether each index represents a prime, initially set to true.
    primes = [True] * (upperBound + 1)
    # Setting 0 and 1 to non-prime
    primes[0], primes[1] = False, False
    # iterating from 2 to the square root of the given upperbound + 1
    for num in range(2, int(math.sqrt(upperBound)) + 1):
        # if the number is still listed as prime we will set all products of it which are less than the upper bound to non-prime. 
        # e.g. num = 3, set 9, 15, 21, 27... to non-prime (it would set 6, 12, 18... to prime but all even numbers were set to non-prime on the previous iteration)
        if primes[num]:
            for nonPrime in range(num * num, upperBound + 1, num):
                primes[nonPrime] = False
    # returning the list of booleans with the index indicating prime or non-prime
    return primes

def main():
    upperBound = 2000000
    # getting the list of primes
    primes = sieveOfEratosthenes(upperBound)
    # Summing and printing the prime list.
    print(sum(num for num in range(2,upperBound + 1) if primes[num]))

if __name__ == '__main__':
    try:
        main()
    except:
        print(format_exc())