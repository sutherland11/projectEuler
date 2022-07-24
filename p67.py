# Main method, an iterative dynamic programming solution for finding the solution to problem 67 on projectEuler (There is also a recursive method that would solve this problem)
def greatestSum(path):
    # Opening given text file
    file = open(path, 'r')
    rows = []
    # Creating list of lists with integers from text file
    for line in file.readlines():
        rows.append([int(item) for item in line.split()])
    rows.reverse()
    row = 1
    sums = []
    # Iterating through the list from the bottom to the top
    while row < len(rows):
        col = 0 
        # On anything but the first iteration the following 3 lines will replace the previous line with the highest possible sum of adjacent items up to that line.
        if sums:
            rows[row - 1] = sums
            sums = []
        # Iterating through the row and appending the max possible sum of adjacent values the "sums" list
        while col < len(rows[row]):
            sums.append(max(rows[row - 1][col] + rows[row][col] ,rows[row - 1][col + 1] + rows[row][col]))
            col += 1
        row += 1
    return sums[0]

path = r"C:\Users\wills\OneDrive\Desktop\myPyScripts\ProjectEuler\67\p67.txt"
# Executing main method with the only given parameter being the location of the text file which is given by the user.
greatestSum = greatestSum(path)
print(greatestSum)
