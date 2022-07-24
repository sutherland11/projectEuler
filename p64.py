from math import sqrt
from math import floor
from traceback import format_exc

# This method will find the period of the square root of N when written as a continued fraction. Essentially a0, a1, a2, etc can be found based on the previous iterations 
# values of the same values. The pattern can be seen algebraically. Once the pattern repeats (seen when d and m are reoccuring parameters) the period has been found.
def findPeriod(N):
    parameters = []
    a0 = floor(sqrt(N))
    a = [a0]
    d = 1
    m = -a0
    parameters = [[d, m]]
    periodFound = False
    while not periodFound:
        d = int((N - m**2) / d)
        a_i = floor((sqrt(N) - m) / d)
        m = -m - (a_i * d)
        a.append(a_i)
        if [d, m] in parameters:
            periodFound = True
        parameters.append([d, m])
    return a

# Determining if sqrt(N) is irrational
def isIrrationalSquareRoot(N):
    return not floor(sqrt(N))**2 == N

def main():
    N = 10000
    index = 2
    count = 0 
    while index <= N:
        # incrementing the count if the square root of index is both irrational and has an odd period when written as a continued fraction.
        count += (isIrrationalSquareRoot(index) and len(findPeriod(index)) % 2 == 0)
        index += 1
    print(count)

if __name__ == '__main__':
    try:
        main()
    except:
        print(format_exc())