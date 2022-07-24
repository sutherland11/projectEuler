from traceback import format_exc
from math import prod

# Main method finds the largest product of N numbers in a given series.
def main():
    # opening file at given path and creating a list
    path = 'C:\\Users\\wills\\OneDrive\\Desktop\\myPyScripts\\ProjectEuler\\8\\p8numberFile.txt'
    file = open(path, 'r')
    nums = [int(num) for num in file.read() if num != '\n']

    # simply iterating through the list and finding the product of 13 consecutive numbers, setting the product as the largest if it 
    # is larger than the previous largest.
    N = 13
    maxProduct = 0
    index = 0 
    while index < len(nums) - N:
        product = prod(nums[index : index + N])
        maxProduct = product if product > maxProduct else maxProduct
        index += 1
    print(maxProduct)

if __name__ == '__main__':
    try:
        main()
    except:
        print(format_exc())
