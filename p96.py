from math import floor
from copy import deepcopy
from traceback import format_exc

# This python script will read in the sudoku.txt file and attempt to first solve it in a deterministic manner before using a recursive brute force approach.

# position class will track the grid position, possible values at that position and whether the value has been found or not.
class position:
    def __init__(self, gp):
        self.gp = gp
        self.possibleValues = ['1','2','3','4','5','6','7','8','9']
        self.attemptedGuesses = []
        self.found = False

# the gtris class will hold all of the positions and track how many positions have been found, etc. When the class is initialized it will iterate through the rows
# and columns and remove possible values for each position that has not been found based on positions that have been found.
class grid:
    def __init__(self, lines):
        self.positions = []
        self.numFound = 0
        self.sum = 0 
        rIndex = 0
        while rIndex < len(lines):
            cIndex = 0
            row = []
            while cIndex < len(lines[rIndex]):
                if lines[rIndex][cIndex] != '\n':
                    newPosition = position([rIndex, cIndex])
                    if lines[rIndex][cIndex] != '0':
                        newPosition.possibleValues = [lines[rIndex][cIndex]]
                        newPosition.found = True
                        self.numFound += 1
                    row.append(newPosition)
                cIndex += 1
            self.positions.append(row)
            rIndex += 1
        self.setPossibleValues()

    # Returns values in a given row
    def getRowValues(self, row):
        return [index.possibleValues[0] if len(index.possibleValues) == 1 else ' ' for index in self.positions[row]]

    # returns values in a given column
    def getColumnValues(self, column):
        dColumn = []
        row = 0 
        while row < len(self.positions):
            if len(self.positions[row][column].possibleValues) == 1:
                dColumn.append(self.positions[row][column].possibleValues[0])
            else:
                dColumn.append(' ')
            row += 1
        return dColumn

    # return values in a given 3 by 3 box
    def getBoxValues(self, box):
        dBox = []
        row = 0
        while row < len(self.positions):
            col = 0
            while col < len(self.positions[row]):
                if floor(row / 3) * 3 + floor(col / 3) == box:
                    if len(self.positions[row][col].possibleValues) == 1:
                        dBox.append(self.positions[row][col].possibleValues[0])
                    else:
                        dBox.append(' ')
                col += 1
            row += 1
        return dBox

    # Sets possible values for each position that is in the same row, column or box as pos.gp (grid position of position pos)
    def setPossibleValues(self):
        for row in self.positions:
            for pos in row:
                if pos.found:
                    self.eliminatePossibilities(pos.gp)

    # Eliminates possible values at each position based on the box, row, and column of the grid position gp.
    def eliminatePossibilities(self, gp):
        changesMade = False
        gpValue = self.positions[gp[0]][gp[1]].possibleValues[0]
        affectedPositions = []
        for item in self.positions[gp[0]]:
            if item.gp != gp and not item.found and gpValue in item.possibleValues:
                affectedPositions.append(item)
        row = 0
        while row < len(self.positions):
            if row != gp[0] and not self.positions[row][gp[1]].found and gpValue in self.positions[row][gp[1]].possibleValues:
                affectedPositions.append(self.positions[row][gp[1]])
            row += 1
        row = floor(gp[0] / 3) * 3
        while row < floor(gp[0] / 3) * 3 + 3:
            col = floor(gp[1] / 3) * 3
            while col < floor(gp[1] / 3) * 3 + 3:
                if [row, col] != gp and not self.positions[row][col].found and gpValue in self.positions[row][col].possibleValues and self.positions[row][col] not in affectedPositions:
                    affectedPositions.append(self.positions[row][col])
                col += 1
            row += 1
        for item in affectedPositions:
            if gpValue in item.possibleValues:
                item.possibleValues.remove(gpValue)
                changesMade = True
                if len(item.possibleValues) == 1:
                    item.found = True
                    self.numFound += 1
        return changesMade

    # Will continually call the eliminate possibilities function until no further changes can be found using this method.
    def elimination(self):
        changes = False
        while 1:
            changeNum = 0
            for row in self.positions:
                for item in row:
                    if item.found:
                        if self.eliminatePossibilities(item.gp):
                            changes = True
                            changeNum += 1
                            if self.numFound == 81:
                                return False
            if changeNum == 0:
                break
        return True if changes else False

    # This function will attempt to find the position of a value rather than the value at a given position. For example it will try to the find the position of the 1 in the 
    # first row or first column, rather than trying to find the value at position 1, 1. It will iterate until no further changes can be made using this method.
    def findValuePosition(self):
        changes = True
        while changes:
            changes = False
            changeNum = 0
            cSet = [[] for num in range(9)]
            cValuesToFind = [[str(pValue) for pValue in range(1, 10)] for num in range(9)]
            bSet = [[] for num in range(9)]
            bValuesToFind = [[str(pValue) for pValue in range(1, 10)] for num in range(9)]
            row = 0
            while row < len(self.positions):
                rSet = []
                rValuesToFind = [str(num) for num in range(1, 10)]
                col = 0
                while col < len(self.positions[row]):
                    if self.positions[row][col].found:  
                        if self.positions[row][col].possibleValues[0] in rValuesToFind:
                            rValuesToFind.remove(self.positions[row][col].possibleValues[0])
                        if self.positions[row][col].possibleValues[0] in cValuesToFind[col]:
                            cValuesToFind[col].remove(self.positions[row][col].possibleValues[0])
                        if self.positions[row][col].possibleValues[0] in bValuesToFind[floor(row / 3) * 3 + floor(col / 3)]:
                            bValuesToFind[floor(row / 3) * 3 + floor(col / 3)].remove(self.positions[row][col].possibleValues[0])
                    else:
                        rSet.append(self.positions[row][col])
                        cSet[col].append(self.positions[row][col])
                        bSet[floor(row / 3) * 3 + floor(col / 3)].append(self.positions[row][col])
                    col += 1
                for value in rValuesToFind:
                    if self.searchForValuePosition(rSet, value):
                        changeNum += 1
                        if self.numFound == 81:
                            break
                row += 1
            col = 0
            while col < len(cSet):
                for value in cValuesToFind[col]:
                    if self.searchForValuePosition(cSet[col], value):
                        changeNum += 1
                        if self.numFound == 81:
                            break
                col += 1
            box = 0
            while box < len(bSet):
                for value in bValuesToFind[box]:
                    if self.searchForValuePosition(bSet[box], value):
                        changeNum += 1
                        if self.numFound == 81:
                            break
                box += 1
            if changeNum < 1:
                changes = False
        return changes

    # method used by findValuePosition method 
    def searchForValuePosition(self, set, value):
        possiblePositions = []
        for item in set:
            if not item.found and value in item.possibleValues:
                possiblePositions.append(item)
        if len(possiblePositions) == 1:
            possiblePositions[0].possibleValues = [value]
            possiblePositions[0].found = True
            self.numFound += 1
            return True

    # Solve puzzle method will call elimination method while it is still making progress. That method will call other deterministic methods.
    def solvePuzzle(self):
        changes = 1
        while changes > 0:
            changes = 0 
            changes += self.elimination()

    # Checking if solution is valid
    def isValidSolution(self):
        try:
            nums = ['1','2','3','4','5','6','7','8','9']
            for index in range(9):
                if not all(num in self.getRowValues(index) for num in nums) or not all(num in self.getColumnValues(index) for num in nums) or not all(num in self.getBoxValues(index) for num in nums):
                    return False
            return True
        except IndexError:
            return False

# Method used by the recursive method
def solve(grid, row, col, num):
    for x in range(9):
        if grid[row][x] == num:
            return False
    for x in range(9):
        if grid[x][col] == num:
            return False
    startRow = row - row % 3
    startCol = col - col % 3
    for i in range(3):
        for j in range(3):
            if grid[i + startRow][j + startCol] == num:
                return False
    return True
 
# Recursive brute force method to be used in cases where quicker methods fail.
def bruteForce(grid, row, col):
    M = 9
    if (row == M - 1 and col == M):
        return True
    if col == M:
        row += 1
        col = 0
    if grid[row][col] > 0:
        return bruteForce(grid, row, col + 1)
    for num in range(1, M + 1, 1): 
        if solve(grid, row, col, num):
            grid[row][col] = num
            if bruteForce(grid, row, col + 1):
                return True
        grid[row][col] = 0
    return False

# Main method which will read in the file, attempt to solve using quicker methods and then solve using brute force recursive method when other methods fail.
def main():
    path = 'C:\\Users\\wills\\OneDrive\\Desktop\\myPyScripts\\ProjectEuler\\96\\sudoku.txt'
    file = open(path, 'r')
    lines = [line for line in file.readlines()]
    total = 0
    for gridNum in range(50):
        rows = lines[1 + 10 * gridNum:10 + 10 * gridNum]
        newGrid = grid(rows)
        newGrid.solvePuzzle()
        if newGrid.isValidSolution():
            total += int(''.join([num.possibleValues[0] for num in newGrid.positions[0][0:3]]))
        else:
            intGrid = []
            for row in newGrid.positions:
                intRow = []
                for col in row:
                    if len(col.possibleValues) == 1:
                        intRow.append(int(col.possibleValues[0]))
                    else:
                        intRow.append(0)
                intGrid.append(intRow)
            bruteForce(intGrid, 0, 0)
            total += int(''.join(str(num) for num in intGrid[0][0:3]))
    print(total)

if __name__ == '__main__':
    try:
        main()
    except:
        print(format_exc())