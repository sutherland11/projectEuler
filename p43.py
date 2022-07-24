import math
import time
from traceback import format_exc
from math import factorial

def getDivisibleSubstrings():
    # creating dictionary to store all numbers for which one of the first 7 primes is a divisor.
    primes = {'2': [], '3': [], '5': [], '7': [], '11': [], '13': [], '17': []}
    num = 12
    # iterating from 12 to 999 and determining which primes each is divisible by.
    while num < 1000:
        chars = str(num) if num > 99 else '0' + str(num)
        if len(set(chars)) == len(chars):
            for prime in primes:
                if num % int(prime) == 0:
                    primes[prime].append(chars)
        num += 1
    # return the first 7 primes and the numbers < 999 for which they are divisors
    return primes

# The main method will get all numbers for which one of the primes is a factor in reverse order then combine them as strings if the digits match one of the
# possible sub-string solutiuons. e.g. 289 is divisible by 17 and 728 is divisible by 13 so 7298 is a possible string to attempt to match to any number < 999
# for which 11 is a factor and for which no digit is repeated. This process will continue through the lower primes until we have a list of 9 digit numbers. 
# Each of the nine will then have the only missing digit added as the first digit, these are numbers with the desired properties whhich are then summed.
def main():
    # getting the first 7 primes and the numbers < 999 for which they are divisors
    divisibleSubstrings = getDivisibleSubstrings()
    targetStrings = []
    # iterating through each of the first 7 primes in reverse order for optimization
    for prime in divisibleSubstrings.__reversed__():
        updatedTargetStrings = []
        # iterating through the numbers for which the prime is a factor
        for substring in divisibleSubstrings[prime]:
            # when 17 is the factor we create the original list of possible strings
            if prime == '17':
                updatedTargetStrings.append(substring)
            # otherwise we search for compatible substrings to continue the process
            else:
                for target in targetStrings:
                    if substring[1:3] == target[0:2] and len(set(substring + target[2::])) == len(substring + target[2::]):
                        updatedTargetStrings.append(substring + target[2::])
        targetStrings = updatedTargetStrings
    # iterating through the valid strings and adding the missing digit to creat the number with the deired properties, then adding that to the total.
    total = 0
    for target in targetStrings:
        for digit in '0123456789':
            if digit not in target:
                total += int(digit + target)
                break
    print(total)

if __name__ == '__main__':
    try:
        main()
    except:
        print(format_exc())
