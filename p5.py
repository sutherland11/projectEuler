# Main method will find the smallest positive number that is evenly divisible by all numbers from 1 to 20.
def main():
    # Since we already know that 2520 is the smallest number divisible by 1 through 10 we can start there and increment by 2520 each time. 
    product = 2520
    found = False
    while not found:
        product += 2520
        isDivisible = True
        divisor = 11
        # iterating from 11 to 20, if any of these do not evenly divide into the product the loop will break and the product will be incremented before looping from 11 to 20 again.
        while divisor <= 20:
            if product % divisor != 0: 
                isDivisible = False
                break
            divisor += 1
        if isDivisible:
            found = True
    return product

print(main())