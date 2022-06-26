
def sumEvenFibonacci(maxNum):
    total = 0 
    termA = 0
    termB = 1
    while termB < maxNum:
        termA, termB = termB, termA + termB
        total += termB if termB % 2 == 0 else 0
    return total

print(sumEvenFibonacci(4000000))
