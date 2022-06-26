# A one line soluton to problem 1 on prjectEuler.net
# Finds the sum of all natural numbers below 1000 which are multiples of 3 or 5
# Takes the sum of a list which only includes the numbers that are evenly divisible by 3 or 5 (Modulus of these numbers is 0)
print(sum([num for num in range(1000) if num % 3 == 0 and num % 5 == 0]))