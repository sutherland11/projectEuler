from collections import Counter   
from traceback import format_exc    

# This function will rank a hand, for example a flush will rank higher than a pair. This will be compared first to determine the winner. In the event of the same rank
# there will be further comparisons.
def rankHand(hand, valueDictionary, ranks):
    # Checking if all cards in the hand have the same suit
    isFlush = all([hand[0][1] == card[1] for card in hand])
    # The next few lines will sort the hand in order of value, then create two lists, a and b, with the type of card and how many of that card are in the hand.
    hand = sorted([card[0] for card in hand], key=valueDictionary.get, reverse=True)
    a = Counter([card[0] for card in hand]).most_common()
    b = [i for i, j in a]
    c = [j for i, j in a]
    rank = ranks.index(c)
    isStraight = True
    if len(b) == 5:
        # iterating through hand to check if it is a straight
        index = 0 
        while index < 4:
            if valueDictionary[b[index]] - 1 != valueDictionary[b[index + 1]]:
                isStraight = False
                break
            index += 1
        # Assigning rank if hand is a straight, flush or straight flush
        if isStraight:
            if rank not in (6, 7):
                rank = 4
            if isFlush:
                if b[0] == 'A':
                    rank = 9
                else:
                    rank = 8
    return rank, b
    
def main():
    # reading file at given path.
    path = 'C:\\Users\\wills\\OneDrive\\Desktop\\myPyScripts\\ProjectEuler\\54\\p54handFile.txt'
    file = open(path, 'r')
    # the list of lists called ranks will be used to rank a hand based on number of reoccuring cards, pair of tens, three jacks, two-pair, etc.
    ranks = [[1,1,1,1,1],[2,1,1,1],[2,2,1],[3,1,1],[],[],[3,2],[4,1]]
    valueDictionary = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'T': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14}
    # iterating through the file
    p1Wins = 0
    for line in file.readlines():
        # Ranking hands using the rankHand function
        p1Hand = [i for i in line.split()[0:5]]
        p2Hand = [i for i in line.split()[5:10]]
        rank1, b1 = rankHand(p1Hand, valueDictionary, ranks)
        rank2, b2 = rankHand(p2Hand, valueDictionary, ranks)
        # Comparing ranks
        if rank1 > rank2:
            p1Wins += 1
        # Comparing the highest value cards in the event of a tied rank
        if rank1 == rank2:
            index = 0
            while valueDictionary[b1[index]] == valueDictionary[b2[index]]:
                index += 1
            if valueDictionary[b1[index]] > valueDictionary[b2[index]]:
                p1Wins += 1
    print(p1Wins)

if __name__ == '__main__':
    try:
        main()
    except:
        print(format_exc())
