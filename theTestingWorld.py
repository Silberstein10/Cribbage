from cribbageGameFunctions import *
from dataAnalysis import *
import json
import itertools


deck = ["A","2","3","4","5","6","7","8","9","10","J","Q","K"]
deckAsInt = []

#card = "7"
for i in range(0,13):
    card = deck[i]
    deckAsInt.append(cardValue(card))
    #print("The card value is: " + str(cardValue(card)))

"""
card1 = deck[5]
card2 = deck[8]

print(card1) #6
print(card2) #9
print(fifteen(card1,card2))

card3 = deck[5]
card4 = deck[5]

print(card3) #6
print(card4) #6
print(pairs(card3,card4))
"""
handA = [deckAsInt[4], deckAsInt[2], deckAsInt[9], deckAsInt[3], deckAsInt[5]]
handB = [deckAsInt[4], deckAsInt[4], deckAsInt[4], deckAsInt[4], deckAsInt[5]]
handC = [deckAsInt[0], deckAsInt[6], deckAsInt[5], deckAsInt[6], deckAsInt[7]]
handD = [deckAsInt[1], deckAsInt[2], deckAsInt[3], deckAsInt[4], deckAsInt[5]]
handE = [deckAsInt[1], deckAsInt[1], deckAsInt[2], deckAsInt[3], deckAsInt[4]]
handF = [deckAsInt[1], deckAsInt[2], deckAsInt[2], deckAsInt[3], deckAsInt[3]]
handG = [deckAsInt[9], deckAsInt[9], deckAsInt[10], deckAsInt[10], deckAsInt[11]]

#print(sort(handA))
#print(handD)
#print(findPairs(handB)) #works
#print(findFifteen(handC)) #works
#print(str(handG) + ": " + str(findRun(handG))) #works


#oneGameReader('Cribbage_Data_Files/6.json')

"""
config = json.loads(open('Cribbage_Data_Files/6.json').read()) #opens the barebones json file.
print(config)
"""
createCSVFile() #creats the excel worksheet

deck = createNewDeck()
deck2 = createNewDeck()
deck3 = createNewDeck()
#theSpecificHand = ['C2','C3','C5','D5','S6','D10']
#playerOneHand = drawAHand(deck)
#specfichand = drawSpecificHand(theSpecificHand, deck2)
#print(chooseHand(playerOneHand, deck))
#print(chooseHand(specfichand, deck2))
handOne = drawAHand(deck3)
handTwo = drawAHand(deck3)
playerOneHand = pickingAHandYourCrib(handOne, deck3)
playerTwoHand = pickingAHandOpponentsCrib(handTwo, deck3)
print("PlayerOne Hand: ", playerOneHand)
print("PlayerTwo Hand: ", playerTwoHand)
print(len(deck3))
#print()
#print(pickingAHandOpponentsCrib(specfichand, deck2))
