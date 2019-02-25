from collections import Counter
import random
import itertools
import numpy as np

#important functions
def cardValue(card): 
    """
    CardValue retrieves the actual integer value of the card
        @date 9/12/2017
        @param card       is the inputed card that we are trying to convert to an integer
        @return cardAsAnInt     the actual integer value of the card
    """
    cardAsAnInt = 0 
    if (card == "A"):
        cardAsAnInt = 1
    elif (card == "J"):
        cardAsAnInt = 11
    elif (card == "Q"):
        cardAsAnInt = 12
    elif (card == "K"):
        cardAsAnInt = 13  
    elif (int(card) >= 2 and int(card) <= 10):
        cardAsAnInt = int(card)
    return cardAsAnInt

def sort(inputtedArray):
    """
    Given a set of cards, organizes them in ascending order (ex: A, K, 6, 7, 3 --> A, 3, 6, 7, K).
        @date 9/14/2017
        @param inputtedArray       an array containing the inputed cards.
        @return sortedArray     returns the cards as a sortedArray in ascending order.
    """
    sortedArray = []
    isSorted = False  

    while inputtedArray:
        smallest = min(inputtedArray)
        index = inputtedArray.index(smallest)
        sortedArray.append(inputtedArray.pop(index))
    return sortedArray

def sortWithSuit(inputtedArray):
    """
    Given a set of cards with their respective Suit, organizes them in ascending order (ex: SA, HK, D6, S7, C3 --> SA, C3, D6, S7, HK).
        @date 11/14/2017
        @param inputtedArray       an array containing the inputed cards.
        @variable noSuitArray      the array containing the inputed cards but without their respective suit.
        @return sortedArray     returns the cards as a sortedArray in ascending order.
    """
    sortedArray = []
    isSorted = False  
    noSuitArray = removeSuit(inputtedArray)
    while inputtedArray:
        smallest = min(noSuitArray)
        index = noSuitArray.index(smallest)
        noSuitArray.pop(index)
        sortedArray.append(inputtedArray.pop(index))
    return sortedArray

def removeSuit(inputtedArray):
    """
    Given a set of cards with their respective Suit, removes the suit and returns the new array.
        @date 12/5/2017
        @param inputtedArray       an array containing the inputed cards.
        @return noSuitArray     returns the cards with just their numbers, no suits.
    """
    noSuitArray = []
    for i in range(0, len(inputtedArray)):
        noSuitArray.append(int(inputtedArray[i][1:]))
    return noSuitArray

#findingPoints
def findFifteen(inputHand):
    """
    findFifteen returns all possible combinations that add up to 15
        @date 9/19/2017
        @param inputtedArray       an array containing the inputed cards.
        @return addsUpToFifteen     returns a two-dimensional array containing all combinations of 15.
    """
    addsUpToFifteenArray = [] #A 2-dimension array containing all possible combinations of 15 in a hand.
    fifteenInt = 15
    inputtedArray = sort(inputHand.copy()) #sorts the array from smallest to largest.
    length = len(inputtedArray) #the amount of cards in a hand (will range from 4-5. 4 = starting hand. 5 = includes the up-card)
    for i in range(0, length): #this fixes the fact that JQK are 11,12,13 respectively, but they count as 10 when refering to a 15.
        if (inputtedArray[i] > 10):
            inputtedArray[i] = 10

    for i in range(0, length):
        for j in range (i+1, length):
            #If statement that is comparing 2 cards that adds up to 15.
            if (inputtedArray[i] + inputtedArray[j] == fifteenInt):
                tempArray = [] #temporary array containing an individual pair.
                tempArray.append(inputtedArray[i]) #adds the first card
                tempArray.append(inputtedArray[j]) #adds the second card
                addsUpToFifteenArray.append(tempArray) #adds the 'pair' into the array
            for k in range(j+1, length):
                #If statement that is comparing 3 cards that adds up to 15.
                if (inputtedArray[i] + inputtedArray[j] + inputtedArray[k] == fifteenInt):
                    tempArray = [] #temporary array containing an individual pair.
                    tempArray.append(inputtedArray[i]) #adds the first card
                    tempArray.append(inputtedArray[j]) #adds the second card
                    tempArray.append(inputtedArray[k]) #adds the third card
                    addsUpToFifteenArray.append(tempArray) #adds the 'pair' into the array
                for l in range(k+1, length):
                    #If statement that is comparing 4 cards that adds up to 15.                    
                    if (inputtedArray[i] + inputtedArray[j] + inputtedArray[k] + inputtedArray[l] == fifteenInt):
                        tempArray = [] #temporary array containing an individual pair.
                        tempArray.append(inputtedArray[i]) #adds the first card
                        tempArray.append(inputtedArray[j]) #adds the second card
                        tempArray.append(inputtedArray[k]) #adds the third card
                        tempArray.append(inputtedArray[l]) #adds the fourth card
                        addsUpToFifteenArray.append(tempArray) #adds the 'pair' into the array
    #If statement that is comparing 5 cards that add up to 15. (no need for a loop since this will only happen once).                    
    if (length == 5):
        if (inputtedArray[0] + inputtedArray[1] + inputtedArray[2] + inputtedArray[3] + inputtedArray[4] == fifteenInt):
            tempArray = [] #temporary array containing an individual pair.
            tempArray.append(inputtedArray[0]) #adds the first card
            tempArray.append(inputtedArray[1]) #adds the second card
            tempArray.append(inputtedArray[2]) #adds the third card
            tempArray.append(inputtedArray[3]) #adds the fourth card
            tempArray.append(inputtedArray[4]) #adds the fifth card
            addsUpToFifteenArray.append(tempArray) #adds the 'pair' into the array
    
    return addsUpToFifteenArray    

def findPairs(inputHand):
    """
    findPairs returns all pairs in the array.
        @date 9/14/2017
        @param inputtedArray       an array containing the inputed cards.
        @return pairArray     returns a two-dimensional array containing all pairs.
    """
    pairArray = [] #A 2-dimension array containing all possible pairs in a hand.
    inputtedArray = sort(inputHand.copy()) #sorts the array from smallest to largest.
    length = len(inputtedArray) #the amount of cards in a hand (will range from 4-5. 4 = starting hand. 5 = includes the up-card)
    for i in range(0, length):
        for j in range (i+1, length):
            tempArray = [] #temporary array containing an individual pair.
            if (inputtedArray[i] == inputtedArray[j]):
                tempArray.append(inputtedArray[i]) #adds the first card
                tempArray.append(inputtedArray[j]) #adds the second card
                pairArray.append(tempArray) #adds the 'pair' into the array

    return pairArray

def findRun(inputHand):
    """
    run checks to see if there is atleast one run and returns all possible runs (not including the up card).
        @date 10/31/2017
        @param inputtedArray       an array containing the inputed cards.
        @return runArray     
    """    
    runArray = [] #A 2-dimension array containing all the longest runs in a hand.
    allPossibleRuns = [] #A 2-dimension array containing all possible runs in a hand.
    inputtedArray = sort(inputHand.copy()) #sorts the array from smallest to largest.
    length = len(inputtedArray) #the amount of cards in a hand (will range from 4-5. 4 = starting hand. 5 = includes the up-card)
    longestRunLen = 0

    for L in range(0, len(inputtedArray)+1):
        for subset in itertools.combinations(inputtedArray, L):
            tempArray = []
            if (len(subset) == 5):
                if (subset[0]+1 == subset[1] and subset[1]+1 == subset[2] and subset[2]+1 == subset[3] and subset[3]+1 == subset[4]):
                    tempArray.append(subset[0])
                    tempArray.append(subset[1])
                    tempArray.append(subset[2])
                    tempArray.append(subset[3])
                    tempArray.append(subset[4])
                    allPossibleRuns.append(tempArray)
                    longestRunLen = 5
            elif (len(subset) == 4):
                if (subset[0]+1 == subset[1] and subset[1]+1 == subset[2] and subset[2]+1 == subset[3]):
                    tempArray.append(subset[0])
                    tempArray.append(subset[1])
                    tempArray.append(subset[2])
                    tempArray.append(subset[3])
                    allPossibleRuns.append(tempArray)
                    if (longestRunLen <= 4):
                        longestRunLen = 4
            elif (len(subset) == 3):
                if (subset[0]+1 == subset[1] and subset[1]+1 == subset[2]):
                    tempArray.append(subset[0])
                    tempArray.append(subset[1])
                    tempArray.append(subset[2])
                    allPossibleRuns.append(tempArray)
                    if (longestRunLen <= 3):
                        longestRunLen = 3
    for i in range (0, len(allPossibleRuns)):
        if (len(allPossibleRuns[i]) >= longestRunLen):
            runArray.append(allPossibleRuns[i])

    return runArray

def nobs(pInputHand):
    """
    nobs returns 1 point if there is a jack in the hand and the suit of the jack matches the upcard's suit.
        @date 1/25/2017
        @param inputHand       an array containing the inputed cards containing their suits.
        @return points     returns 1 point if there is a nobs
    """
    inputHand = pInputHand.copy()
    length = len(inputHand) #the amount of cards in a hand (will range from 4-5. 4 = starting hand. 5 = includes the up-card)
    upCard = 'Z14'
    if (length == 5):
        upCard = str(inputHand.pop()) #the upcard is the last card of the inputHand
        length = len(inputHand)
    points = 0
    for i in range(0, length):
        if (int(inputHand[i][1:]) == 11): #checks the number
            if (str(inputHand[i][:1]) == str(upCard[:1])): #checks the suit
                points += 1
                i = length
    return points
        
def flush(pInputHand):
    """
    flush returns 4 point if all the cards within the hand share the same suit, if they do it checks the upCard and if it matches returns 5 points.
        @date 1/25/2017
        @param inputHand       an array containing the inputed cards containing their suits.
        @param upCard          the upCard with its suit.
        @return points     returns 4 or 5 points if there is a flush
    """
    inputHand = pInputHand.copy()
    length = len(inputHand) #the amount of cards in a hand (will range from 4-5. 4 = starting hand. 5 = includes the up-card)
    upCard = 'Z14'
    points = 0
    if (length == 5):
        upCard = inputHand.pop #the upcard is the last card of the inputHand
        if (inputHand[0][:1] == inputHand[1][:1] and inputHand[0][:1] == inputHand[2][:1] and inputHand[0][:1] == inputHand[3][:1] and inputHand[0][:1] == inputHand[4][:1] ):
            points = 5
        elif (inputHand[0][:1] == inputHand[1][:1] and inputHand[0][:1] == inputHand[2][:1] and inputHand[0][:1] == inputHand[3][:1] ):
            points = 4
    return points

def fifteenPoints(array):
    """
    Given a two-dimensional array calculates the appropiate amount of points to return for 15.
        @date 12/5/2017
        @param array        two-dimensional array containing all the combinations of 15.
        @return points      the amount of points the user recieved from the array.
    """
    length = len(array)
    points = 0
    for i in range(0, length):
        points += 2
    return points

def pairPoints(array):
    """
    Given a two-dimensional array calculates the appropiate amount of points to return for pairs.
        @date 12/5/2017
        @param array        two-dimensional array containing all the combinations of pairs.
        @return points      the amount of points the user recieved from the array.
    """
    length = len(array)
    points = 0
    for i in range(0, length):
        points += 2
    return points

def runPoints(array):
    """
    Given a two-dimensional array calculates the appropiate amount of points to return for runs.
        @date 12/5/2017
        @param array        two-dimensional array containing all the combinations of runs.
        @return points      the amount of points the user recieved from the array.
    """
    length = len(array)
    points = 0
    for i in range(0, length):
        runLength = len(array[i])
        points += runLength
    return points

#game aspects
def createNewDeck():
    """
    Creates a deck of cards with 13 different cards of 4 different suits and then shuffles the deck.
        @date 12/5/2017
        @return deck     returns an array of 52 cards
    """
    deck = []
    for i in range(1,14):
        deck.append('C' + str(i))
        deck.append('D' + str(i))
        deck.append('H' + str(i))
        deck.append('S' + str(i))
    random.shuffle(deck)    
    return deck

def drawOneCard(theDeck):
    """
    Removes a card from theDeck and returns the card.
        @date 12/5/2017
        @param theDeck   an array of cards.
        @return card     the card removed from theDeck.
    """
    length = len(theDeck) - 1
    cardNumber = random.randint(0,length)
    card = theDeck[cardNumber]
    theDeck.remove(card)
    return card

def drawAHand(theDeck):
    """
    Calls drawOneCard 6 times and returns an array of 6 cards.
        @date 12/5/2017
        @param theDeck     an array of cards.
        @return player     an array containing 6 cards that the player was dealt.
    """
    player = []
    for i in range(0,6): #draws a hand size of 6
        player.append(drawOneCard(theDeck))
    return player

def drawSpecificHand(sixCardHand, theDeck):
    """
    Returns the specific hand with the deck
        @date 12/5/2017
        @param theDeck     an array of cards.
        @return player     an array containing 6 cards that the player was dealt.
    """

    for i in range(0, len(theDeck)): #loops through the whole deck looking for the cards
        for j in range (0,6): #loops through the hand
            if (i < len(theDeck)):
                if (str(theDeck[i]) == str(sixCardHand[j])):
                    theDeck.remove(theDeck[i])
        
    return sixCardHand

def flipUpCard(theDeck):
    """
    Removes a card from the deck and returns the card.
        @date 12/5/2017
        @param theDeck      an array of cards.
        @return upCard      the returned card that is the upCard for the game.
    """
    upCard = drawOneCard(theDeck)
    return upCard

def chooseHand(sixCardHandWithSuit, theDeck):
    """
    Returns the expected value of all the combinations of 4 card hands and chooses the highest one. If tie, randomly picks one from the tie.
        @date 12/5/2017
        @param sixCardHandWithSuit      the inputted array of six cards with their respectived suit
        @param theDeck                  the respective deck to the hand
        @return
    """    
    sixCardHand = sort(removeSuit(sixCardHandWithSuit))
    fourCardHandArray = list(itertools.combinations(sixCardHand, 4))
    fourCardHandWithSuitArray = list(itertools.combinations(sixCardHandWithSuit, 4))
    #print(sixCardHand)
    fourCardHandArrayPoints = [None] * 16
    maxPoints = 0
    maxPointsIndex = 0
    for i in range (0,15):
        fourCardHand = list(fourCardHandArray[i])
        fourCardHandWithSuit = list(fourCardHandWithSuitArray[i])
        fourCardHandArrayPoints[i] = getPoints(fourCardHand) + probabilityPoints(fourCardHand, theDeck) + getPointsWithSuit(fourCardHandWithSuit)  + probabilityPointsWithSuit(fourCardHandWithSuit, theDeck)
        #print(str(i) + ": " + str(fourCardHand) + " = " + str(fourCardHandArrayPoints[i]))
        if(fourCardHandArrayPoints[i] > maxPoints):
            maxPoints = fourCardHandArrayPoints[i]
            maxPointsIndex = i
        elif(fourCardHandArrayPoints[i] == maxPoints):
            randomNumber = random.randint(1,1001)
            if (randomNumber > 500):
                maxPoints = fourCardHandArrayPoints[i]
                maxPointsIndex = i
    #print (str(maxPointsIndex) + ": " + str(maxPoints))

    return fourCardHandArray[maxPointsIndex]

def chooseHandWithSuit(sixCardHandWithSuit, theDeck):
    """
    Returns the expected value of all the combinations of 4 card hands and chooses the highest one. If tie, randomly picks one from the tie.
        @date 12/5/2017
        @param sixCardHandWithSuit      the inputted array of six cards with their respectived suit
        @param theDeck                  the respective deck to the hand
        @return 
    """    
    sixCardHand = sort(removeSuit(sixCardHandWithSuit))
    fourCardHandArray = list(itertools.combinations(sixCardHand, 4))
    fourCardHandWithSuitArray = list(itertools.combinations(sixCardHandWithSuit, 4))
    #print(sixCardHand)
    fourCardHandArrayPoints = [None] * 16
    maxPoints = 0
    maxPointsIndex = 0
    for i in range (0,15):
        fourCardHand = list(fourCardHandArray[i])
        fourCardHandWithSuit = list(fourCardHandWithSuitArray[i])
        fourCardHandArrayPoints[i] = getPoints(fourCardHand) + probabilityPoints(fourCardHand, theDeck) + getPointsWithSuit(fourCardHandWithSuit)  + probabilityPointsWithSuit(fourCardHandWithSuit, theDeck)
        print(str(i) + ": " + str(fourCardHand) + " = " + str(fourCardHandArrayPoints[i]))
        if(fourCardHandArrayPoints[i] > maxPoints):
            maxPoints = fourCardHandArrayPoints[i]
            maxPointsIndex = i
        elif(fourCardHandArrayPoints[i] == maxPoints):
            randomNumber = random.randint(1,1001)
            if (randomNumber > 500):
                maxPoints = fourCardHandArrayPoints[i]
                maxPointsIndex = i
    print (str(maxPointsIndex) + ": " + str(maxPoints))

    return fourCardHandWithSuitArray[maxPointsIndex]

def probabilityPoints(hand, deck):
    deckNoSuits = removeSuit(deck)
    points = 0
    #print(Counter(deckNoSuits))
    #print(Counter(deckNoSuits).get(1))
    for i in range (1,14):
        hand.append(i)
        points += (getPoints(hand) * (Counter(deckNoSuits).get(i) / len(deckNoSuits)))
        hand.pop()
    return points

def probabilityPointsWithSuit(hand, deck):
    points = 0
    for i in range (1,14):
        for j in range (0,4):
            if (j == 0):
                letter = 'S'
            elif (j == 1):
                letter = 'C'
            elif (j == 2):
                letter = 'D'
            elif (j == 3):
                letter = 'H'
            hand.append(letter + str(i))
            points += (getPointsWithSuit(hand) * (1 / len(deck)))
            hand.pop()
    return points

def getPoints(hand):
    """
    Given a hand it returns the max amount of points the hand is able to get.
        @date 12/5/2017
        @param hand         the user hand
        @return points      max amount of points the user can get from a specific hand
    """
    maxPoints = 0
    maxPoints = fifteenPoints(findFifteen(hand)) + runPoints(findRun(hand)) + pairPoints(findPairs(hand)) 
    return maxPoints

def getPointsWithSuit(hand):
    """
    Given a hand with suits it returns the max amount of points the hand is able to get.
        @date 1/25/2018
        @param hand         the user hand with suits
        @return points      max amount of points the user can get from a specific hand
    """
    maxPoints = 0
    maxPoints = flush(hand) + nobs(hand)
    return maxPoints

#game aspects including the board and a card from the hand
def boardPairs(board, card): #return the amount of pair points for a specific board and one card from a hand
    points = 0
    length = len(board)
    if (length == 1):
        if (board[length-1] == card):
            points += 2
    elif (length == 2):
        if (board[length-2] == board[length-1] and board[length-1] == card):
            points += 6  
        elif (board[length-1] == card):
            points += 2
    elif (length >= 3):
        if (board[length-3] == board[length-2] and board[length-2] == board[length-1] and board[length-1] == card):
            points += 12  
        elif (board[length-2] == board[length-1] and board[length-1] == card):
            points += 6  
        elif (board[length-1] == card):
            points += 2            
    return points

def boardRuns(board, card): #return the amount of run points for a specific board and one card from a hand
    points = 0
    newBoard = []
    board.append(card)
    length = len(board)
    if (length == 3):
        newBoard.append(board[0])
        newBoard.append(board[1])
        newBoard.append(board[2])
        newBoard.sort(reverse = True)
        if (newBoard[length-1] + 2 == newBoard[length-2] + 1 and 
            newBoard[length-2] + 1 == newBoard[length-3]):
            points += 3
    elif (length == 4):
        newBoard.append(board[0])
        newBoard.append(board[1])
        newBoard.append(board[2])
        newBoard.append(board[3])
        newBoard.sort(reverse = True)
        if (newBoard[length-1] + 3 == newBoard[length-2] + 2 and 
            newBoard[length-2] + 2 == newBoard[length-3] + 1 and
            newBoard[length-3] + 1 == newBoard[length-4]):
            points += 4
    elif (length == 5):
        newBoard.append(board[0])
        newBoard.append(board[1])
        newBoard.append(board[2])
        newBoard.append(board[3])
        newBoard.append(board[4])
        newBoard.sort(reverse = True)
        if (newBoard[length-1] + 4 == newBoard[length-2] + 3 and 
            newBoard[length-2] + 3 == newBoard[length-3] + 2 and
            newBoard[length-3] + 2 == newBoard[length-4] + 1 and
            newBoard[length-4] + 1 == newBoard[length-5]):
            points += 5   
    elif (length == 6):
        newBoard.append(board[0])
        newBoard.append(board[1])
        newBoard.append(board[2])
        newBoard.append(board[3])
        newBoard.append(board[4])
        newBoard.append(board[5])
        newBoard.sort(reverse = True)
        if (newBoard[length-1] + 5 == newBoard[length-2] + 4 and 
            newBoard[length-2] + 4 == newBoard[length-3] + 3 and
            newBoard[length-3] + 3 == newBoard[length-4] + 2 and
            newBoard[length-4] + 2 == newBoard[length-5] + 1 and
            newBoard[length-5] + 1 == newBoard[length-6]):
            points += 6
    elif (length == 7):
        newBoard.append(board[0])
        newBoard.append(board[1])
        newBoard.append(board[2])
        newBoard.append(board[3])
        newBoard.append(board[4])
        newBoard.append(board[5])
        newBoard.append(board[6])
        newBoard.sort(reverse = True)
        if (newBoard[length-1] + 6 == newBoard[length-2] + 5 and 
            newBoard[length-2] + 5 == newBoard[length-3] + 4 and
            newBoard[length-3] + 4 == newBoard[length-4] + 3 and
            newBoard[length-4] + 3 == newBoard[length-5] + 2 and
            newBoard[length-5] + 2 == newBoard[length-6] + 1 and
            newBoard[length-6] + 1 == newBoard[length-7]):
            points += 7
    board.pop()
    return points
      
def boardNumbers(board, card): #return the amount of points, either for 15 or 31, for a specific board and one card from a hand
    points = 0
    board.append(card)
    length = len(board)
    sum = 0
    for i in range (length):
        sum += board[i]
    if (sum == 15 or sum == 31):
        points = 2
    board.pop()
    return points

def boardLastCard(board, card): #return the amount of points, for playing the last card, for a specific board and one card from a hand
    points = 0
    length = len(board)
    sum = 0
    for i in range (length):
        sum += board[i]
        if (sum == 15 or sum == 31):
            points = 2
    return points

#game aspects including the hand and the upCard
def handPairs(hand, upCard):
    handWithoutSuit = []
    for i in range (len(hand)):
        handWithoutSuit.append(hand[i][1:])
    handWithoutSuit.append(upCard[1:])
    print(handWithoutSuit)
    print(findPairs(handWithoutSuit))
    print(pairPoints(findPairs(handWithoutSuit)))

#The decisions and cribbage game
def decisionOnFirstCard(hand):
    handWithoutSuit = removeSuit(hand)
    intercept = 0.593350325167
    ace = six = seven = nine = intercept
    two = intercept - 0.00210846
    three = intercept - 0.1570842 
    four = intercept - 0.12435004
    five = intercept + 0.08971364
    eight = intercept - 0.01379082
    ten = intercept + 0.02634555
    jack = intercept + 0.04638059
    queen = intercept + 0.03179576
    king = intercept + 0.00691374
    d = {}
    for i in range (len(handWithoutSuit)):
        d1 = {}
        if (handWithoutSuit[i] == 1 or handWithoutSuit[i] == 6 or handWithoutSuit[i] == 7 or handWithoutSuit[i] == 9):
            d1 = {intercept: handWithoutSuit[i]}
        elif (handWithoutSuit[i] == 2):
            d1 = {two: handWithoutSuit[i]}
        elif (handWithoutSuit[i] == 3):
            d1 = {three: handWithoutSuit[i]}
        elif (handWithoutSuit[i] == 4):
            d1 = {four: handWithoutSuit[i]}
        elif (handWithoutSuit[i] == 5):
            d1 = {five: handWithoutSuit[i]}
        elif (handWithoutSuit[i] == 8):
            d1 = {eight: handWithoutSuit[i]}
        elif (handWithoutSuit[i] == 10):
            d1 = {ten: handWithoutSuit[i]}
        elif (handWithoutSuit[i] == 11):
            d1 = {jack: handWithoutSuit[i]}
        elif (handWithoutSuit[i] == 12):
            d1 = {queen: handWithoutSuit[i]}
        elif (handWithoutSuit[i] == 13):
            d1 = {king: handWithoutSuit[i]}
        d.update(d1)
    expectedValuesForHand_Array = []
    for k,v in d.items():
        expectedValuesForHand_Array.append(k)
    expectedValueForCardToPlay = min(expectedValuesForHand_Array)
    expectedValueForCardToPlay_Index =  np.argmin(expectedValuesForHand_Array)
    return (expectedValueForCardToPlay_Index)

def decisionOnFirstCardNoSuit(hand):
    #handWithoutSuit = removeSuit(hand)
    handWithoutSuit = hand
    intercept = 0.593350325167
    ace = six = seven = nine = intercept
    two = intercept - 0.00210846
    three = intercept - 0.1570842 
    four = intercept - 0.12435004
    five = intercept + 0.08971364
    eight = intercept - 0.01379082
    ten = intercept + 0.02634555
    jack = intercept + 0.04638059
    queen = intercept + 0.03179576
    king = intercept + 0.00691374
    d = {}
    for i in range (len(handWithoutSuit)):
        d1 = {}
        if (handWithoutSuit[i] == 1 or handWithoutSuit[i] == 6 or handWithoutSuit[i] == 7 or handWithoutSuit[i] == 9):
            d1 = {intercept: handWithoutSuit[i]}
        elif (handWithoutSuit[i] == 2):
            d1 = {two: handWithoutSuit[i]}
        elif (handWithoutSuit[i] == 3):
            d1 = {three: handWithoutSuit[i]}
        elif (handWithoutSuit[i] == 4):
            d1 = {four: handWithoutSuit[i]}
        elif (handWithoutSuit[i] == 5):
            d1 = {five: handWithoutSuit[i]}
        elif (handWithoutSuit[i] == 8):
            d1 = {eight: handWithoutSuit[i]}
        elif (handWithoutSuit[i] == 10):
            d1 = {ten: handWithoutSuit[i]}
        elif (handWithoutSuit[i] == 11):
            d1 = {jack: handWithoutSuit[i]}
        elif (handWithoutSuit[i] == 12):
            d1 = {queen: handWithoutSuit[i]}
        elif (handWithoutSuit[i] == 13):
            d1 = {king: handWithoutSuit[i]}
        d.update(d1)
    expectedValuesForHand_Array = []
    print("Probabilities for first Card Played:", d)
    for k,v in d.items():
        expectedValuesForHand_Array.append(k)
    expectedValueForCardToPlay = min(expectedValuesForHand_Array)
    expectedValueForCardToPlay_Index =  np.argmin(expectedValuesForHand_Array)
    
    return (expectedValueForCardToPlay_Index)

def decisionOnNextCard(board, hand):
    hand = removeSuit(hand)
    decisionOnNextCard_Dict = {}
    amountOfCards_Hand = len(hand)    
    sumOfPointsInTheBoard = 0
    for s in range (len(board)):
        sumOfPointsInTheBoard += board[s]
    for i in range (amountOfCards_Hand):
        if (sumOfPointsInTheBoard + hand[i] <= 31):
            points = 0
            points = boardPairs(board, hand[i]) + boardRuns(board, hand[i]) + boardNumbers(board, hand[i]) + boardLastCard(board, hand[i])
            #pairPoints = boardPairs(board, hand[i])
            #runPoints = boardRuns(board, hand[i])
            #fifteenAndThirtyOnePoints = boardNumbers(board, hand[i])
            d1 = {hand[i]: points}
            decisionOnNextCard_Dict.update(d1)
    #for k,v in decisionOnNextCard_Dict():
    arrayOfPoints = []
    maxPoints = 0
    maxPointsIndex = 0
    maxPointsCard = 0
    index = 0
    for k,v in decisionOnNextCard_Dict.items():
        #print ("k:", k, " v:", v)
        if (v > maxPoints):
            maxPoints = v
            maxPointsCard = k
            maxPointsIndex = index
        elif (v == maxPoints):
            if ((k + sumOfPointsInTheBoard <= 31 
                and k > maxPointsCard) 
                or k >= 15 
                or k != 21
                or k != 26):
                maxPoints = v
                maxPointsCard = k
                maxPointsIndex = index
            elif ((maxPointsCard + sumOfPointsInTheBoard <= 31
                and k < maxPointsCard) 
                or maxPointsCard >= 15 
                or maxPointsCard != 21
                or maxPointsCard != 26):
                maxPoints = maxPoints
                maxPointsCard = maxPointsCard
                maxPointsIndex = index
            elif (random.randint(1,101) > 50):
                maxPoints = v
                maxPointsCard = k
                maxPointsIndex = index
        index += 1
    #print("Card: ", maxPointsCard, "Points:", maxPoints, "Index:", maxPointsIndex)
    return maxPointsIndex

def oneHandCribbage():
    deck = createNewDeck()
    you_SixCardHand = drawAHand(deck)
    opponent_SixCardHand = drawAHand(deck)
    upCard = flipUpCard(deck)
    #deciding on who goes first
    randomNumber = random.randint(1,101)
    if (randomNumber > 50):
        firstPlayer = "You"
        secondPlayer = "Bill"
        #you_FourCardHand = list(pickingAHandYourCrib(you_SixCardHand, deck))
        #opponent_FourCardHand = list(pickingAHandOpponentsCrib(opponent_SixCardHand, deck))
    else:
        firstPlayer = "Bill"
        secondPlayer = "You"
        #you_FourCardHand = list(pickingAHandOpponentsCrib(you_SixCardHand, deck))
        #opponent_FourCardHand = list(pickingAHandYourCrib(opponent_SixCardHand, deck))
    print("You 6 card Hand: ", you_SixCardHand)
    print("Bill's 6 card Hand: ", opponent_SixCardHand)
    you_FourCardHand = list(chooseHandWithSuit(you_SixCardHand, deck))
    opponent_FourCardHand = list(chooseHandWithSuit(opponent_SixCardHand, deck))
    """
    you_points = 0 #keeps track of the points gained for this hand Round
    you_points_dictionary = {} #takes account of all the reasons why points were gained
    opponent_points = 0 #keeps track of the points gained for this hand Round
    opponent_points_dictionary = {} #takes account of all the reasons why points were gained
    """
    crib = []
    activeBoard = []
    allCardsPlayed = []
    sumOfActiveBoard = 0
    roundNumber = 1
    for i in range(6):
        if (str(you_SixCardHand[i]) != str(you_FourCardHand[0]) and
            str(you_SixCardHand[i]) != str(you_FourCardHand[1]) and
            str(you_SixCardHand[i]) != str(you_FourCardHand[2]) and
            str(you_SixCardHand[i]) != str(you_FourCardHand[3])):
            crib.append(str(you_SixCardHand[i]))
        if (str(opponent_SixCardHand[i]) != str(opponent_FourCardHand[0]) and
            str(opponent_SixCardHand[i]) != str(opponent_FourCardHand[1]) and
            str(opponent_SixCardHand[i]) != str(opponent_FourCardHand[2]) and
            str(opponent_SixCardHand[i]) != str(opponent_FourCardHand[3])):
            crib.append(str(opponent_SixCardHand[i]))
    print("You 4 card Hand: ", you_FourCardHand)
    print("Bill's 4 card Hand: ", opponent_FourCardHand)
    print("Crib: ", crib)
    print("UpCard: ", upCard)
    #print(handPairs(you_FourCardHand,upCard))
    #deciding on who goes first
    if (firstPlayer == "You"):
        cardPlayed = you_FourCardHand.pop(decisionOnFirstCard(you_FourCardHand))[1:]
    else:
        cardPlayed = opponent_FourCardHand.pop(decisionOnFirstCard(opponent_FourCardHand))[1:]
    cardPlayed = int(cardPlayed)
    if (cardPlayed >= 10):
        sumOfActiveBoard += 10
    else:
        sumOfActiveBoard += cardPlayed    
    activeBoard.append(cardPlayed)
    print("_______________________________________________________________________________________________________")
    print("|                                                                                                     |")
    print("|                                                Game                                                 |")
    print("|_____________________________________________________________________________________________________|")
    print('{0: >11}'.format("Round " + str(roundNumber)))
    roundNumber += 1
    print("Card played by", str(firstPlayer), ":", str(cardPlayed))
    print("Cards on the board:", activeBoard)
    print("Sum of the Active Board: ", sumOfActiveBoard)
    print("You Hand: ", you_FourCardHand)
    print("Bill's Hand: ", opponent_FourCardHand)
    while (len(you_FourCardHand) != 0 or len(opponent_FourCardHand) != 0):
        print('{0: >11}'.format("Round " + str(roundNumber)))
        roundNumber += 1
        if (len(you_FourCardHand) >= len(opponent_FourCardHand)):
            cardPlayed = you_FourCardHand.pop(decisionOnNextCard(activeBoard, you_FourCardHand))[1:]
            print("Next Card played by You:", cardPlayed)
        else:
            cardPlayed = opponent_FourCardHand.pop(decisionOnNextCard(activeBoard, opponent_FourCardHand))[1:]
            print("Next Card played by Bill:", cardPlayed)
        cardPlayed = int(cardPlayed)
        if (cardPlayed + sumOfActiveBoard <= 31):
            if (cardPlayed >= 10):
                sumOfActiveBoard += 10
            else:
                sumOfActiveBoard += cardPlayed 
        else:
            if (cardPlayed >= 10):
                sumOfActiveBoard = 10
            else:
                sumOfActiveBoard = cardPlayed 
            for i in range(len(activeBoard)):
                allCardsPlayed.append(activeBoard.pop())
        activeBoard.append(int(cardPlayed))
        print("Cards on the board:", activeBoard)
        print("Sum of the Active Board: ", sumOfActiveBoard)
        print("You Hand: ", you_FourCardHand)
        print("Bill's Hand: ", opponent_FourCardHand)

def oneHandCribbageSpecificHand(yourHand,opponentsHand):
    deck = createNewDeck()
    you_SixCardHand = drawSpecificHand(yourHand,deck)
    opponent_SixCardHand = drawSpecificHand(opponentsHand,deck)
    upCard = flipUpCard(deck)
    #deciding on who goes first
    randomNumber = random.randint(1,101)
    if (randomNumber > 50):
        firstPlayer = "You"
        secondPlayer = "Bill"
        #you_FourCardHand = list(pickingAHandYourCrib(you_SixCardHand, deck))
        #opponent_FourCardHand = list(pickingAHandOpponentsCrib(opponent_SixCardHand, deck))
    else:
        firstPlayer = "Bill"
        secondPlayer = "You"
        #you_FourCardHand = list(pickingAHandOpponentsCrib(you_SixCardHand, deck))
        #opponent_FourCardHand = list(pickingAHandYourCrib(opponent_SixCardHand, deck))
    print("You 6 card Hand: ", you_SixCardHand)
    print("Bill's 6 card Hand: ", opponent_SixCardHand)
    you_FourCardHand = list(chooseHandWithSuit(you_SixCardHand, deck))
    opponent_FourCardHand = list(chooseHandWithSuit(opponent_SixCardHand, deck))
    """
    you_points = 0 #keeps track of the points gained for this hand Round
    you_points_dictionary = {} #takes account of all the reasons why points were gained
    opponent_points = 0 #keeps track of the points gained for this hand Round
    opponent_points_dictionary = {} #takes account of all the reasons why points were gained
    """
    crib = []
    activeBoard = []
    allCardsPlayed = []
    sumOfActiveBoard = 0
    roundNumber = 1
    for i in range(6):
        if (str(you_SixCardHand[i]) != str(you_FourCardHand[0]) and
            str(you_SixCardHand[i]) != str(you_FourCardHand[1]) and
            str(you_SixCardHand[i]) != str(you_FourCardHand[2]) and
            str(you_SixCardHand[i]) != str(you_FourCardHand[3])):
            crib.append(str(you_SixCardHand[i]))
        if (str(opponent_SixCardHand[i]) != str(opponent_FourCardHand[0]) and
            str(opponent_SixCardHand[i]) != str(opponent_FourCardHand[1]) and
            str(opponent_SixCardHand[i]) != str(opponent_FourCardHand[2]) and
            str(opponent_SixCardHand[i]) != str(opponent_FourCardHand[3])):
            crib.append(str(opponent_SixCardHand[i]))
    print("You 4 card Hand: ", you_FourCardHand)
    print("Bill's 4 card Hand: ", opponent_FourCardHand)
    print("Crib: ", crib)
    print("UpCard: ", upCard)
    #print(handPairs(you_FourCardHand,upCard))
    #deciding on who goes first
    if (firstPlayer == "You"):
        cardPlayed = you_FourCardHand.pop(decisionOnFirstCard(you_FourCardHand))[1:]
    else:
        cardPlayed = opponent_FourCardHand.pop(decisionOnFirstCard(opponent_FourCardHand))[1:]
    cardPlayed = int(cardPlayed)
    if (cardPlayed >= 10):
        sumOfActiveBoard += 10
    else:
        sumOfActiveBoard += cardPlayed    
    activeBoard.append(cardPlayed)
    print("_______________________________________________________________________________________________________")
    print("|                                                                                                     |")
    print("|                                                Game                                                 |")
    print("|_____________________________________________________________________________________________________|")
    print('{0: >11}'.format("Round " + str(roundNumber)))
    roundNumber += 1
    print("Card played by", str(firstPlayer), ":", str(cardPlayed))
    print("Cards on the board:", activeBoard)
    print("Sum of the Active Board: ", sumOfActiveBoard)
    print("You Hand: ", you_FourCardHand)
    print("Bill's Hand: ", opponent_FourCardHand)
    while (len(you_FourCardHand) != 0 or len(opponent_FourCardHand) != 0):
        print('{0: >11}'.format("Round " + str(roundNumber)))
        roundNumber += 1
        if (len(you_FourCardHand) >= len(opponent_FourCardHand)):
            cardPlayed = you_FourCardHand.pop(decisionOnNextCard(activeBoard, you_FourCardHand))[1:]
            print("Next Card played by You:", cardPlayed)
        else:
            cardPlayed = opponent_FourCardHand.pop(decisionOnNextCard(activeBoard, opponent_FourCardHand))[1:]
            print("Next Card played by Bill:", cardPlayed)
        cardPlayed = int(cardPlayed)
        if (cardPlayed + sumOfActiveBoard <= 31):
            if (cardPlayed >= 10):
                sumOfActiveBoard += 10
            else:
                sumOfActiveBoard += cardPlayed 
        else:
            if (cardPlayed >= 10):
                sumOfActiveBoard = 10
            else:
                sumOfActiveBoard = cardPlayed 
            for i in range(len(activeBoard)):
                allCardsPlayed.append(activeBoard.pop())
        activeBoard.append(int(cardPlayed))
        print("Cards on the board:", activeBoard)
        print("Sum of the Active Board: ", sumOfActiveBoard)
        print("You Hand: ", you_FourCardHand)
        print("Bill's Hand: ", opponent_FourCardHand)

#def pegging(playerOneHand, playerTwoHand):
    
#def theBoard(card):
#oneHandCribbage()
