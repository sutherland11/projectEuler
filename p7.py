import math
from traceback import format_exc
import time

# This function wil return the largest number that the Nth prime could be. For example given N = 10 it will return 32 meaning that the 10th prime must be less than 32.
def largestPossiblePrime(N):
    return math.ceil(N * (math.log(N) + math.log(math.log(N))))

# My implementation of the sieve of Eratosthenes, a method for finding all primes below a given upper bound.
def sieveOfEratosthenes(upperBound):
    # creating a list of all numbers from 2 to the given upper bound
    nums = [num for num in range(2, upperBound + 1)]
    index = 0
    # factor is the current factor for which we will eliminate numbers which are not primes because it is a factor
    factor = nums[0]
    # iterating from the current factor squared to the upper bound
    while factor**2 <= upperBound:
        # creating a list consisting of the list nums without any number for which the current factor is a divisor, creating a new list using 
        # list comprehension because it is much quicker than removing each number individually. 
        nums = [num for num in nums if num not in range(factor * 2, upperBound + 1, factor)]
        index += 1
        # changing factor to the new lowest prime that has not yet had all of its products removed.
        factor = nums[index]
    return nums

def main():
    N = 10001
    # getting the upper bound, the largest that the nth prime could be.
    upperBound = largestPossiblePrime(N)
    # getting list of primes less than the upper bound
    primes = sieveOfEratosthenes(upperBound)
    # printing nth prime
    print(primes[N - 1])

if __name__ == '__main__':
    try:
        main()
    except:
        print(format_exc())