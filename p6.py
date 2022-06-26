# A pythonic one line solution to problem 6, the first section will simply sum every number from 1 to 100 before squaring it. 
# The second section will square every number from 1 to 100 before summing them, the difference is then easily found.
print(sum([num for num in range(0, 100 + 1)])**2 - sum([num**2 for num in range(0, 100 + 1)]))
