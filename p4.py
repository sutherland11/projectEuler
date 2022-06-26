# Finds the largest number that is a product of 2 3-digit number and is a palindrome.

# Ths function simply returns true if the 2 factors produce a product that is a palindrome.
def isPalindrome(num1, num2):
    return str(num1 * num2) == str(num1 * num2)[::-1]

# Main method, there is almost definitely a more efficient method but since the computation time on this problem is small I thought this would be sufficient.
def main():
    # Set largest palindrome to 0 initially
    largestPalindrome = 0
    # nested for loop will iterate through all possible combinations of 3-digit factors to determine the largest palindrome.
    for factor1 in range(999, 100, -1):
        for factor2 in range(factor1, 100, -1):
            if isPalindrome(factor1, factor2) and factor1 * factor2 > largestPalindrome:
                largestPalindrome = factor1 * factor2
    return largestPalindrome

print(main())
