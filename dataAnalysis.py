import json
import csv
import numpy as np
import pandas as pd
import statsmodels.api as sm
import statsmodels
from pandas import read_csv
from cribbageGameFunctions import *
import matplotlib.pyplot as plt
import numpy
from sklearn import linear_model
from sklearn.preprocessing import MultiLabelBinarizer
import random

#prints one json file at a time
def oneGameReader(dataFile):
    """
    Prints out one json file.
        @date 12/5/2017
        @param dataFile   name of the json file
    """
    gameNumber = dataFile[20 : len(dataFile)-5]
    #'Cribbage_Data_Files/1.json'
    config = json.loads(open(dataFile).read())
    #print(config)
    #print(len(config)) #tells us how many items are in the first layer of the list
    print('__________________________________________________________________________________________________________________')
    print('|                                                                                                                |')
    print('|                                                                                                                |')
    print('                                                    Game ' + gameNumber + '                                                     ')
    print('|                                                                                                                |')
    print('|________________________________________________________________________________________________________________|')
    print('Players: ' + str(config['players']))
    print('Winner: ' + str(config['winner']))
    print('Final Scores: ' + str(config['finalScores']))
    print('__________________________________________________________________________________________________________________')
    print('Amount of Rounds: ' + str(len(config['rounds']))) #gives us the amount of rounds in the game
    #print('"Bill" Initial Hand: ' + str(config['rounds'][0-8][]...[]))  this tells us how many times to loop through 'rounds' = 8 for this game
    r = 0 #the round iterating through
    p = 7 #the pegging round iterating through
    amountOfRounds = len(config['rounds'])
    for r in range(0, amountOfRounds):
        print('__________________________________________________________________________________________________________________')
        print('|                                                                                                                |')
        print('|                                                   Round ' + str(r) + '                                                      |')
        print('|________________________________________________________________________________________________________________|')
        print('Dealer: ' + str(config['rounds'][r]['dealer'])) #the dealer of that round
        print('Round Start Score: ' + str(config['rounds'][r]['roundStartScore']))
        print('Round End Score: ' + str(config['rounds'][r]['roundEndScore']))
        print('"You" Initial Hand: ' + str(config['rounds'][r]['initialHands']['You']))
        print('"Bill" Initial Hand: ' + str(config['rounds'][r]['initialHands']['Bill']))
        print('Cards in the Crib: ' + str(config['rounds'][r]['crib']['cards']))
        print('Cards "You" put in the Crib: ' + str(config['rounds'][r]['crib']['You']))
        print('Cards "Bill" put in the Crib: ' + str(config['rounds'][r]['crib']['Bill']))
        print('"You" cards held for pegging: ' + str(config['rounds'][r]['peggingHands']['You']))
        print('"Bill" cards held for pegging: ' + str(config['rounds'][r]['peggingHands']['Bill']))
        #### FINISH ORGANZING THE FIRST GAME
        print('____________________________________________________________________________________________________________')
        print('|                                                                                                          |')
        print('|                                                   Pegging                                                |')
        print('|__________________________________________________________________________________________________________|')
        amountOfPegging = len(config['rounds'][r]['pegging']['moves'])
        for p in range(0, amountOfPegging):
            print('The upCard: ' + str(config['rounds'][r]['pegging']['cutCard']))
            #print(len(config['rounds'][r]['pegging']['moves'])) this gives the length of the "moves" array
            print('The "Type": ' + str(config['rounds'][r]['pegging']['moves'][p]['type']))
            print('Who played: ' + str(config['rounds'][r]['pegging']['moves'][p]['player']))
            print('The card played: ' + str(config['rounds'][r]['pegging']['moves'][p]['card']))
            print('The currentBoardValue: ' + str(config['rounds'][r]['pegging']['moves'][p]['currentBoardValue']))
            print('All cards that have been played: ' + str(config['rounds'][r]['pegging']['moves'][p]['allTableCards']))
            print('All cards that are on the board: ' + str(config['rounds'][r]['pegging']['moves'][p]['activeTableCards']))
            print('Pegging score: ' + str(config['rounds'][r]['pegging']['moves'][p]['playScore']))
            if(len(config['rounds'][r]['pegging']['moves'][p]['scores']) > 0):
                for s in range(0, len(config['rounds'][r]['pegging']['moves'][p]['scores'])):
                    print('"Pegging score" details (id) : ' + str(config['rounds'][r]['pegging']['moves'][p]['scores'][s]['id']))
                    print('"Pegging score" details (score): ' + str(config['rounds'][r]['pegging']['moves'][p]['scores'][s]['score']))
                    print('"Pegging score" details (cards): ' + str(config['rounds'][r]['pegging']['moves'][p]['scores'][s]['cards']))
        print('____________________________________________________________________________________________________________')
        print('|                                                                                                          |')
        print('|                                                   Scoring                                                |')
        print('|__________________________________________________________________________________________________________|')
        print('_______________')
        print('|    "You"    |')
        print('|_____________|')
        print('The Hand "Total Score": ' + str(config['rounds'][r]['scoring']['You']['hand']['totalScore']))
        print('The Hand "Combinations": ' + str(config['rounds'][r]['scoring']['You']['hand']['combinations']))
        #print(len(config['rounds'][r]['scoring']['You']['hand']['combinations'])) length of combinations
        for c in range(0, len(config['rounds'][r]['scoring']['You']['hand']['combinations'])):
            print('"Combinations" details (id): ' + str(config['rounds'][r]['scoring']['You']['hand']['combinations'][c]['id']))
            print('"Combinations" details (score): ' + str(config['rounds'][r]['scoring']['You']['hand']['combinations'][c]['score']))
            print('"Combinations" details (cards): ' + str(config['rounds'][r]['scoring']['You']['hand']['combinations'][c]['cards']))
        print('"You" Crib: ' + str(config['rounds'][r]['scoring']['You']['crib']))
        if(config['rounds'][r]['scoring']['You']['crib'] is not None):
            print('The Crib "Total Score": ' + str(config['rounds'][r]['scoring']['You']['crib']['totalScore']))
            print('The Crib "Combinations": ' + str(config['rounds'][r]['scoring']['You']['crib']['combinations']))
        print('________________')
        print('|    "Bill"    |')
        print('|______________|')
        print('The Hand "Total Score": ' + str(config['rounds'][r]['scoring']['Bill']['hand']['totalScore']))
        print('The Hand "Combinations": ' + str(config['rounds'][r]['scoring']['Bill']['hand']['combinations']))
        #print(len(config['rounds'][r]['scoring']['Bill']['hand']['combinations'])) length of combinations
        for c in range(0, len(config['rounds'][r]['scoring']['Bill']['hand']['combinations'])):
            print('"Combinations" details (id): ' + str(config['rounds'][r]['scoring']['Bill']['hand']['combinations'][c]['id']))
            print('"Combinations" details (score): ' + str(config['rounds'][r]['scoring']['Bill']['hand']['combinations'][c]['score']))
            print('"Combinations" details (cards): ' + str(config['rounds'][r]['scoring']['Bill']['hand']['combinations'][c]['cards']))
        print('"Bill" Crib: ' + str(config['rounds'][r]['scoring']['Bill']['crib']))
        if(config['rounds'][r]['scoring']['Bill']['crib'] is not None):
            print('The Crib "Total Score": ' + str(config['rounds'][r]['scoring']['Bill']['crib']['totalScore']))
            print('The Crib "Combinations": ' + str(config['rounds'][r]['scoring']['Bill']['crib']['combinations']))
            #print(len(config['rounds'][r]['scoring']['Bill']['hand']['combinations'])) length of combinations
            """
            print(len(config['rounds'][r]['scoring']['Bill']['hand']['combinations']))
            if(len(config['rounds'][r]['scoring']['Bill']['hand']['combinations']) > 0):
                print('"Combinations" details (id): ' + str(config['rounds'][r]['scoring']['Bill']['crib']['combinations'][2]['id']))
                print('"Combinations" details (score): ' + str(config['rounds'][r]['scoring']['Bill']['crib']['combinations'][2]['score']))
                print('"Combinations" details (cards): ' + str(config['rounds'][r]['scoring']['Bill']['crib']['combinations'][2]['cards']))
            """
        done = "Finished running through: " + dataFile    
    return done

#creates an excel sheet called AllGames.csv reading all the initial json files.
def createCSVFile():
    """
    Creates the excel sheet (AllGames.csv) by reading all the json files.
        @date 12/5/2017
    """
    with open('AllGames.csv', 'w') as csvFile:
        fieldnames = ['Game', 
                        'Hand_Round', 
                        'Dealer', 
                        'Round_Start_Score_"You"', 
                        'Round_End_Score_"You"', 
                        'Round_Start_Score_"Bill"', 
                        'Round_End_Score_"Bill"',
                        '"You"_Initial_Hand_FirstCard_Suit', '"You"_Initial_Hand_FirstCard_Number', 
                        '"You"_Initial_Hand_SecondCard_Suit', '"You"_Initial_Hand_SecondCard_Number', 
                        '"You"_Initial_Hand_ThirdCard_Suit', '"You"_Initial_Hand_ThirdCard_Number', 
                        '"You"_Initial_Hand_FourthCard_Suit', '"You"_Initial_Hand_FourthCard_Number', 
                        '"You"_Initial_Hand_FifthCard_Suit', '"You"_Initial_Hand_FifthCard_Number', 
                        '"You"_Initial_Hand_SixthCard_Suit', '"You"_Initial_Hand_SixthCard_Number', 
                        '"Bill"_Initial_Hand_FirstCard_Suit', '"Bill"_Initial_Hand_FirstCard_Number', 
                        '"Bill"_Initial_Hand_SecondCard_Suit', '"Bill"_Initial_Hand_SecondCard_Number', 
                        '"Bill"_Initial_Hand_ThirdCard_Suit', '"Bill"_Initial_Hand_ThirdCard_Number', 
                        '"Bill"_Initial_Hand_FourthCard_Suit', '"Bill"_Initial_Hand_FourthCard_Number', 
                        '"Bill"_Initial_Hand_FifthCard_Suit', '"Bill"_Initial_Hand_FifthCard_Number', 
                        '"Bill"_Initial_Hand_SixthCard_Suit', '"Bill"_Initial_Hand_SixthCard_Number', 
                        'Cards_In_The_Crib_FirstCard_Suit', 'Cards_In_The_Crib_FirstCard_Number', 
                        'Cards_In_The_Crib_SecondCard_Suit', 'Cards_In_The_Crib_SecondCard_Number',
                        'Cards_In_The_Crib_ThirdCard_Suit', 'Cards_In_The_Crib_ThirdCard_Number', 
                        'Cards_In_The_Crib_FourthCard_Suit', 'Cards_In_The_Crib_FourthCard_Number',  
                        'Cards_"You"_Put_In_Crib_FirstCard_Suit', 'Cards_"You"_Put_In_Crib_FirstCard_Number', 
                        'Cards_"You"_Put_In_Crib_SecondCard_Suit', 'Cards_"You"_Put_In_Crib_SecondCard_Number', 
                        'Cards_"Bill"_Put_In_Crib_FirstCard_Suit', 'Cards_"Bill"_Put_In_Crib_FirstCard_Number', 
                        'Cards_"Bill"_Put_In_Crib_SecondCard_Suit', 'Cards_"Bill"_Put_In_Crib_SecondCard_Number', 
                        'Cards_In_"You"_Hand_FirstCard_Suit', 'Cards_In_"You"_Hand_FirstCard_Number',
                        'Cards_In_"You"_Hand_SecondCard_Suit', 'Cards_In_"You"_Hand_SecondCard_Number',
                        'Cards_In_"You"_Hand_ThirdCard_Suit', 'Cards_In_"You"_Hand_ThirdCard_Number',
                        'Cards_In_"You"_Hand_FourthCard_Suit', 'Cards_In_"You"_Hand_FourthCard_Number',
                        'Cards_In_"Bill"_Hand_FirstCard_Suit', 'Cards_In_"Bill"_Hand_FirstCard_Number',
                        'Cards_In_"Bill"_Hand_SecondCard_Suit', 'Cards_In_"Bill"_Hand_SecondCard_Number',
                        'Cards_In_"Bill"_Hand_ThirdCard_Suit', 'Cards_In_"Bill"_Hand_ThirdCard_Number',
                        'Cards_In_"Bill"_Hand_FourthCard_Suit', 'Cards_In_"Bill"_Hand_FourthCard_Number',
                        'Pegging_Round', 
                        'UpCard_Suit', 
                        'UpCard_Number',
                        'The_Type',  
                        'Player',
                        'Card_Played',
                        'Card_Played_Suit',
                        'Card_Played_Number',
                        'Current_Board_Value',  
                        'All_Cards_On_The_Active_Board', 
                        'All_Cards_Played', 
                        'Pegging_Total_Score', 
                        'Pegging_Score_ID', 
                        'Pegging_Score_Array',
                        'Pegging_Score_Sum',  
                        'Pegging_Score_Cards', 
                        'Scoring_"You"', 
                        'Combinations_ID', 
                        'Combinations_Score', 
                        'Combinations_Cards', 
                        'Total_Score', 
                        'Crib', 
                        'Crib_Total_Score', 
                        'Crib_Combinations', 
                        'Scoring_"Bill"',
                        'Combinations_ID', 
                        'Combinations_Score', 
                        'Combinations_Cards', 
                        'Total_Score', 
                        'Crib', 
                        'Crib_Total_Score', 
                        'Crib_Combinations',]
        writer = csv.DictWriter(csvFile, fieldnames = fieldnames, lineterminator = '\n')

        writer.writeheader()

        for g in range(1,1001):
            dataFile = 'Cribbage_Data_Files/'+ str(g) + '.json'
            #dataFile = 'Cribbage_Data_Files/1.json'     #the json file
            gameNumber = dataFile[20 : len(dataFile)-5] #gets the number of game
            config = json.loads(open(dataFile).read())  #reads the json file
            amountOfRounds = len(config['rounds'])      #gets the amount of rounds in a single game
            for r in range(0, amountOfRounds):           
                You_handCombinations_ID = None
                You_handCombinations_Score = None 
                You_handCombinations_Cards = None
                Bill_handCombinations_ID = None
                Bill_handCombinations_Score = None
                Bill_handCombinations_Cards = None
                You_Crib_totalScore = None
                You_Crib_Combinations = None
                Bill_Crib_totalScore = None
                Bill_Crib_Combinations = None
                if (len(config['rounds'][r]['scoring']['You']['hand']['combinations']) > 0):
                    for c in range(0, len(config['rounds'][r]['scoring']['You']['hand']['combinations'])):
                        You_handCombinations_ID = str(config['rounds'][r]['scoring']['You']['hand']['combinations'][c]['id'])
                        You_handCombinations_Score = str(config['rounds'][r]['scoring']['You']['hand']['combinations'][c]['score'])
                        You_handCombinations_Cards = str(config['rounds'][r]['scoring']['You']['hand']['combinations'][c]['cards'])
                if (len(config['rounds'][r]['scoring']['Bill']['hand']['combinations']) > 0):
                    for c in range(0, len(config['rounds'][r]['scoring']['Bill']['hand']['combinations'])):
                        Bill_handCombinations_ID = str(config['rounds'][r]['scoring']['Bill']['hand']['combinations'][c]['id'])
                        Bill_handCombinations_Score = str(config['rounds'][r]['scoring']['Bill']['hand']['combinations'][c]['score'])
                        Bill_handCombinations_Cards = str(config['rounds'][r]['scoring']['Bill']['hand']['combinations'][c]['cards'])
                if(config['rounds'][r]['scoring']['You']['crib'] is not None):
                    You_Crib_totalScore = str(config['rounds'][r]['scoring']['You']['crib']['totalScore'])
                    You_Crib_Combinations = str(config['rounds'][r]['scoring']['You']['crib']['combinations'])
                if(config['rounds'][r]['scoring']['Bill']['crib'] is not None):
                    Bill_Crib_totalScore = str(config['rounds'][r]['scoring']['Bill']['crib']['totalScore'])
                    Bill_Crib_Combinations = str(config['rounds'][r]['scoring']['Bill']['crib']['combinations'])
                    
                amountOfPeggingRounds = len(config['rounds'][r]['pegging']['moves'])
                for p in range(0, amountOfPeggingRounds):
                    peggingScore_ID = []
                    peggingScore_Array = []
                    peggingScore_Cards = []
                    peggingScore_Sum = 0
                    #fix pegging only getting one combination of scores and inputting it into the excel as well as getting the sum of each pegging round
                    if(len(config['rounds'][r]['pegging']['moves'][p]['scores']) > 0):
                        for s in range(0, len(config['rounds'][r]['pegging']['moves'][p]['scores'])):
                            peggingScore_ID.append(str(config['rounds'][r]['pegging']['moves'][p]['scores'][s]['id']))
                            peggingScore_Array.append(str(config['rounds'][r]['pegging']['moves'][p]['scores'][s]['score']))
                            peggingScore_Cards.append(str(config['rounds'][r]['pegging']['moves'][p]['scores'][s]['cards']))
                            peggingScore_Sum += config['rounds'][r]['pegging']['moves'][p]['scores'][s]['score']
                    
                    #getting the suit and number of each card played during the pegging round
                    if (config['rounds'][r]['pegging']['moves'][p]['card'] is not None):
                        Card_Played_Suit = config['rounds'][r]['pegging']['moves'][p]['card'][0:1]
                        Card_Played_Number = config['rounds'][r]['pegging']['moves'][p]['card'][1: ] + '.0'
                    else:
                        Card_Played_Suit = "Z"
                        Card_Played_Number = "Z"
                        
                    #Writing all the Data into the Excel Spreadsheet
                    writer.writerow({                   
                        'Game': g, 
                        'Hand_Round': r, 
                        'Dealer': str(config['rounds'][r]['dealer']), 
                        'Round_Start_Score_"You"': str(config['rounds'][r]['roundStartScore']['You']), 
                        'Round_End_Score_"You"': str(config['rounds'][r]['roundEndScore']['You']), 
                        'Round_Start_Score_"Bill"': str(config['rounds'][r]['roundStartScore']['Bill']),  
                        'Round_End_Score_"Bill"': str(config['rounds'][r]['roundEndScore']['Bill']),
                        '"You"_Initial_Hand_FirstCard_Suit': str(config['rounds'][r]['initialHands']['You'][0][0:1]), #[0:1] is how you do substring in python
                        '"You"_Initial_Hand_FirstCard_Number': str(config['rounds'][r]['initialHands']['You'][0][1: ]),
                        '"You"_Initial_Hand_SecondCard_Suit': str(config['rounds'][r]['initialHands']['You'][1][0:1]), 
                        '"You"_Initial_Hand_SecondCard_Number': str(config['rounds'][r]['initialHands']['You'][1][1: ]),
                        '"You"_Initial_Hand_ThirdCard_Suit': str(config['rounds'][r]['initialHands']['You'][2][0:1]), 
                        '"You"_Initial_Hand_ThirdCard_Number': str(config['rounds'][r]['initialHands']['You'][2][1: ]),
                        '"You"_Initial_Hand_FourthCard_Suit': str(config['rounds'][r]['initialHands']['You'][3][0:1]), 
                        '"You"_Initial_Hand_FourthCard_Number': str(config['rounds'][r]['initialHands']['You'][3][1: ]),
                        '"You"_Initial_Hand_FifthCard_Suit': str(config['rounds'][r]['initialHands']['You'][4][0:1]), 
                        '"You"_Initial_Hand_FifthCard_Number': str(config['rounds'][r]['initialHands']['You'][4][1: ]),
                        '"You"_Initial_Hand_SixthCard_Suit': str(config['rounds'][r]['initialHands']['You'][5][0:1]), 
                        '"You"_Initial_Hand_SixthCard_Number': str(config['rounds'][r]['initialHands']['You'][5][1: ]),
                        '"Bill"_Initial_Hand_FirstCard_Suit': str(config['rounds'][r]['initialHands']['Bill'][0][0:1]), 
                        '"Bill"_Initial_Hand_FirstCard_Number': str(config['rounds'][r]['initialHands']['Bill'][0][1: ]),
                        '"Bill"_Initial_Hand_SecondCard_Suit': str(config['rounds'][r]['initialHands']['Bill'][1][0:1]), 
                        '"Bill"_Initial_Hand_SecondCard_Number': str(config['rounds'][r]['initialHands']['Bill'][1][1: ]),
                        '"Bill"_Initial_Hand_ThirdCard_Suit': str(config['rounds'][r]['initialHands']['Bill'][2][0:1]), 
                        '"Bill"_Initial_Hand_ThirdCard_Number': str(config['rounds'][r]['initialHands']['Bill'][2][1: ]),
                        '"Bill"_Initial_Hand_FourthCard_Suit': str(config['rounds'][r]['initialHands']['Bill'][3][0:1]), 
                        '"Bill"_Initial_Hand_FourthCard_Number': str(config['rounds'][r]['initialHands']['Bill'][3][1: ]),
                        '"Bill"_Initial_Hand_FifthCard_Suit': str(config['rounds'][r]['initialHands']['Bill'][4][0:1]), 
                        '"Bill"_Initial_Hand_FifthCard_Number': str(config['rounds'][r]['initialHands']['Bill'][4][1: ]),
                        '"Bill"_Initial_Hand_SixthCard_Suit': str(config['rounds'][r]['initialHands']['Bill'][5][0:1]), 
                        '"Bill"_Initial_Hand_SixthCard_Number': str(config['rounds'][r]['initialHands']['Bill'][5][1: ]),
                        'Cards_In_The_Crib_FirstCard_Suit': str(config['rounds'][r]['crib']['cards'][0][0:1]), 
                        'Cards_In_The_Crib_FirstCard_Number': str(config['rounds'][r]['crib']['cards'][0][1: ]), 
                        'Cards_In_The_Crib_SecondCard_Suit': str(config['rounds'][r]['crib']['cards'][1][0:1]), 
                        'Cards_In_The_Crib_SecondCard_Number': str(config['rounds'][r]['crib']['cards'][1][1: ]),
                        'Cards_In_The_Crib_ThirdCard_Suit': str(config['rounds'][r]['crib']['cards'][2][0:1]), 
                        'Cards_In_The_Crib_ThirdCard_Number': str(config['rounds'][r]['crib']['cards'][2][1: ]), 
                        'Cards_In_The_Crib_FourthCard_Suit': str(config['rounds'][r]['crib']['cards'][3][0:1]), 
                        'Cards_In_The_Crib_FourthCard_Number': str(config['rounds'][r]['crib']['cards'][3][1: ]),  
                        'Cards_"You"_Put_In_Crib_FirstCard_Suit': str(config['rounds'][r]['crib']['You'][0][0:1]), 
                        'Cards_"You"_Put_In_Crib_FirstCard_Number': str(config['rounds'][r]['crib']['You'][0][1: ]), 
                        'Cards_"You"_Put_In_Crib_SecondCard_Suit': str(config['rounds'][r]['crib']['You'][1][0:1]), 
                        'Cards_"You"_Put_In_Crib_SecondCard_Number': str(config['rounds'][r]['crib']['You'][1][1: ]), 
                        'Cards_"Bill"_Put_In_Crib_FirstCard_Suit': str(config['rounds'][r]['crib']['Bill'][0][0:1]), 
                        'Cards_"Bill"_Put_In_Crib_FirstCard_Number': str(config['rounds'][r]['crib']['Bill'][0][1: ]), 
                        'Cards_"Bill"_Put_In_Crib_SecondCard_Suit': str(config['rounds'][r]['crib']['Bill'][1][0:1]), 
                        'Cards_"Bill"_Put_In_Crib_SecondCard_Number': str(config['rounds'][r]['crib']['Bill'][1][1: ]),
                        'Cards_In_"You"_Hand_FirstCard_Suit': str(config['rounds'][r]['peggingHands']['You'][0][0:1]), 
                        'Cards_In_"You"_Hand_FirstCard_Number': str(config['rounds'][r]['peggingHands']['You'][0][1: ]), 
                        'Cards_In_"You"_Hand_SecondCard_Suit': str(config['rounds'][r]['peggingHands']['You'][1][0:1]),  
                        'Cards_In_"You"_Hand_SecondCard_Number': str(config['rounds'][r]['peggingHands']['You'][1][1: ]),
                        'Cards_In_"You"_Hand_ThirdCard_Suit': str(config['rounds'][r]['peggingHands']['You'][2][0:1]),  
                        'Cards_In_"You"_Hand_ThirdCard_Number': str(config['rounds'][r]['peggingHands']['You'][2][1: ]),
                        'Cards_In_"You"_Hand_FourthCard_Suit': str(config['rounds'][r]['peggingHands']['You'][3][0:1]),  
                        'Cards_In_"You"_Hand_FourthCard_Number': str(config['rounds'][r]['peggingHands']['You'][3][1: ]),
                        'Cards_In_"Bill"_Hand_FirstCard_Suit': str(config['rounds'][r]['peggingHands']['Bill'][0][0:1]), 
                        'Cards_In_"Bill"_Hand_FirstCard_Number': str(config['rounds'][r]['peggingHands']['Bill'][0][1: ]),
                        'Cards_In_"Bill"_Hand_SecondCard_Suit': str(config['rounds'][r]['peggingHands']['Bill'][1][0:1]), 
                        'Cards_In_"Bill"_Hand_SecondCard_Number': str(config['rounds'][r]['peggingHands']['Bill'][1][1: ]),
                        'Cards_In_"Bill"_Hand_ThirdCard_Suit': str(config['rounds'][r]['peggingHands']['Bill'][2][0:1]), 
                        'Cards_In_"Bill"_Hand_ThirdCard_Number': str(config['rounds'][r]['peggingHands']['Bill'][2][1: ]),
                        'Cards_In_"Bill"_Hand_FourthCard_Suit': str(config['rounds'][r]['peggingHands']['Bill'][3][0:1]), 
                        'Cards_In_"Bill"_Hand_FourthCard_Number': str(config['rounds'][r]['peggingHands']['Bill'][3][1: ]), 
                        'Pegging_Round': p,
                        'UpCard_Suit': str(config['rounds'][r]['pegging']['cutCard'][0:1]), 
                        'UpCard_Number': str(config['rounds'][r]['pegging']['cutCard'][1: ]),
                        'The_Type': str(config['rounds'][r]['pegging']['moves'][p]['type']),               
                        'Player': str(config['rounds'][r]['pegging']['moves'][p]['player']), 
                        'Card_Played': str(config['rounds'][r]['pegging']['moves'][p]['card']),
                        'Card_Played_Suit': str(Card_Played_Suit),
                        'Card_Played_Number': str(Card_Played_Number),
                        'Current_Board_Value': str(config['rounds'][r]['pegging']['moves'][p]['currentBoardValue']), 
                        'All_Cards_On_The_Active_Board': str(config['rounds'][r]['pegging']['moves'][p]['activeTableCards']), 
                        'All_Cards_Played': str(config['rounds'][r]['pegging']['moves'][p]['allTableCards']), 
                        'Pegging_Total_Score': str(config['rounds'][r]['pegging']['moves'][p]['playScore']),
                        'Pegging_Score_ID': str(peggingScore_ID), 
                        'Pegging_Score_Array': str(peggingScore_Array), 
                        'Pegging_Score_Sum': str(peggingScore_Sum),  
                        'Pegging_Score_Cards': str(peggingScore_Cards), 
                        'Scoring_"You"': "You", 
                        'Combinations_ID': str(You_handCombinations_ID), 
                        'Combinations_Score': str(You_handCombinations_Score), 
                        'Combinations_Cards': str(You_handCombinations_Cards), 
                        'Total_Score': str(config['rounds'][r]['scoring']['You']['hand']['totalScore']), 
                        'Crib': str(config['rounds'][r]['scoring']['You']['crib']), 
                        'Crib_Total_Score': You_Crib_totalScore, 
                        'Crib_Combinations': You_Crib_Combinations,
                        'Scoring_"Bill"': "Bill",  
                        'Combinations_ID': str(Bill_handCombinations_ID), 
                        'Combinations_Score': str(Bill_handCombinations_Score), 
                        'Combinations_Cards': str(Bill_handCombinations_Cards),  
                        'Total_Score': str(config['rounds'][r]['scoring']['Bill']['hand']['totalScore']), 
                        'Crib': str(config['rounds'][r]['scoring']['Bill']['crib']), 
                        'Crib_Total_Score': Bill_Crib_totalScore, 
                        'Crib_Combinations': Bill_Crib_Combinations})

#creates a multiLevelModel over AllGames.csv
def multiLevelModeling():    
    data = pd.read_csv("AllGames.csv")
    smallerDataSet = data.iloc[:,[0,1,70,77]] #0 = Game, 1 = Hand_Round, 70 = Card_Played_Number, 77 = Pegging_Score_Sum
    smallerDataSet = smallerDataSet.replace('Z', np.NaN) #in the smallerDataSet it replaces all the Z to NAN
    smallerDataSet.dropna(inplace=True)

    #FIGURE OUT HOW TO WRITE SMALLERDATASET INTO A CSV FILE
    #smallerDataSet.to_csv('SmallerDataSet.csv', encoding = 'utf-8', index = False) #This writes the smallerDataSet into a csv file

    #data = data.replace('Z', '  ')
    #model = sm.MixedLM.from_formula("Hand_Round ~ Pegging_Round", data, groups=data["Game"]) #20 seconds
    #model = sm.MixedLM.from_formula("Pegging_Round ~ Hand_Round", data, groups=data["Game"]) #230 seconds
    #model = sm.MixedLM.from_formula("Pegging_Round ~ Pegging_Score_Score", data, groups=data["Hand_Round"]) #135 seconds
    #model = sm.MixedLM.from_formula("Pegging_Score ~ Pegging_Round", data, groups=data["Hand_Round"]) #100 seconds

    model = sm.MixedLM.from_formula("Pegging_Score_Sum ~ Card_Played_Number", smallerDataSet, groups = smallerDataSet["Hand_Round"])
    result = model.fit()
    print(result.summary())

    #HISTOGRAM STUFF
    cribDataSet = data.iloc[:,[0,1,77,83,84,85,91,92]]
    cribDataSet.to_csv('cribDataSet.csv', encoding = 'utf-8', index = True) #This writes the smallerDataSet into a csv file
    """
    gaussian_numbers = 0
    gaussian_numbers = numpy.count_nonzero()
    plt.hist(gaussian_numbers)
    plt.title("Cribbage Histogram")
    plt.xlabel("Card's Thrown to the Crib")
    plt.ylabel("Frequency")

    fig = plt.gcf()

    plot_url = py.plot_mpl(fig, filename='AllGamesFormatted.csv')
    """

#analyzes the points gathered determining whether it is your or bill's crib.
def cribAnalysis():  
    data = pd.read_csv("cribAnalysis.csv")
    smallerDataSet = data.iloc[:8866,[12,13,14,15,16,17,18,19,20,22]]  
    with open('twoCardsIntoCrib.csv', 'w') as csvFile:
        fieldnames = ['Card', 'SameSuit', 'CribScore']
        for i in range (1, 92):
            fieldnames.append('x' + str(i))
        writer = csv.DictWriter(csvFile, fieldnames = fieldnames, lineterminator = '\n')
        writer.writeheader()
        for i in range (0,8866): #8866
            dealer = smallerDataSet.iloc[i]['Who Dealt']
            #we don't want to throw cards into bill's yet. only checking to see my own crib
            #while (str(dealer) != 'Bill' and i < 8865):
                #i = i + 1
                #dealer = smallerDataSet.iloc[i]['Who Dealt']
                #print(i)
            firstCard = int(smallerDataSet.iloc[i]['Card'])
            firstCardSuit = str(smallerDataSet.iloc[i]['Suit.4'])
            secondCard = int(smallerDataSet.iloc[i]['Card.1'])
            secondCardSuit = str(smallerDataSet.iloc[i]['Suit.5'])
            thirdCard = int(smallerDataSet.iloc[i]['Card.2'])
            thirdCardSuit = str(smallerDataSet.iloc[i]['Suit.6'])
            fourthCard = int(smallerDataSet.iloc[i]['Card.3'])
            fourthCardSuit = str(smallerDataSet.iloc[i]['Suit.7'])
            upCard = int(smallerDataSet.iloc[i]['UpCard'])
            hand = [firstCard,secondCard,thirdCard,fourthCard,upCard]
            cribScore = getPoints(hand)
            d = {}
            #if (str(dealer != 'You')):                
                #to check what cards to throw into your crib, make it firstcard and second card.
                #"""
            for n in range (1, 14):
                if (str(dealer) == 'You'): #checks to see if the dealer is You
                    if (str(firstCard) == str(n)): #checks to see if the firstCard is the same as the number "n"
                        for m in range (1, 14): #loops through 13 numbers
                            if (str(secondCard) == str(m)): #checks to see if the secondCard is the same as the number "m"
                                cards = str(firstCard) + ', ' + str(secondCard)
                                isSameSuit = 0
                                if (firstCardSuit == secondCardSuit):
                                    isSameSuit = 1
                                d = {'Card': cards,'CribScore': cribScore, 'SameSuit': isSameSuit}
                                for index in range(1,92):
                                    if (n == 1): #x1 - x13
                                        if (n*m == index):
                                            d1 = {'x'+ str(index): 1}
                                        else:
                                            d1 = {'x'+ str(index): 0}
                                    elif (n == 2): #x14 - x25
                                        if (m + 12 == index and m >= 2):
                                            d1 = {'x'+ str(index): 1}
                                        else:
                                            d1 = {'x'+ str(index): 0}
                                    elif (n == 3): #x26 - x36
                                        if (m + 23 == index and m >= 3):
                                            d1 = {'x'+ str(index): 1}
                                        else:
                                            d1 = {'x'+ str(index): 0}
                                    elif (n == 4): #x37 - x46
                                        if (m + 33 == index and m >= 4):
                                            d1 = {'x'+ str(index): 1}
                                        else:
                                            d1 = {'x'+ str(index): 0}
                                    elif (n == 5): #x47 - x55
                                        if (m + 42 == index and m >= 5):
                                            d1 = {'x'+ str(index): 1}
                                        else:
                                            d1 = {'x'+ str(index): 0}
                                    elif (n == 6): #x56 - x63
                                        if (m + 50 == index and m >= 6):
                                            d1 = {'x'+ str(index): 1}
                                        else:
                                            d1 = {'x'+ str(index): 0}
                                    elif (n == 7): #x64 - x70
                                        if (m + 57 == index and m >= 7):
                                            d1 = {'x'+ str(index): 1}
                                        else:
                                            d1 = {'x'+ str(index): 0}
                                    elif (n == 8): #x71 - x76
                                        if (m + 63 == index and m >= 8):
                                            d1 = {'x'+ str(index): 1}
                                        else:
                                            d1 = {'x'+ str(index): 0}
                                    elif (n == 9): #x77 - x81
                                        if (m + 68 == index and m >= 9):
                                            d1 = {'x'+ str(index): 1}
                                        else:
                                            d1 = {'x'+ str(index): 0}
                                    elif (n == 10): #x82 - x85
                                        if (m + 72 == index and m >= 10):
                                            d1 = {'x'+ str(index): 1}
                                        else:
                                            d1 = {'x'+ str(index): 0}
                                    elif (n == 11): #x86 - x88
                                        if (m + 75 == index and m >= 11):
                                            d1 = {'x'+ str(index): 1}
                                        else:
                                            d1 = {'x'+ str(index): 0}
                                    elif (n == 12): #x89 - x90
                                        if (m + 77 == index and m >= 12):
                                            d1 = {'x'+ str(index): 1}
                                        else:
                                            d1 = {'x'+ str(index): 0}
                                    elif (n == 13): #x91
                                        if (m + 78 == index and m == 13):
                                            d1 = {'x'+ str(index): 1}
                                        else:
                                            d1 = {'x'+ str(index): 0}
                                    
                                    d.update(d1)
                                m = 15
                                n = 15
            #"""
            #to check what cards to throw into "Bill" crib, make it firstCard and second card of "Bill"
            """
            for n in range (1, 14):
                if (str(dealer) == 'Bill'): #checks to see if the dealer is Bill
                    if (str(firstCard) == str(n)): #checks to see if the firstCard is the same as the number "n"
                        for m in range (1, 14): #loops through 13 numbers
                            if (str(secondCard) == str(m)): #checks to see if the secondCard is the same as the number "m"
                                cards = str(firstCard) + ', ' + str(secondCard)
                                isSameSuit = 0
                                if (firstCardSuit == secondCardSuit):
                                    isSameSuit = 1
                                d = {'Card': cards,'CribScore': cribScore, 'SameSuit': isSameSuit}
                                for index in range(1,92):
                                    if (n == 1): #x1 - x13
                                        if (n*m == index):
                                            d1 = {'x'+ str(index): 1}
                                        else:
                                            d1 = {'x'+ str(index): 0}
                                    elif (n == 2): #x14 - x25
                                        if (m + 12 == index and m >= 2):
                                            d1 = {'x'+ str(index): 1}
                                        else:
                                            d1 = {'x'+ str(index): 0}
                                    elif (n == 3): #x26 - x36
                                        if (m + 23 == index and m >= 3):
                                            d1 = {'x'+ str(index): 1}
                                        else:
                                            d1 = {'x'+ str(index): 0}
                                    elif (n == 4): #x37 - x46
                                        if (m + 33 == index and m >= 4):
                                            d1 = {'x'+ str(index): 1}
                                        else:
                                            d1 = {'x'+ str(index): 0}
                                    elif (n == 5): #x47 - x55
                                        if (m + 42 == index and m >= 5):
                                            d1 = {'x'+ str(index): 1}
                                        else:
                                            d1 = {'x'+ str(index): 0}
                                    elif (n == 6): #x56 - x63
                                        if (m + 50 == index and m >= 6):
                                            d1 = {'x'+ str(index): 1}
                                        else:
                                            d1 = {'x'+ str(index): 0}
                                    elif (n == 7): #x64 - x70
                                        if (m + 57 == index and m >= 7):
                                            d1 = {'x'+ str(index): 1}
                                        else:
                                            d1 = {'x'+ str(index): 0}
                                    elif (n == 8): #x71 - x76
                                        if (m + 63 == index and m >= 8):
                                            d1 = {'x'+ str(index): 1}
                                        else:
                                            d1 = {'x'+ str(index): 0}
                                    elif (n == 9): #x77 - x81
                                        if (m + 68 == index and m >= 9):
                                            d1 = {'x'+ str(index): 1}
                                        else:
                                            d1 = {'x'+ str(index): 0}
                                    elif (n == 10): #x82 - x85
                                        if (m + 72 == index and m >= 10):
                                            d1 = {'x'+ str(index): 1}
                                        else:
                                            d1 = {'x'+ str(index): 0}
                                    elif (n == 11): #x86 - x88
                                        if (m + 75 == index and m >= 11):
                                            d1 = {'x'+ str(index): 1}
                                        else:
                                            d1 = {'x'+ str(index): 0}
                                    elif (n == 12): #x89 - x90
                                        if (m + 77 == index and m >= 12):
                                            d1 = {'x'+ str(index): 1}
                                        else:
                                            d1 = {'x'+ str(index): 0}
                                    elif (n == 13): #x91
                                        if (m + 78 == index and m == 13):
                                            d1 = {'x'+ str(index): 1}
                                        else:
                                            d1 = {'x'+ str(index): 0}
                                    
                                    d.update(d1)
                                m = 15
                                n = 15      
            """
            for n in range (1, 14):
                if (str(dealer) == 'Bill'): #checks to see if the dealer is Bill
                    if (str(firstCard) == str(n)): #checks to see if the firstCard is the same as the number "n"
                        for m in range (1, 14): #loops through 13 numbers
                            if (str(secondCard) == str(m)): #checks to see if the secondCard is the same as the number "m"
                                cards = str(firstCard) + ', ' + str(secondCard)
                                isSameSuit = 0
                                if (firstCardSuit == secondCardSuit):
                                    isSameSuit = 1
                                d = {'Card': cards,'CribScore': cribScore, 'SameSuit': isSameSuit}
                                for index in range(1,92):
                                    if (n == 1): #x1 - x13
                                        if (n*m == index):
                                            d1 = {'x'+ str(index): 1}
                                        else:
                                            d1 = {'x'+ str(index): 0}
                                    elif (n == 2): #x14 - x25
                                        if (m + 12 == index and m >= 2):
                                            d1 = {'x'+ str(index): 1}
                                        else:
                                            d1 = {'x'+ str(index): 0}
                                    elif (n == 3): #x26 - x36
                                        if (m + 23 == index and m >= 3):
                                            d1 = {'x'+ str(index): 1}
                                        else:
                                            d1 = {'x'+ str(index): 0}
                                    elif (n == 4): #x37 - x46
                                        if (m + 33 == index and m >= 4):
                                            d1 = {'x'+ str(index): 1}
                                        else:
                                            d1 = {'x'+ str(index): 0}
                                    elif (n == 5): #x47 - x55
                                        if (m + 42 == index and m >= 5):
                                            d1 = {'x'+ str(index): 1}
                                        else:
                                            d1 = {'x'+ str(index): 0}
                                    elif (n == 6): #x56 - x63
                                        if (m + 50 == index and m >= 6):
                                            d1 = {'x'+ str(index): 1}
                                        else:
                                            d1 = {'x'+ str(index): 0}
                                    elif (n == 7): #x64 - x70
                                        if (m + 57 == index and m >= 7):
                                            d1 = {'x'+ str(index): 1}
                                        else:
                                            d1 = {'x'+ str(index): 0}
                                    elif (n == 8): #x71 - x76
                                        if (m + 63 == index and m >= 8):
                                            d1 = {'x'+ str(index): 1}
                                        else:
                                            d1 = {'x'+ str(index): 0}
                                    elif (n == 9): #x77 - x81
                                        if (m + 68 == index and m >= 9):
                                            d1 = {'x'+ str(index): 1}
                                        else:
                                            d1 = {'x'+ str(index): 0}
                                    elif (n == 10): #x82 - x85
                                        if (m + 72 == index and m >= 10):
                                            d1 = {'x'+ str(index): 1}
                                        else:
                                            d1 = {'x'+ str(index): 0}
                                    elif (n == 11): #x86 - x88
                                        if (m + 75 == index and m >= 11):
                                            d1 = {'x'+ str(index): 1}
                                        else:
                                            d1 = {'x'+ str(index): 0}
                                    elif (n == 12): #x89 - x90
                                        if (m + 77 == index and m >= 12):
                                            d1 = {'x'+ str(index): 1}
                                        else:
                                            d1 = {'x'+ str(index): 0}
                                    elif (n == 13): #x91
                                        if (m + 78 == index and m == 13):
                                            d1 = {'x'+ str(index): 1}
                                        else:
                                            d1 = {'x'+ str(index): 0}
                                    
                                    d.update(d1)
                                m = 15
                                n = 15      
                
            if(len(d) != 0):
                writer.writerow(d)   
            results = []
        
        with open('twoCardsIntoCrib.csv', 'r') as csvFile:
            reader = csv.DictReader(csvFile)
            
            for row in reader:
                #print(row['Card'],row['SameSuit'], row['x1'], row['x2'], row['x3'], row['x4'], row['x5'], row['x6'], row['x7'], row['x8'], row['x9'], row['x10'], row['x11'] , row['x12'] , row['x13'], row['CribScore'])
                #print(row)
                results.append(row)
            x = []
            y = []
            for i in range(0,len(results)):
                observation = []
                observation.append(int(results[i]['SameSuit'])) 
                for j in range(1,92):
                    observation.append(int(results[i]['x' + str(j)]))   
                y.append(int(results[i]['CribScore']))
                x.append(observation)
            clf = linear_model.Lasso(alpha=0.001, fit_intercept= True, max_iter = 10000)
            clf.fit(x, y)
            print(clf.coef_)
            print(clf.intercept_)
         
#calculates the total of the Hand, Pegging, and Crib Score
def peggingScorePerCard(card):
    """
    Returns the peggign score of a given card.
        @date 3/22/2018
        @param card   the pegging score correlated with the card that was selected.
        @return points  returns the average amount of points gained when playing a certain card in pegging.
    """
    points = 1.189
    if (card == 1):
        points -= 0
    elif (card == 2):
        points -= 0.199
    elif (card == 3):
        points -= 0.436
    elif (card == 4):
        points -= 0.509
    elif (card == 5):
        points -= 0.093
    elif (card == 6):
        points -= 0.356
    elif (card == 7):
        points -= 0.583
    elif (card == 8):
        points -= 0.685
    elif (card == 9):
        points -= 0.663
    elif (card == 10):
        points -= 0.752
    elif (card == 11):
        points -= 0.765
    elif (card == 12):
        points -= 0.810
    elif (card == 13):
        points -= 0.866
    return points

def pickingAHand():
    """
    Picks a specific hand given a random deck and random 6 cards while taking account the Hand, Pegging, and Crib Score.
        @date 3/22/2018
        @return fourCardHandArray[maxPointsIndex]  returns the best 4 card hand given a 6 card hand.
    """
    theDeck = createNewDeck()
    sixCardHandWithSuit = drawAHand(theDeck)
    sixCardHand = sort(removeSuit(sixCardHandWithSuit))
    fourCardHandArray = list(itertools.combinations(sixCardHand, 4))
    twoCardCribArray = list(itertools.combinations(sixCardHand, 2))
    fourCardHandWithSuitArray = list(itertools.combinations(sixCardHandWithSuit, 4))
    print("Six Card Hand: ", sixCardHand)
    fourCardHandArrayPoints = [None] * 16
    maxPoints = 0
    maxPointsIndex = 0

    with open('2CardCribPoints.csv', 'r') as csvFile: 
        reader = csv.DictReader(csvFile)
        input_csv = []
        for row in reader:
            input_csv.append(row)

        for i in range (0,15):
            fourCardHand = list(fourCardHandArray[i])
            fourCardHandWithSuit = list(fourCardHandWithSuitArray[i])
            twoCardCrib = list(twoCardCribArray[14 - i])

            firstCardCrib = str(twoCardCrib[1])
            secondCardCrib = str(twoCardCrib[0])
            #print(firstCardCrib)
            #print(secondCardCrib)
            fourCardHandArrayPoints[i] = getPoints(fourCardHand) + probabilityPoints(fourCardHand, theDeck) + getPointsWithSuit(fourCardHandWithSuit)  + probabilityPointsWithSuit(fourCardHandWithSuit, theDeck)
            #this gets the points for the crib
            for row in input_csv:
                #print("First Card: ", row[firstCardCrib], " Second Card: ", row['4.543'], secondCardCrib)
                if(row[firstCardCrib] is not '' and row['4.543'] == secondCardCrib):
                    fourCardHandArrayPoints[i] += float(row[firstCardCrib])
                    #print("test2",i,fourCardHandArrayPoints[i])
            for j in range (0,4):
                fourCardHandArrayPoints[i] += float(peggingScorePerCard(fourCardHand[j]))
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
    #print(fourCardHandArray[maxPointsIndex])
    return(fourCardHandArray[maxPointsIndex]) 

def pickingAHandYourCrib(hand, deck):
    """
    Picks a specific hand given a certain deck, it's your crib, and a specific 6 cards while taking account the Hand, Pegging, and Crib Score.
        @date 3/22/2018
        @return fourCardHandArray[maxPointsIndex]  returns the best 4 card hand given a 6 card hand.
    """
    #theDeck = createNewDeck()
    #sixCardHandWithSuit = drawAHand(theDeck)
    theDeck = deck
    sixCardHandWithSuit = hand
    sixCardHand = sort(removeSuit(sixCardHandWithSuit))
    fourCardHandArray = list(itertools.combinations(sixCardHand, 4))
    twoCardCribArray = list(itertools.combinations(sixCardHand, 2))
    fourCardHandWithSuitArray = list(itertools.combinations(sixCardHandWithSuit, 4))
    print("Six Card Hand: ", sixCardHand)
    fourCardHandArrayPoints = [None] * 16
    maxPoints = 0
    maxPointsIndex = 0

    with open('2CardCribPoints.csv', 'r') as csvFile: 
        reader = csv.DictReader(csvFile)
        input_csv = []
        for row in reader:
            input_csv.append(row)

        for i in range (0,15):
            fourCardHand = list(fourCardHandArray[i])
            fourCardHandWithSuit = list(fourCardHandWithSuitArray[i])
            twoCardCrib = list(twoCardCribArray[14 - i])

            firstCardCrib = str(twoCardCrib[1])
            secondCardCrib = str(twoCardCrib[0])
            #print(firstCardCrib)
            #print(secondCardCrib)
            fourCardHandArrayPoints[i] = getPoints(fourCardHand) + probabilityPoints(fourCardHand, theDeck) + getPointsWithSuit(fourCardHandWithSuit)  + probabilityPointsWithSuit(fourCardHandWithSuit, theDeck)
            #this gets the points for the crib
            for row in input_csv:
                #print("First Card: ", row[firstCardCrib], " Second Card: ", row['4.543'], secondCardCrib)
                if(row[firstCardCrib] is not '' and row['4.543'] == secondCardCrib):
                    fourCardHandArrayPoints[i] += float(row[firstCardCrib])
                    #print("test2",i,fourCardHandArrayPoints[i])
            for j in range (0,4):
                fourCardHandArrayPoints[i] += float(peggingScorePerCard(fourCardHand[j]))
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
    #print(fourCardHandArray[maxPointsIndex])
    return(fourCardHandArray[maxPointsIndex])     

def pickingAHandOpponentsCrib(hand, deck):
    """
    Picks a specific hand given a certain deck, it's the Opponents crib, and a specific 6 cards while taking account the Hand, Pegging, and Crib Score.
        @date 3/22/2018
        @return fourCardHandArray[maxPointsIndex]  returns the best 4 card hand given a 6 card hand.
    """    
    #theDeck = createNewDeck()
    #sixCardHandWithSuit = drawAHand(theDeck)
    theDeck = deck
    sixCardHandWithSuit = hand
    sixCardHand = sort(removeSuit(sixCardHandWithSuit))
    fourCardHandArray = list(itertools.combinations(sixCardHand, 4))
    twoCardCribArray = list(itertools.combinations(sixCardHand, 2))
    fourCardHandWithSuitArray = list(itertools.combinations(sixCardHandWithSuit, 4))
    print("Six Card Hand: ", sixCardHand)
    fourCardHandArrayPoints = [None] * 16
    maxPoints = 0
    maxPointsIndex = 0

    with open('2CardCribPoints.csv', 'r') as csvFile: 
        reader = csv.DictReader(csvFile)
        input_csv = []
        for row in reader:
            input_csv.append(row)

        for i in range (0,15):
            fourCardHand = list(fourCardHandArray[i])
            fourCardHandWithSuit = list(fourCardHandWithSuitArray[i])
            twoCardCrib = list(twoCardCribArray[14 - i])

            firstCardCrib = str(twoCardCrib[1])
            secondCardCrib = str(twoCardCrib[0])
            #print(firstCardCrib)
            #print(secondCardCrib)
            fourCardHandArrayPoints[i] = getPoints(fourCardHand) + probabilityPoints(fourCardHand, theDeck) + getPointsWithSuit(fourCardHandWithSuit)  + probabilityPointsWithSuit(fourCardHandWithSuit, theDeck)
            #this gets the points for the crib
            for row in input_csv:
                #print("First Card: ", row[firstCardCrib], " Second Card: ", row['4.543'], secondCardCrib)
                if(row[firstCardCrib] is not '' and row['4.543'] == secondCardCrib):
                    fourCardHandArrayPoints[i] -= float(row[firstCardCrib])
                    #print("test2",i,fourCardHandArrayPoints[i])
            for j in range (0,4):
                fourCardHandArrayPoints[i] += float(peggingScorePerCard(fourCardHand[j]))
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
    #print(fourCardHandArray[maxPointsIndex])
    return(fourCardHandArray[maxPointsIndex])

#creates initial pegging excel sheet
def creatingInitialPeggingDataFile():
    data = pd.read_csv("AllGames.csv")
    smallerDataSet = data.iloc[:83259,[0,1,2,48,50,52,54,56,58,60,62,63,66,67,70,71,72,73,74,75,76,77,78]] 
    #print(smallerDataSet) 
    
    with open('initialPeggingData.csv', 'w') as csvFile:
        fieldnames = ['Game', 'Hand_Round', 'Dealer',
                        'YouFirstCard', 'YouSecondCard', 'YouThirdCard', 'YouFourthCard',
                        'BillFirstCard', 'BillSecondCard', 'BillThirdCard', 'BillFourthCard',
                        'PeggingRound', 'TheType', 'Player', 'CardPlayed',
                        'CurrentBoardValue', 'AllCardsOnTheActiveBoard',
                        'AllCardsPlayed', 'PeggingTotalScore',
                        'PeggingScoreID', 'PeggingScoreArray', 'PeggingScoreSum', 'PeggingScoreCards']
        writer = csv.DictWriter(csvFile, fieldnames = fieldnames, lineterminator = '\n')
        writer.writeheader()

        #for i in range (83258):
        for i in range (13,23): #testing purposes
            game = smallerDataSet.iloc[i]['Game']
            hand_Round = smallerDataSet.iloc[i]['Hand_Round']
            dealer = smallerDataSet.iloc[i]['Dealer']
            youFirstCard = smallerDataSet.iloc[i]['Cards_In_"You"_Hand_FirstCard_Number']
            youSecondCard = smallerDataSet.iloc[i]['Cards_In_"You"_Hand_SecondCard_Number']
            youThirdCard = smallerDataSet.iloc[i]['Cards_In_"You"_Hand_ThirdCard_Number']
            youFourthCard = smallerDataSet.iloc[i]['Cards_In_"You"_Hand_FourthCard_Number']
            billFirstCard = smallerDataSet.iloc[i]['Cards_In_"Bill"_Hand_FirstCard_Number']
            billSecondCard = smallerDataSet.iloc[i]['Cards_In_"Bill"_Hand_SecondCard_Number']
            billThirdCard = smallerDataSet.iloc[i]['Cards_In_"Bill"_Hand_ThirdCard_Number']
            billFourthCard = smallerDataSet.iloc[i]['Cards_In_"Bill"_Hand_FourthCard_Number']
            peggingRound = smallerDataSet.iloc[i]['Pegging_Round']
            theType = smallerDataSet.iloc[i]['The_Type']
            player = smallerDataSet.iloc[i]['Player']
            cardPlayed = smallerDataSet.iloc[i]['Card_Played_Number']
            if (cardPlayed == 'Z'):
                cardPlayed = 0
            currentBoardValue = smallerDataSet.iloc[i]['Current_Board_Value']
            allCardsOnTheActiveBoard = smallerDataSet.iloc[i]['All_Cards_On_The_Active_Board']
            allCardsPlayed = smallerDataSet.iloc[i]['All_Cards_Played']
            peggingTotalScore = smallerDataSet.iloc[i]['Pegging_Total_Score']
            peggingScoreID = smallerDataSet.iloc[i]['Pegging_Score_ID']
            peggingScoreArray = smallerDataSet.iloc[i]['Pegging_Score_Array']
            peggingScoreSum = smallerDataSet.iloc[i]['Pegging_Score_Sum']
            peggingScoreCards = smallerDataSet.iloc[i]['Pegging_Score_Cards']

            writer.writerow({'Game': game, 'Hand_Round': hand_Round, 'Dealer': dealer,
                        'YouFirstCard': youFirstCard, 'YouSecondCard': youSecondCard, 'YouThirdCard': youThirdCard, 'YouFourthCard': youFourthCard,
                        'BillFirstCard': billFirstCard, 'BillSecondCard': billSecondCard, 'BillThirdCard': billThirdCard, 'BillFourthCard': billFourthCard,
                        'PeggingRound': peggingRound, 'TheType': theType, 'Player': player, 'CardPlayed': cardPlayed,
                        'CurrentBoardValue': currentBoardValue, 'AllCardsOnTheActiveBoard': allCardsOnTheActiveBoard,
                        'AllCardsPlayed': allCardsPlayed, 'PeggingTotalScore': peggingTotalScore, 'PeggingScoreID': peggingScoreID, 
                        'PeggingScoreArray': peggingScoreArray, 'PeggingScoreSum': peggingScoreSum, 'PeggingScoreCards': peggingScoreCards})
    
    return True

#creates a more indepth pegging excel sheet that uses the initial pegging excel sheet
def creatingPeggingFile():
    #with open('peggingAnalysis.csv', 'r') as csvFile:
    df = pd.read_csv('peggingAnalysis.csv')
    
    with open('peggingAnalysis3.csv', 'w') as csvFile:
        fieldnames = ['Game', 'Hand_Round', 'Dealer',
                            'YouFirstCard', 'YouSecondCard', 'YouThirdCard', 'YouFourthCard',
                            'BillFirstCard', 'BillSecondCard', 'BillThirdCard', 'BillFourthCard',
                            'PeggingRound', 'TheType', 'Player', 'CardPlayed',
                            'CurrentBoardValue', 
                            'AllCardsOnTheActiveBoard_1', 'AllCardsOnTheActiveBoard_2', 'AllCardsOnTheActiveBoard_3', 'AllCardsOnTheActiveBoard_4',
                            'AllCardsOnTheActiveBoard_5', 'AllCardsOnTheActiveBoard_6', 'AllCardsOnTheActiveBoard_7', 'AllCardsOnTheActiveBoard_8',
                            'ThreeCardRun', 'FourCardRun', 'FiveCardRun', 'SixCardRun', 'SevenCardRun', 
                            'Pair','Triple','Quad', 'Fifteen', 'ThirtyOne', 'LastCard',
                            'AllCardsPlayed_1', 'AllCardsPlayed_2', 'AllCardsPlayed_3', 'AllCardsPlayed_4',
                            'AllCardsPlayed_5', 'AllCardsPlayed_6', 'AllCardsPlayed_7', 'AllCardsPlayed_8',
                            'PeggingTotalScore',
                            'PeggingScoreID_1', 'PeggingScoreArray_1', 'PeggingScoreCards_1',
                            'PeggingScoreID_2', 'PeggingScoreArray_2', 'PeggingScoreCards_2',
                            'PeggingScoreID_3', 'PeggingScoreArray_3', 'PeggingScoreCards_3', 
                            'PeggingScoreSum']
        writer = csv.DictWriter(csvFile, fieldnames = fieldnames, lineterminator = '\n')
        writer.writeheader()
        replacementCharacters = "['] "
        suitCharacters = "SDCH"
        array = []
        allCardsOnTheActiveBoard = [] #1-8 cards
        allCardsPlayed = [] #1-8 cards
        peggingScoreID = [] #1-3 cards
        peggingScoreArray = [] #1-3 cards
        peggingScoreCards = [] #1-3 cards
        for i in range (83258): #column #83258
            game = df.iloc[i]['Game']
            hand_Round = df.iloc[i]['Hand_Round']
            dealer = df.iloc[i]['Dealer']
            youFirstCard = df.iloc[i]['YouFirstCard']
            youSecondCard = df.iloc[i]['YouSecondCard']
            youThirdCard = df.iloc[i]['YouThirdCard']
            youFourthCard = df.iloc[i]['YouFourthCard']
            billFirstCard = df.iloc[i]['BillFirstCard']
            billSecondCard = df.iloc[i]['BillSecondCard']
            billThirdCard = df.iloc[i]['BillThirdCard']
            billFourthCard = df.iloc[i]['BillFourthCard']
            peggingRound = df.iloc[i]['PeggingRound']
            theType = df.iloc[i]['TheType']
            player = df.iloc[i]['Player']
            cardPlayed = df.iloc[i]['CardPlayed']
            if (cardPlayed == 'Z'):
                cardPlayed = 0
            currentBoardValue = df.iloc[i]['CurrentBoardValue']
            peggingTotalScore = df.iloc[i]['PeggingTotalScore']
            peggingScoreSum = df.iloc[i]['PeggingScoreSum']
        #fixes the arrays for 16,17,19,20,21
            allCardsOnTheActiveBoardString = str(df.iloc[i, 16])
            allCardsPlayedString = str(df.iloc[i, 17])
            peggingScoreIDString = str(df.iloc[i, 19])
            peggingScoreArrayString = str(df.iloc[i, 20])
            peggingScoreCardsString = str(df.iloc[i, 21])
            for char in replacementCharacters:
                allCardsOnTheActiveBoardString = allCardsOnTheActiveBoardString.replace(char,"")
                allCardsPlayedString = allCardsPlayedString.replace(char,"")
                peggingScoreIDString = peggingScoreIDString.replace(char,"")
                peggingScoreArrayString = peggingScoreArrayString.replace(char,"")
                peggingScoreCardsString = peggingScoreCardsString.replace(char,"")
            for char in suitCharacters:
                allCardsOnTheActiveBoardString = allCardsOnTheActiveBoardString.replace(char,"")
                allCardsPlayedString = allCardsPlayedString.replace(char,"")
            allCardsOnTheActiveBoard = allCardsOnTheActiveBoardString.split(',')
            allCardsPlayed = allCardsPlayedString.split(',')
            peggingScoreID = peggingScoreIDString.split(',')
            peggingScoreArray = peggingScoreArrayString.split(',')
            peggingScoreCards = peggingScoreCardsString.split(',')
        #for threeCardRun, fourCardRun, and fiveCardRun. Also for Pair, Triple, Quad, Fifteen, ThirtyOne, LastCard
            numberOfCards = len(allCardsOnTheActiveBoard)
            smallerHand = []
            threeCardRun = fourCardRun = fiveCardRun = sixCardRun = sevenCardRun = 0
            pair = triple = quad = fifteen = thirtyOne = lastCard = 0
            if (i <= 83256):
                sayGo = df.iloc[i+1]['TheType']
                if (sayGo == 'saygo'):
                    lastCard = 1
            if (numberOfCards >= 2):
                firstCard = int(allCardsOnTheActiveBoard[numberOfCards-1])
                secondCard = int(allCardsOnTheActiveBoard[numberOfCards-2])
                if (firstCard == secondCard):
                    pair = 1
                    triple = 0
                    quad = 0
                if (currentBoardValue == 15):
                    fifteen = 1
            if (numberOfCards >= 3):
                thirdCard = int(allCardsOnTheActiveBoard[numberOfCards-3])
                smallerHand.append(firstCard)
                smallerHand.append(secondCard)
                smallerHand.append(thirdCard)
                smallHandCards = len(smallerHand)
                smallerHand.sort(reverse = True)
                if (smallerHand[smallHandCards-1] + 2 == smallerHand[smallHandCards-2] + 1 and smallerHand[smallHandCards-2] + 1 == smallerHand[smallHandCards-3]):
                    threeCardRun = 1
                if (firstCard == secondCard and secondCard == thirdCard):
                    pair = 1
                    triple = 1
                    quad = 0
                if (currentBoardValue == 15):
                    fifteen = 1
            if (numberOfCards >= 4):
                fourthCard = int(allCardsOnTheActiveBoard[numberOfCards-4])
                smallerHand.append(fourthCard)
                smallHandCards = len(smallerHand)
                smallerHand.sort(reverse = True)
                if (smallerHand[smallHandCards-1] + 3 == smallerHand[smallHandCards-2] + 2 and smallerHand[smallHandCards-2] + 2 == smallerHand[smallHandCards-3] + 1 and smallerHand[smallHandCards-3] + 1 == smallerHand[smallHandCards-4]):
                    threeCardRun = fiveCardRun = sixCardRun = sevenCardRun = 0
                    fourCardRun = 1
                if (firstCard == secondCard and secondCard == thirdCard and thirdCard == fourthCard):
                    pair = 1
                    triple = 1
                    quad = 1
                if (currentBoardValue == 15):
                    fifteen = 1
                elif (currentBoardValue == 31):
                    thirtyOne = 1
            if (numberOfCards >= 5):
                fifthCard = int(allCardsOnTheActiveBoard[numberOfCards-5])
                smallerHand.append(fifthCard)
                smallHandCards = len(smallerHand)
                smallerHand.sort(reverse = True)
                if (smallerHand[smallHandCards-1] + 4 == smallerHand[smallHandCards-2] + 3 and smallerHand[smallHandCards-2] + 3 == smallerHand[smallHandCards-3] + 2 and smallerHand[smallHandCards-3] + 2 == smallerHand[smallHandCards-4] + 1 and smallerHand[smallHandCards-4] + 1 == smallerHand[smallHandCards-5]):
                    threeCardRun = fourCardRun = sixCardRun = sevenCardRun = 0
                    fiveCardRun = 1
                if (currentBoardValue == 15):
                    fifteen = 1
                elif (currentBoardValue == 31):
                    thirtyOne = 1
            if (numberOfCards >= 6):
                sixthCard = int(allCardsOnTheActiveBoard[numberOfCards-6])
                smallerHand.append(sixthCard)
                smallHandCards = len(smallerHand)
                smallerHand.sort(reverse = True)
                if (smallerHand[smallHandCards-1] + 5 == smallerHand[smallHandCards-2] + 4 and smallerHand[smallHandCards-2] + 4 == smallerHand[smallHandCards-3] + 3 and smallerHand[smallHandCards-3] + 3 == smallerHand[smallHandCards-4] + 2 and smallerHand[smallHandCards-4] + 2 == smallerHand[smallHandCards-5] + 1 and smallerHand[smallHandCards-5] + 1 == smallerHand[smallHandCards-6]):
                    threeCardRun = fourCardRun = fiveCardRun = sevenCardRun = 0
                    sixCardRun = 1
                if (currentBoardValue == 15):
                    fifteen = 1
                elif (currentBoardValue == 31):
                    thirtyOne = 1
            if (numberOfCards >= 7):
                seventhCard = int(allCardsOnTheActiveBoard[numberOfCards-7])
                smallerHand.append(seventhCard)
                smallHandCards = len(smallerHand)
                smallerHand.sort(reverse = True)
                if (smallerHand[smallHandCards-1] + 6 == smallerHand[smallHandCards-2] + 5 and smallerHand[smallHandCards-2] + 5 == smallerHand[smallHandCards-3] + 4 and smallerHand[smallHandCards-3] + 4 == smallerHand[smallHandCards-4] + 3 and smallerHand[smallHandCards-4] + 3 == smallerHand[smallHandCards-5] + 2 and smallerHand[smallHandCards-5] + 2 == smallerHand[smallHandCards-6] + 1 and smallerHand[smallHandCards-6] + 1 == smallerHand[smallHandCards-7]):
                    threeCardRun = fourCardRun = fiveCardRun = sixCardRun = 0
                    sevenCardRun = 1
                if (currentBoardValue == 15):
                    fifteen = 1
                elif (currentBoardValue == 31):
                    thirtyOne = 1
            if (numberOfCards == 8):
                if (currentBoardValue == 15):
                    fifteen = 1
                elif (currentBoardValue == 31):
                    thirtyOne = 1

        #making the arrays the correct size
            while(len(allCardsOnTheActiveBoard) != 8):
                allCardsOnTheActiveBoard.append(" ")
            while(len(allCardsPlayed) != 8):
                allCardsPlayed.append(" ")
            while(len(peggingScoreID) != 3):
                peggingScoreID.append(" ")
            while(len(peggingScoreArray) != 3):
                peggingScoreArray.append(" ")
            while(len(peggingScoreCards) != 3):
                peggingScoreCards.append(" ")
                
        #writing the rows    
            writer.writerow({'Game': game, 'Hand_Round': hand_Round, 'Dealer': dealer,
                    'YouFirstCard': youFirstCard, 'YouSecondCard': youSecondCard, 'YouThirdCard': youThirdCard, 'YouFourthCard': youFourthCard,
                    'BillFirstCard': billFirstCard, 'BillSecondCard': billSecondCard, 'BillThirdCard':billThirdCard, 'BillFourthCard':billFourthCard,
                    'PeggingRound': peggingRound, 'TheType': theType, 'Player': player, 'CardPlayed': cardPlayed,
                    'CurrentBoardValue': currentBoardValue, 
                    'AllCardsOnTheActiveBoard_1': allCardsOnTheActiveBoard[0], 'AllCardsOnTheActiveBoard_2': allCardsOnTheActiveBoard[1], 
                    'AllCardsOnTheActiveBoard_3': allCardsOnTheActiveBoard[2], 'AllCardsOnTheActiveBoard_4': allCardsOnTheActiveBoard[3],
                    'AllCardsOnTheActiveBoard_5': allCardsOnTheActiveBoard[4], 'AllCardsOnTheActiveBoard_6': allCardsOnTheActiveBoard[5], 
                    'AllCardsOnTheActiveBoard_7': allCardsOnTheActiveBoard[6], 'AllCardsOnTheActiveBoard_8': allCardsOnTheActiveBoard[7],
                    'ThreeCardRun': threeCardRun, 'FourCardRun': fourCardRun, 'FiveCardRun': fiveCardRun, 'SixCardRun': sixCardRun, 'SevenCardRun': sevenCardRun,  
                    'Pair': pair, 'Triple': triple,'Quad': quad, 'Fifteen': fifteen, 'ThirtyOne': thirtyOne, 'LastCard': lastCard,
                    'AllCardsPlayed_1': allCardsPlayed[0], 'AllCardsPlayed_2': allCardsPlayed[1], 
                    'AllCardsPlayed_3': allCardsPlayed[2], 'AllCardsPlayed_4': allCardsPlayed[3],
                    'AllCardsPlayed_5': allCardsPlayed[4], 'AllCardsPlayed_6': allCardsPlayed[5], 
                    'AllCardsPlayed_7': allCardsPlayed[6], 'AllCardsPlayed_8': allCardsPlayed[7],
                    'PeggingTotalScore': peggingTotalScore,
                    'PeggingScoreID_1': peggingScoreID[0], 'PeggingScoreArray_1': peggingScoreArray[0], 'PeggingScoreCards_1': peggingScoreCards[0],
                    'PeggingScoreID_2': peggingScoreID[1], 'PeggingScoreArray_2': peggingScoreArray[1], 'PeggingScoreCards_2': peggingScoreCards[1],
                    'PeggingScoreID_3': peggingScoreID[2], 'PeggingScoreArray_3': peggingScoreArray[2], 'PeggingScoreCards_3': peggingScoreCards[2], 
                    'PeggingScoreSum': peggingScoreSum})

#analyzes the max min and avg for the pegging data
def analyze_Max_Min_Avg_PeggingFile():
    df = pd.read_csv('peggingAnalysis3.csv')
    youHandRoundArray = []
    billHandRoundArray = []
    you_Max_Dict = {}
    you_Min_Dict = {}
    bill_Max_Dict = {}
    bill_Min_Dict = {}
    index = 0 #83096
    
    for g in range (0,1001): #83258  #22 #1001 #Loops through all the games
        r = 0 #r resets per game.
        while (df.iloc[index]['Game'] == g): #Loops through all the data of a game. Should enter this loop for all games.
            youHandRoundArray = [] #The hand arrays should reset after every end of the round
            billHandRoundArray = []  #Thats why it gets initialized before the start of the next round 
            while (df.iloc[index]['Hand_Round'] == r): #Loops through all the rounds of a game. Should enter this loop for all the rounds per game.
                #Adds the corresponding "You" data into its array to then be analayzed.
                if (df.iloc[index]['Player'] == 'You'):
                    youHandRoundArray.append(df.iloc[index]['PeggingTotalScore'])
                #Adds the corresponding "Bill" data into its array to then be analayzed.
                elif (df.iloc[index]['Player'] == 'Bill'):
                    billHandRoundArray.append(df.iloc[index]['PeggingTotalScore'])
                index = index + 1 #after adding the data points, the index will be increased by one to go to the next round.
            you_max_value = max(youHandRoundArray)
            you_min_value = min(youHandRoundArray)
            bill_max_value = max(billHandRoundArray)
            bill_min_value = min(billHandRoundArray)
            you_Max_Dict[(g, r)] = you_max_value #You Max
            you_Min_Dict[(g, r)] = you_min_value #You Min
            bill_Max_Dict[(g, r)] = bill_max_value #Bill Max
            bill_Min_Dict[(g, r)] = bill_min_value #Bill Min
            r = r + 1 #Once the index is a different value of the round, increase r by one.
    #print("You_Max_Dict", you_Max_Dict)
    #print("Bill_Max_Dict", bill_Max_Dict)
    #print("You_Min_Dict", you_Min_Dict)
    #print("Bill_Min_Dict", bill_Min_Dict)
    you_Max_TotalSum = bill_Max_TotalSum = you_Min_TotalSum = bill_Min_TotalSum = 0
    you_Max_Counter = bill_Max_Counter = you_Min_Counter = bill_Min_Counter = 0
    you_Max_List = []
    bill_Max_List = []
    you_Min_List = []    
    bill_Min_List = []
    for k,v in you_Max_Dict.items():
        you_Max_List.append(v)
        you_Max_TotalSum = you_Max_TotalSum + v
        you_Max_Counter = you_Max_Counter + 1
    for k,v in bill_Max_Dict.items():
        bill_Max_List.append(v)
        bill_Max_TotalSum = bill_Max_TotalSum + v
        bill_Max_Counter = bill_Max_Counter + 1
    for k,v in you_Min_Dict.items():
        you_Min_List.append(v)
        you_Min_TotalSum = you_Min_TotalSum + v
        you_Min_Counter = you_Min_Counter + 1
    for k,v in bill_Min_Dict.items():
        bill_Min_List.append(v)
        bill_Min_TotalSum = bill_Min_TotalSum + v
        bill_Min_Counter = bill_Min_Counter + 1

    you_Max_Average = you_Max_TotalSum / you_Max_Counter
    bill_Max_Average = bill_Max_TotalSum / bill_Max_Counter
    print("You Max Value:", max(you_Max_List))
    print("Bill Max Value:", max(bill_Max_List))
    print("You Min Value:", min(you_Min_List))
    print("Bill Min Value:", min(bill_Min_List))
    print("You_Max_Average", you_Max_Average)
    print("Bill_Max_Average", bill_Max_Average)
    you_descrstats = statsmodels.stats.weightstats.DescrStatsW(you_Max_List)
    bill_descrstats = statsmodels.stats.weightstats.DescrStatsW(bill_Max_List)
    print(you_descrstats.tconfint_mean(alpha= 0.01))      
    print(bill_descrstats.tconfint_mean(alpha= 0.01))

    

    """
        if (df.iloc[i]['TheType'] == 'playcard' and df.iloc[i]['ThreeCardRun'] == 1):
            counts = counts + 1
        elif (df.iloc[i]['TheType'] == 'playcard' and df.iloc[i]['FourCardRun'] == 1):
            counts = counts + 1
        elif (df.iloc[i]['TheType'] == 'playcard' and df.iloc[i]['FiveCardRun'] == 1):
            counts = counts + 1
        elif (df.iloc[i]['TheType'] == 'playcard' and df.iloc[i]['SixCardRun'] == 1):
            counts = counts + 1
        elif (df.iloc[i]['TheType'] == 'playcard' and df.iloc[i]['SevenCardRun'] == 1):
            counts = counts + 1
        if (df.iloc[i]['TheType'] == 'playcard'):
            nobs = nobs + 1
        if (if (df.iloc[i]['TheType'] == 'playcard' and df.iloc[i]['ThreeCardRun'] == 1):
            counts = counts + 1)
    """
    #print(counts)
    #counts = 1818 threeCardRun
    #nobs = 70928
    #print(statsmodels.stats.proportion.proportion_confint(counts, nobs, alpha=0.01, method='normal'))
    """
    with open('peggingAnalysis3.csv', 'r') as csvFile:
        reader = csv.DictReader(csvFile)
        
        #statsmodels.stats.proportion.proportion_confint(count, nobs, alpha=0.05, method='normal')[source]¶
            #if the first card thrown is a 10, given your hand as a second player find the different expected values of all possible plays
            #for row in reader:
    """

#creats an excel sheet with dummy code to be used for the first play
def createDummyCodeForFirstPlay():
    df = pd.read_csv('peggingAnalysis3.csv')
    with open('dummyCodeForFirstPlay.csv', 'w') as csvFile:
        fieldnames = ['Participant', 'FirstCardPlayed']
        for i in range (1, 14):
            fieldnames.append('Card_' + str(i)) #adds Card_# to the field names.
        fieldnames.append('ScoreOnNextPlay') #gets the score that the second player gets after playing a card
        writer = csv.DictWriter(csvFile, fieldnames = fieldnames, lineterminator = '\n')
        writer.writeheader()

        for i in range (83258): #83258
            firstCardPlayed = int(df.iloc[i]['CardPlayed'])
            if (df.iloc[i]['CardPlayed'] == df.iloc[i]['AllCardsOnTheActiveBoard_1']):
                if (df.iloc[i]['AllCardsOnTheActiveBoard_2'] == " "):
                    d = {}
                    d = {'Participant': i,'FirstCardPlayed': firstCardPlayed}
                    for n in range (1,14):
                        if (firstCardPlayed == n):
                            d1 = {'Card_' + str(n): 1}
                        else:
                            d1 = {'Card_' + str(n): 0}
                        d.update(d1)
                    d2 = {'ScoreOnNextPlay': df.iloc[i+1]['PeggingScoreCards_1']}
                    d.update(d2)
                    if(len(d) != 0):
                        writer.writerow(d)   

def lassoOnDummyCodeForFirstPlay():
    with open('dummyCodeForFirstPlay.csv', 'r') as csvFile:
        reader = csv.DictReader(csvFile)
        results = []
        for row in reader:
            #print(row['Card'],row['SameSuit'], row['x1'], row['x2'], row['x3'], row['x4'], row['x5'], row['x6'], row['x7'], row['x8'], row['x9'], row['x10'], row['x11'] , row['x12'] , row['x13'], row['CribScore'])
            #print(row)
            results.append(row)
        x = []
        y = []
        for i in range(0,len(results)):
            observation = []
            for j in range(1,14):
                observation.append(int(results[i]['Card_' + str(j)]))   
            y.append(int(results[i]['ScoreOnNextPlay']))
            x.append(observation)
        clf = linear_model.Lasso(alpha=0.005, fit_intercept= True, max_iter = 2000,)
        clf.fit(x, y)
        print(clf.coef_)
        print(clf.intercept_)

        

#creatingInitialPeggingDataFile()
#analyze_Max_Min_Avg_PeggingFile()
#creatingPeggingFile()
#createDummyCodeForFirstPlay()
#lassoOnDummyCodeForFirstPlay() #use for first play

#cribAnalysis()
"""
board = []
hand = []
board.append(10)
board.append(10)
board.append(3)
hand.append(3)
hand.append(8)
"""
"""
for i in range (12):
    decisionOnNextCard(board,hand)
print(decisionOnNextCard(board,hand))
"""

"""
deck = createNewDeck()
deck.remove('S2')
deck.remove('S3')
deck.remove('D4')
deck.remove('H5')
deck.remove('S5')
deck.remove('S10')
handOne = ['S2','S3','D4','H5','S5','S10']
yourHand = handOne
opponentsHand = ['H2','S7','S8','S9','H10','D11']
#print("First Function",chooseHandWithSuit(handOne,deck)) #fix the print in this function
fourCardHand = list(pickingAHandYourCrib(handOne,deck))
print("FourCard Hand:",fourCardHand) 
#print("Third Function",pickingAHandOpponentsCrib(handOne,deck)) 
print("Card Played: ", fourCardHand.pop(decisionOnFirstCardNoSuit(fourCardHand)))
print("___________Last Step_____________")

oneHandCribbageSpecificHand(yourHand,opponentsHand)
"""
cribAnalysis()