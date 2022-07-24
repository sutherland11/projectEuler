import math
from traceback import format_exc

# A slightly modified version of the sieve of Eratosphenes function used in problem 10, this one will return a list of the primes as well as a list of booleans for all
# numbers indicating primality.
def sieveOfEratosthenes(upperBound):
    primes = [True] * (upperBound + 1)
    primes[0] = primes[1] = False
    for num in range(2, int(math.sqrt(upperBound)) + 1):
        if primes[num]:
            for nonPrime in range(num * num, upperBound + 1, num):
                primes[nonPrime] = False
    return primes, [index for index in range(len(primes) - 1) if primes[index]]

# Main method which will find which prime, below a given upper bound, can be written as the sum of the most consecutive primes.
def main():
    upperBound = 1000000
    # Calling sieve function to get list of primes and boolean list of primality based on index.
    bitPrimes, primes = sieveOfEratosthenes(upperBound)
    # Iterating through the primes list to find the cumulative sum of primes to that point.
    cumulativeSums = []
    cumulativeSum = 0
    for index in range(len(primes) + 1):
        cumulativeSum += primes[index - 1]
        cumulativeSums.append(cumulativeSum)
    length = 0
    primeSum = 0
    endIndex = len(cumulativeSums)
    # iterating through the list of cumulative sums, storing the length and sum of consecutive primes if length is greater than the previous max. The inner loop will break if the 
    # sum of primes is greater than the given upper bound.
    for i in range(endIndex):
        for j in range(i + length, endIndex):
            if cumulativeSums[j] - cumulativeSums[i] >= upperBound:
                endIndex = j
                break
            if j - i > length and bitPrimes[cumulativeSums[j] - cumulativeSums[i]]:
                length = len(primes[i : j])
                primeSum = sum(primes[i : j])
    print(primeSum)
            
if __name__ == '__main__':
    try:
        main()
    except:
        print(format_exc())
