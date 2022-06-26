# Finds the sum of the even-valued terms in the fibonacci sequence whose value is less than some max number, 4,000,000 in this case.
def sumEvenFibonacci(maxNum):
    # start by setting the total to 0, and the first 2 terms to 1 and 2 respectively.
    total = 0 
    termA = 0
    termB = 1
    # Loop until the larger term is greater than or equal to the given max number.
    while termB <= maxNum:
        # set the first term to the value of the 2nd and the second to the sum of the first and second term then add the 2nd term to the total if it is even.
        termA, termB = termB, termA + termB
        total += termB if termB % 2 == 0 else 0
    return total

print(sumEvenFibonacci(4000000))
