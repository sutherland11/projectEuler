from traceback import format_exc

# main method finds the product of the Pythagorean triplet where a + b + c = 1000
def main():
    numSum = 1000
    # outer loop will loop to 1000
    for b in range(1, numSum):
        # a must be smaller than b so a will loop to b - 1
        for a in range(1, b):
            # we know a + b + c must equal 1000 so we set c to the appropriate value, check if it is the desired triplet, and return the product if so.
            c = numSum - a - b
            if a**2 + b**2 == c**2:
                return a * b * c

if __name__ == '__main__':
    try:
        print(main())
    except:
        print(format_exc())