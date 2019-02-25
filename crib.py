import json
import csv
import numpy as np
import pandas as pd
import statsmodels.api as sm
from pandas import read_csv
from cribbageGameFunctions import *
import matplotlib.pyplot as plt
import numpy
from sklearn import linear_model
from sklearn.preprocessing import MultiLabelBinarizer


data = pd.read_csv("cribAnalysis.csv")
smallerDataSet = data.iloc[:8866,[12,13,14,15,16,17,18,19,20,22]]
#print(smallerDataSet)

#smallerDataSet = smallerDataSet.replace('Z', np.NaN) #in the smallerDataSet it replaces all the Z to NAN
#smallerDataSet.dropna(inplace=True)
#print(smallerDataSet)
#print(smallerDataSet.iloc[8865:8866])
#card = smallerDataSet.iloc[:1, [0]]
#print(card)
#card = smallerDataSet.iloc[0]
#print(card)
#card = smallerDataSet.iloc[0]['Who Dealt']
#print(card)
#print(smallerDataSet.iloc[:1, [0]])
#print(smallerDataSet.iloc[:1, [1]])
#print(smallerDataSet.iloc[:1, [2]])
#print(smallerDataSet.iloc[:1, [3]])
#print(smallerDataSet.iloc[:1, [4]])
#print(smallerDataSet.iloc[:1, [5]])

#8866
"""
with open('oneCardIntoCrib.csv', 'w') as csvFile:
    fieldnames = ['Card', 
                    'x1', 'x2', 'x3', 'x4', 'x5', 'x6', 'x7', 'x8', 'x9', 'x10', 'x11', 'x12', 'x13',
                    'CribScore']
    writer = csv.DictWriter(csvFile, fieldnames = fieldnames, lineterminator = '\n')
    writer.writeheader()
    for i in range (0,8866):
        dealer = smallerDataSet.iloc[i]['Who Dealt']
        firstCard = int(smallerDataSet.iloc[i]['Card'])
        secondCard = int(smallerDataSet.iloc[i]['Card.1'])
        thirdCard = int(smallerDataSet.iloc[i]['Card.2'])
        fourthCard = int(smallerDataSet.iloc[i]['Card.3'])
        upCard = int(smallerDataSet.iloc[i]['UpCard'])
        hand = [firstCard,secondCard,thirdCard,fourthCard,upCard]
        cribScore = getPoints(hand)
        if (str(dealer) == 'You'):
        #writing the first card into the rows with the crib score
            if (str(firstCard) == '1'):
                writer.writerow({'Card': str(firstCard),'CribScore': cribScore,
                        'x1': 1, 'x2': 0, 'x3': 0, 'x4': 0, 'x5': 0, 'x6': 0, 'x7': 0, 'x8': 0, 'x9': 0, 'x10': 0, 'x11': 0, 'x12': 0, 'x13': 0})
            elif (str(firstCard) == '2'):
                writer.writerow({'Card': str(firstCard),'CribScore': cribScore,
                        'x1': 0, 'x2': 1, 'x3': 0, 'x4': 0, 'x5': 0, 'x6': 0, 'x7': 0, 'x8': 0, 'x9': 0, 'x10': 0, 'x11': 0, 'x12': 0, 'x13': 0})
            elif (str(firstCard) == '3'):
                writer.writerow({'Card': str(firstCard),'CribScore': cribScore,
                        'x1': 0, 'x2': 0, 'x3': 1, 'x4': 0, 'x5': 0, 'x6': 0, 'x7': 0, 'x8': 0, 'x9': 0, 'x10': 0, 'x11': 0, 'x12': 0, 'x13': 0})
            elif (str(firstCard) == '4'):
                writer.writerow({'Card': str(firstCard),'CribScore': cribScore,
                        'x1': 0, 'x2': 0, 'x3': 0, 'x4': 1, 'x5': 0, 'x6': 0, 'x7': 0, 'x8': 0, 'x9': 0, 'x10': 0, 'x11': 0, 'x12': 0, 'x13': 0})
            elif (str(firstCard) == '5'):
                writer.writerow({'Card': str(firstCard),'CribScore': cribScore,
                        'x1': 0, 'x2': 0, 'x3': 0, 'x4': 0, 'x5': 1, 'x6': 0, 'x7': 0, 'x8': 0, 'x9': 0, 'x10': 0, 'x11': 0, 'x12': 0, 'x13': 0})
            elif (str(firstCard) == '6'):
                writer.writerow({'Card': str(firstCard),'CribScore': cribScore,
                        'x1': 0, 'x2': 0, 'x3': 0, 'x4': 0, 'x5': 0, 'x6': 1, 'x7': 0, 'x8': 0, 'x9': 0, 'x10': 0, 'x11': 0, 'x12': 0, 'x13': 0})
            elif (str(firstCard) == '7'):
                writer.writerow({'Card': str(firstCard),'CribScore': cribScore,
                        'x1': 0, 'x2': 0, 'x3': 0, 'x4': 0, 'x5': 0, 'x6': 0, 'x7': 1, 'x8': 0, 'x9': 0, 'x10': 0, 'x11': 0, 'x12': 0, 'x13': 0})
            elif (str(firstCard) == '8'):
                writer.writerow({'Card': str(firstCard),'CribScore': cribScore,
                        'x1': 0, 'x2': 0, 'x3': 0, 'x4': 0, 'x5': 0, 'x6': 0, 'x7': 0, 'x8': 1, 'x9': 0, 'x10': 0, 'x11': 0, 'x12': 0, 'x13': 0})
            elif (str(firstCard) == '9'):
                writer.writerow({'Card': str(firstCard),'CribScore': cribScore,
                        'x1': 0, 'x2': 0, 'x3': 0, 'x4': 0, 'x5': 0, 'x6': 0, 'x7': 0, 'x8': 0, 'x9': 1, 'x10': 0, 'x11': 0, 'x12': 0, 'x13': 0})
            elif (str(firstCard) == '10'):
                writer.writerow({'Card': str(firstCard),'CribScore': cribScore,
                        'x1': 0, 'x2': 0, 'x3': 0, 'x4': 0, 'x5': 0, 'x6': 0, 'x7': 0, 'x8': 0, 'x9': 0, 'x10': 1, 'x11': 0, 'x12': 0, 'x13': 0})
            elif (str(firstCard) == '11'):
                writer.writerow({'Card': str(firstCard),'CribScore': cribScore,
                        'x1': 0, 'x2': 0, 'x3': 0, 'x4': 0, 'x5': 0, 'x6': 0, 'x7': 0, 'x8': 0, 'x9': 0, 'x10': 0, 'x11': 1, 'x12': 0, 'x13': 0})
            elif (str(firstCard) == '12'):
                writer.writerow({'Card': str(firstCard),'CribScore': cribScore,
                        'x1': 0, 'x2': 0, 'x3': 0, 'x4': 0, 'x5': 0, 'x6': 0, 'x7': 0, 'x8': 0, 'x9': 0, 'x10': 0, 'x11': 0, 'x12': 1, 'x13': 0})
            elif (str(firstCard) == '13'):
                writer.writerow({'Card': str(firstCard),'CribScore': cribScore,
                        'x1': 0, 'x2': 0, 'x3': 0, 'x4': 0, 'x5': 0, 'x6': 0, 'x7': 0, 'x8': 0, 'x9': 0, 'x10': 0, 'x11': 0, 'x12': 0, 'x13': 1})            
        #writing the second card into the rows with the same crib score
            if (str(secondCard) == '1'):
                writer.writerow({'Card': str(secondCard),'CribScore': cribScore,
                        'x1': 1, 'x2': 0, 'x3': 0, 'x4': 0, 'x5': 0, 'x6': 0, 'x7': 0, 'x8': 0, 'x9': 0, 'x10': 0, 'x11': 0, 'x12': 0, 'x13': 0})
            elif (str(secondCard) == '2'):
                writer.writerow({'Card': str(secondCard),'CribScore': cribScore,
                        'x1': 0, 'x2': 1, 'x3': 0, 'x4': 0, 'x5': 0, 'x6': 0, 'x7': 0, 'x8': 0, 'x9': 0, 'x10': 0, 'x11': 0, 'x12': 0, 'x13': 0})
            elif (str(secondCard) == '3'):
                writer.writerow({'Card': str(secondCard),'CribScore': cribScore,
                        'x1': 0, 'x2': 0, 'x3': 1, 'x4': 0, 'x5': 0, 'x6': 0, 'x7': 0, 'x8': 0, 'x9': 0, 'x10': 0, 'x11': 0, 'x12': 0, 'x13': 0})
            elif (str(secondCard) == '4'):
                writer.writerow({'Card': str(secondCard),'CribScore': cribScore,
                        'x1': 0, 'x2': 0, 'x3': 0, 'x4': 1, 'x5': 0, 'x6': 0, 'x7': 0, 'x8': 0, 'x9': 0, 'x10': 0, 'x11': 0, 'x12': 0, 'x13': 0})
            elif (str(secondCard) == '5'):
                writer.writerow({'Card': str(secondCard),'CribScore': cribScore,
                        'x1': 0, 'x2': 0, 'x3': 0, 'x4': 0, 'x5': 1, 'x6': 0, 'x7': 0, 'x8': 0, 'x9': 0, 'x10': 0, 'x11': 0, 'x12': 0, 'x13': 0})
            elif (str(secondCard) == '6'):
                writer.writerow({'Card': str(secondCard),'CribScore': cribScore,
                        'x1': 0, 'x2': 0, 'x3': 0, 'x4': 0, 'x5': 0, 'x6': 1, 'x7': 0, 'x8': 0, 'x9': 0, 'x10': 0, 'x11': 0, 'x12': 0, 'x13': 0})
            elif (str(secondCard) == '7'):
                writer.writerow({'Card': str(secondCard),'CribScore': cribScore,
                        'x1': 0, 'x2': 0, 'x3': 0, 'x4': 0, 'x5': 0, 'x6': 0, 'x7': 1, 'x8': 0, 'x9': 0, 'x10': 0, 'x11': 0, 'x12': 0, 'x13': 0})
            elif (str(secondCard) == '8'):
                writer.writerow({'Card': str(secondCard),'CribScore': cribScore,
                        'x1': 0, 'x2': 0, 'x3': 0, 'x4': 0, 'x5': 0, 'x6': 0, 'x7': 0, 'x8': 1, 'x9': 0, 'x10': 0, 'x11': 0, 'x12': 0, 'x13': 0})
            elif (str(secondCard) == '9'):
                writer.writerow({'Card': str(secondCard),'CribScore': cribScore,
                        'x1': 0, 'x2': 0, 'x3': 0, 'x4': 0, 'x5': 0, 'x6': 0, 'x7': 0, 'x8': 0, 'x9': 1, 'x10': 0, 'x11': 0, 'x12': 0, 'x13': 0})
            elif (str(secondCard) == '10'):
                writer.writerow({'Card': str(secondCard),'CribScore': cribScore,
                        'x1': 0, 'x2': 0, 'x3': 0, 'x4': 0, 'x5': 0, 'x6': 0, 'x7': 0, 'x8': 0, 'x9': 0, 'x10': 1, 'x11': 0, 'x12': 0, 'x13': 0})
            elif (str(secondCard) == '11'):
                writer.writerow({'Card': str(secondCard),'CribScore': cribScore,
                        'x1': 0, 'x2': 0, 'x3': 0, 'x4': 0, 'x5': 0, 'x6': 0, 'x7': 0, 'x8': 0, 'x9': 0, 'x10': 0, 'x11': 1, 'x12': 0, 'x13': 0})
            elif (str(secondCard) == '12'):
                writer.writerow({'Card': str(secondCard),'CribScore': cribScore,
                        'x1': 0, 'x2': 0, 'x3': 0, 'x4': 0, 'x5': 0, 'x6': 0, 'x7': 0, 'x8': 0, 'x9': 0, 'x10': 0, 'x11': 0, 'x12': 1, 'x13': 0})
            elif (str(secondCard) == '13'):
                writer.writerow({'Card': str(secondCard),'CribScore': cribScore,
                        'x1': 0, 'x2': 0, 'x3': 0, 'x4': 0, 'x5': 0, 'x6': 0, 'x7': 0, 'x8': 0, 'x9': 0, 'x10': 0, 'x11': 0, 'x12': 0, 'x13': 1})
        elif (str(dealer) == 'Bill'):
        #writing the third card into the rows with the crib score
            if (str(thirdCard) == '1'):
                writer.writerow({'Card': str(thirdCard),'CribScore': cribScore,
                        'x1': 1, 'x2': 0, 'x3': 0, 'x4': 0, 'x5': 0, 'x6': 0, 'x7': 0, 'x8': 0, 'x9': 0, 'x10': 0, 'x11': 0, 'x12': 0, 'x13': 0})
            elif (str(thirdCard) == '2'):
                writer.writerow({'Card': str(thirdCard),'CribScore': cribScore,
                        'x1': 0, 'x2': 1, 'x3': 0, 'x4': 0, 'x5': 0, 'x6': 0, 'x7': 0, 'x8': 0, 'x9': 0, 'x10': 0, 'x11': 0, 'x12': 0, 'x13': 0})
            elif (str(thirdCard) == '3'):
                writer.writerow({'Card': str(thirdCard),'CribScore': cribScore,
                        'x1': 0, 'x2': 0, 'x3': 1, 'x4': 0, 'x5': 0, 'x6': 0, 'x7': 0, 'x8': 0, 'x9': 0, 'x10': 0, 'x11': 0, 'x12': 0, 'x13': 0})
            elif (str(thirdCard) == '4'):
                writer.writerow({'Card': str(thirdCard),'CribScore': cribScore,
                        'x1': 0, 'x2': 0, 'x3': 0, 'x4': 1, 'x5': 0, 'x6': 0, 'x7': 0, 'x8': 0, 'x9': 0, 'x10': 0, 'x11': 0, 'x12': 0, 'x13': 0})
            elif (str(thirdCard) == '5'):
                writer.writerow({'Card': str(thirdCard),'CribScore': cribScore,
                        'x1': 0, 'x2': 0, 'x3': 0, 'x4': 0, 'x5': 1, 'x6': 0, 'x7': 0, 'x8': 0, 'x9': 0, 'x10': 0, 'x11': 0, 'x12': 0, 'x13': 0})
            elif (str(thirdCard) == '6'):
                writer.writerow({'Card': str(thirdCard),'CribScore': cribScore,
                        'x1': 0, 'x2': 0, 'x3': 0, 'x4': 0, 'x5': 0, 'x6': 1, 'x7': 0, 'x8': 0, 'x9': 0, 'x10': 0, 'x11': 0, 'x12': 0, 'x13': 0})
            elif (str(thirdCard) == '7'):
                writer.writerow({'Card': str(thirdCard),'CribScore': cribScore,
                        'x1': 0, 'x2': 0, 'x3': 0, 'x4': 0, 'x5': 0, 'x6': 0, 'x7': 1, 'x8': 0, 'x9': 0, 'x10': 0, 'x11': 0, 'x12': 0, 'x13': 0})
            elif (str(thirdCard) == '8'):
                writer.writerow({'Card': str(thirdCard),'CribScore': cribScore,
                        'x1': 0, 'x2': 0, 'x3': 0, 'x4': 0, 'x5': 0, 'x6': 0, 'x7': 0, 'x8': 1, 'x9': 0, 'x10': 0, 'x11': 0, 'x12': 0, 'x13': 0})
            elif (str(thirdCard) == '9'):
                writer.writerow({'Card': str(thirdCard),'CribScore': cribScore,
                        'x1': 0, 'x2': 0, 'x3': 0, 'x4': 0, 'x5': 0, 'x6': 0, 'x7': 0, 'x8': 0, 'x9': 1, 'x10': 0, 'x11': 0, 'x12': 0, 'x13': 0})
            elif (str(thirdCard) == '10'):
                writer.writerow({'Card': str(thirdCard),'CribScore': cribScore,
                        'x1': 0, 'x2': 0, 'x3': 0, 'x4': 0, 'x5': 0, 'x6': 0, 'x7': 0, 'x8': 0, 'x9': 0, 'x10': 1, 'x11': 0, 'x12': 0, 'x13': 0})
            elif (str(thirdCard) == '11'):
                writer.writerow({'Card': str(thirdCard),'CribScore': cribScore,
                        'x1': 0, 'x2': 0, 'x3': 0, 'x4': 0, 'x5': 0, 'x6': 0, 'x7': 0, 'x8': 0, 'x9': 0, 'x10': 0, 'x11': 1, 'x12': 0, 'x13': 0})
            elif (str(thirdCard) == '12'):
                writer.writerow({'Card': str(thirdCard),'CribScore': cribScore,
                        'x1': 0, 'x2': 0, 'x3': 0, 'x4': 0, 'x5': 0, 'x6': 0, 'x7': 0, 'x8': 0, 'x9': 0, 'x10': 0, 'x11': 0, 'x12': 1, 'x13': 0})
            elif (str(thirdCard) == '13'):
                writer.writerow({'Card': str(thirdCard),'CribScore': cribScore,
                        'x1': 0, 'x2': 0, 'x3': 0, 'x4': 0, 'x5': 0, 'x6': 0, 'x7': 0, 'x8': 0, 'x9': 0, 'x10': 0, 'x11': 0, 'x12': 0, 'x13': 1})            
        #writing the fourth card into the rows with the same crib score    
            if (str(fourthCard) == '1'):
                writer.writerow({'Card': str(fourthCard),'CribScore': cribScore,
                        'x1': 1, 'x2': 0, 'x3': 0, 'x4': 0, 'x5': 0, 'x6': 0, 'x7': 0, 'x8': 0, 'x9': 0, 'x10': 0, 'x11': 0, 'x12': 0, 'x13': 0})
            elif (str(fourthCard) == '2'):
                writer.writerow({'Card': str(fourthCard),'CribScore': cribScore,
                        'x1': 0, 'x2': 1, 'x3': 0, 'x4': 0, 'x5': 0, 'x6': 0, 'x7': 0, 'x8': 0, 'x9': 0, 'x10': 0, 'x11': 0, 'x12': 0, 'x13': 0})
            elif (str(fourthCard) == '3'):
                writer.writerow({'Card': str(fourthCard),'CribScore': cribScore,
                        'x1': 0, 'x2': 0, 'x3': 1, 'x4': 0, 'x5': 0, 'x6': 0, 'x7': 0, 'x8': 0, 'x9': 0, 'x10': 0, 'x11': 0, 'x12': 0, 'x13': 0})
            elif (str(fourthCard) == '4'):
                writer.writerow({'Card': str(fourthCard),'CribScore': cribScore,
                        'x1': 0, 'x2': 0, 'x3': 0, 'x4': 1, 'x5': 0, 'x6': 0, 'x7': 0, 'x8': 0, 'x9': 0, 'x10': 0, 'x11': 0, 'x12': 0, 'x13': 0})
            elif (str(fourthCard) == '5'):
                writer.writerow({'Card': str(fourthCard),'CribScore': cribScore,
                        'x1': 0, 'x2': 0, 'x3': 0, 'x4': 0, 'x5': 1, 'x6': 0, 'x7': 0, 'x8': 0, 'x9': 0, 'x10': 0, 'x11': 0, 'x12': 0, 'x13': 0})
            elif (str(fourthCard) == '6'):
                writer.writerow({'Card': str(fourthCard),'CribScore': cribScore,
                        'x1': 0, 'x2': 0, 'x3': 0, 'x4': 0, 'x5': 0, 'x6': 1, 'x7': 0, 'x8': 0, 'x9': 0, 'x10': 0, 'x11': 0, 'x12': 0, 'x13': 0})
            elif (str(fourthCard) == '7'):
                writer.writerow({'Card': str(fourthCard),'CribScore': cribScore,
                        'x1': 0, 'x2': 0, 'x3': 0, 'x4': 0, 'x5': 0, 'x6': 0, 'x7': 1, 'x8': 0, 'x9': 0, 'x10': 0, 'x11': 0, 'x12': 0, 'x13': 0})
            elif (str(fourthCard) == '8'):
                writer.writerow({'Card': str(fourthCard),'CribScore': cribScore,
                        'x1': 0, 'x2': 0, 'x3': 0, 'x4': 0, 'x5': 0, 'x6': 0, 'x7': 0, 'x8': 1, 'x9': 0, 'x10': 0, 'x11': 0, 'x12': 0, 'x13': 0})
            elif (str(fourthCard) == '9'):
                writer.writerow({'Card': str(fourthCard),'CribScore': cribScore,
                        'x1': 0, 'x2': 0, 'x3': 0, 'x4': 0, 'x5': 0, 'x6': 0, 'x7': 0, 'x8': 0, 'x9': 1, 'x10': 0, 'x11': 0, 'x12': 0, 'x13': 0})
            elif (str(fourthCard) == '10'):
                writer.writerow({'Card': str(fourthCard),'CribScore': cribScore,
                        'x1': 0, 'x2': 0, 'x3': 0, 'x4': 0, 'x5': 0, 'x6': 0, 'x7': 0, 'x8': 0, 'x9': 0, 'x10': 1, 'x11': 0, 'x12': 0, 'x13': 0})
            elif (str(fourthCard) == '11'):
                writer.writerow({'Card': str(fourthCard),'CribScore': cribScore,
                        'x1': 0, 'x2': 0, 'x3': 0, 'x4': 0, 'x5': 0, 'x6': 0, 'x7': 0, 'x8': 0, 'x9': 0, 'x10': 0, 'x11': 1, 'x12': 0, 'x13': 0})
            elif (str(fourthCard) == '12'):
                writer.writerow({'Card': str(fourthCard),'CribScore': cribScore,
                        'x1': 0, 'x2': 0, 'x3': 0, 'x4': 0, 'x5': 0, 'x6': 0, 'x7': 0, 'x8': 0, 'x9': 0, 'x10': 0, 'x11': 0, 'x12': 1, 'x13': 0})
            elif (str(fourthCard) == '13'):
                writer.writerow({'Card': str(fourthCard),'CribScore': cribScore,
                        'x1': 0, 'x2': 0, 'x3': 0, 'x4': 0, 'x5': 0, 'x6': 0, 'x7': 0, 'x8': 0, 'x9': 0, 'x10': 0, 'x11': 0, 'x12': 0, 'x13': 1})
"""

#"""
with open('twoCardsIntoCrib.csv', 'w') as csvFile:
    fieldnames = ['Card', 'SameSuit', 'CribScore']
    for i in range (1, 92):
        fieldnames.append('x' + str(i))
    writer = csv.DictWriter(csvFile, fieldnames = fieldnames, lineterminator = '\n')
    writer.writeheader()
    for i in range (0,8866):
        dealer = smallerDataSet.iloc[i]['Who Dealt']
        #we don't want to throw cards into bill's yet. only checking to see my own crib
        #while (str(dealer) != 'Bill' and i < 8866):
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
        #to check what cards to throw into your crib, make it firstcard and second card.
        """
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
        """
        #to check what cards to throw into "Bill" crib, make it firstCard and second card of "Bill"
        #"""
        for n in range (1, 14):
            if (str(dealer) == 'Bill'): #checks to see if the dealer is Bill
                if (str(thirdCard) == str(n)): #checks to see if the firstCard is the same as the number "n"
                    for m in range (1, 14): #loops through 13 numbers
                        if (str(fourthCard) == str(m)): #checks to see if the secondCard is the same as the number "m"
                            cards = str(thirdCard) + ', ' + str(fourthCard)
                            isSameSuit = 0
                            if (thirdCardSuit == fourthCardSuit):
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
        if(len(d) != 0):
            writer.writerow(d)       
#"""        
                           
"""
        if (str(dealer) == 'You'):
        #writing the first card into the rows with the crib score
            if (str(firstCard) == '1'):
                writer.writerow({'Card': str(firstCard),'CribScore': cribScore,
                        'x1': 1, 'x2': 0, 'x3': 0, 'x4': 0, 'x5': 0, 'x6': 0, 'x7': 0, 'x8': 0, 'x9': 0, 'x10': 0, 'x11': 0, 'x12': 0, 'x13': 0})
            elif (str(firstCard) == '2'):
                writer.writerow({'Card': str(firstCard),'CribScore': cribScore,
                        'x1': 0, 'x2': 1, 'x3': 0, 'x4': 0, 'x5': 0, 'x6': 0, 'x7': 0, 'x8': 0, 'x9': 0, 'x10': 0, 'x11': 0, 'x12': 0, 'x13': 0})
            elif (str(firstCard) == '3'):
                writer.writerow({'Card': str(firstCard),'CribScore': cribScore,
                        'x1': 0, 'x2': 0, 'x3': 1, 'x4': 0, 'x5': 0, 'x6': 0, 'x7': 0, 'x8': 0, 'x9': 0, 'x10': 0, 'x11': 0, 'x12': 0, 'x13': 0})
            elif (str(firstCard) == '4'):
                writer.writerow({'Card': str(firstCard),'CribScore': cribScore,
                        'x1': 0, 'x2': 0, 'x3': 0, 'x4': 1, 'x5': 0, 'x6': 0, 'x7': 0, 'x8': 0, 'x9': 0, 'x10': 0, 'x11': 0, 'x12': 0, 'x13': 0})
            elif (str(firstCard) == '5'):
                writer.writerow({'Card': str(firstCard),'CribScore': cribScore,
                        'x1': 0, 'x2': 0, 'x3': 0, 'x4': 0, 'x5': 1, 'x6': 0, 'x7': 0, 'x8': 0, 'x9': 0, 'x10': 0, 'x11': 0, 'x12': 0, 'x13': 0})
            elif (str(firstCard) == '6'):
                writer.writerow({'Card': str(firstCard),'CribScore': cribScore,
                        'x1': 0, 'x2': 0, 'x3': 0, 'x4': 0, 'x5': 0, 'x6': 1, 'x7': 0, 'x8': 0, 'x9': 0, 'x10': 0, 'x11': 0, 'x12': 0, 'x13': 0})
            elif (str(firstCard) == '7'):
                writer.writerow({'Card': str(firstCard),'CribScore': cribScore,
                        'x1': 0, 'x2': 0, 'x3': 0, 'x4': 0, 'x5': 0, 'x6': 0, 'x7': 1, 'x8': 0, 'x9': 0, 'x10': 0, 'x11': 0, 'x12': 0, 'x13': 0})
            elif (str(firstCard) == '8'):
                writer.writerow({'Card': str(firstCard),'CribScore': cribScore,
                        'x1': 0, 'x2': 0, 'x3': 0, 'x4': 0, 'x5': 0, 'x6': 0, 'x7': 0, 'x8': 1, 'x9': 0, 'x10': 0, 'x11': 0, 'x12': 0, 'x13': 0})
            elif (str(firstCard) == '9'):
                writer.writerow({'Card': str(firstCard),'CribScore': cribScore,
                        'x1': 0, 'x2': 0, 'x3': 0, 'x4': 0, 'x5': 0, 'x6': 0, 'x7': 0, 'x8': 0, 'x9': 1, 'x10': 0, 'x11': 0, 'x12': 0, 'x13': 0})
            elif (str(firstCard) == '10'):
                writer.writerow({'Card': str(firstCard),'CribScore': cribScore,
                        'x1': 0, 'x2': 0, 'x3': 0, 'x4': 0, 'x5': 0, 'x6': 0, 'x7': 0, 'x8': 0, 'x9': 0, 'x10': 1, 'x11': 0, 'x12': 0, 'x13': 0})
            elif (str(firstCard) == '11'):
                writer.writerow({'Card': str(firstCard),'CribScore': cribScore,
                        'x1': 0, 'x2': 0, 'x3': 0, 'x4': 0, 'x5': 0, 'x6': 0, 'x7': 0, 'x8': 0, 'x9': 0, 'x10': 0, 'x11': 1, 'x12': 0, 'x13': 0})
            elif (str(firstCard) == '12'):
                writer.writerow({'Card': str(firstCard),'CribScore': cribScore,
                        'x1': 0, 'x2': 0, 'x3': 0, 'x4': 0, 'x5': 0, 'x6': 0, 'x7': 0, 'x8': 0, 'x9': 0, 'x10': 0, 'x11': 0, 'x12': 1, 'x13': 0})
            elif (str(firstCard) == '13'):
                writer.writerow({'Card': str(firstCard),'CribScore': cribScore,
                        'x1': 0, 'x2': 0, 'x3': 0, 'x4': 0, 'x5': 0, 'x6': 0, 'x7': 0, 'x8': 0, 'x9': 0, 'x10': 0, 'x11': 0, 'x12': 0, 'x13': 1})            
        #writing the second card into the rows with the same crib score
            if (str(secondCard) == '1'):
                writer.writerow({'Card': str(secondCard),'CribScore': cribScore,
                        'x1': 1, 'x2': 0, 'x3': 0, 'x4': 0, 'x5': 0, 'x6': 0, 'x7': 0, 'x8': 0, 'x9': 0, 'x10': 0, 'x11': 0, 'x12': 0, 'x13': 0})
            elif (str(secondCard) == '2'):
                writer.writerow({'Card': str(secondCard),'CribScore': cribScore,
                        'x1': 0, 'x2': 1, 'x3': 0, 'x4': 0, 'x5': 0, 'x6': 0, 'x7': 0, 'x8': 0, 'x9': 0, 'x10': 0, 'x11': 0, 'x12': 0, 'x13': 0})
            elif (str(secondCard) == '3'):
                writer.writerow({'Card': str(secondCard),'CribScore': cribScore,
                        'x1': 0, 'x2': 0, 'x3': 1, 'x4': 0, 'x5': 0, 'x6': 0, 'x7': 0, 'x8': 0, 'x9': 0, 'x10': 0, 'x11': 0, 'x12': 0, 'x13': 0})
            elif (str(secondCard) == '4'):
                writer.writerow({'Card': str(secondCard),'CribScore': cribScore,
                        'x1': 0, 'x2': 0, 'x3': 0, 'x4': 1, 'x5': 0, 'x6': 0, 'x7': 0, 'x8': 0, 'x9': 0, 'x10': 0, 'x11': 0, 'x12': 0, 'x13': 0})
            elif (str(secondCard) == '5'):
                writer.writerow({'Card': str(secondCard),'CribScore': cribScore,
                        'x1': 0, 'x2': 0, 'x3': 0, 'x4': 0, 'x5': 1, 'x6': 0, 'x7': 0, 'x8': 0, 'x9': 0, 'x10': 0, 'x11': 0, 'x12': 0, 'x13': 0})
            elif (str(secondCard) == '6'):
                writer.writerow({'Card': str(secondCard),'CribScore': cribScore,
                        'x1': 0, 'x2': 0, 'x3': 0, 'x4': 0, 'x5': 0, 'x6': 1, 'x7': 0, 'x8': 0, 'x9': 0, 'x10': 0, 'x11': 0, 'x12': 0, 'x13': 0})
            elif (str(secondCard) == '7'):
                writer.writerow({'Card': str(secondCard),'CribScore': cribScore,
                        'x1': 0, 'x2': 0, 'x3': 0, 'x4': 0, 'x5': 0, 'x6': 0, 'x7': 1, 'x8': 0, 'x9': 0, 'x10': 0, 'x11': 0, 'x12': 0, 'x13': 0})
            elif (str(secondCard) == '8'):
                writer.writerow({'Card': str(secondCard),'CribScore': cribScore,
                        'x1': 0, 'x2': 0, 'x3': 0, 'x4': 0, 'x5': 0, 'x6': 0, 'x7': 0, 'x8': 1, 'x9': 0, 'x10': 0, 'x11': 0, 'x12': 0, 'x13': 0})
            elif (str(secondCard) == '9'):
                writer.writerow({'Card': str(secondCard),'CribScore': cribScore,
                        'x1': 0, 'x2': 0, 'x3': 0, 'x4': 0, 'x5': 0, 'x6': 0, 'x7': 0, 'x8': 0, 'x9': 1, 'x10': 0, 'x11': 0, 'x12': 0, 'x13': 0})
            elif (str(secondCard) == '10'):
                writer.writerow({'Card': str(secondCard),'CribScore': cribScore,
                        'x1': 0, 'x2': 0, 'x3': 0, 'x4': 0, 'x5': 0, 'x6': 0, 'x7': 0, 'x8': 0, 'x9': 0, 'x10': 1, 'x11': 0, 'x12': 0, 'x13': 0})
            elif (str(secondCard) == '11'):
                writer.writerow({'Card': str(secondCard),'CribScore': cribScore,
                        'x1': 0, 'x2': 0, 'x3': 0, 'x4': 0, 'x5': 0, 'x6': 0, 'x7': 0, 'x8': 0, 'x9': 0, 'x10': 0, 'x11': 1, 'x12': 0, 'x13': 0})
            elif (str(secondCard) == '12'):
                writer.writerow({'Card': str(secondCard),'CribScore': cribScore,
                        'x1': 0, 'x2': 0, 'x3': 0, 'x4': 0, 'x5': 0, 'x6': 0, 'x7': 0, 'x8': 0, 'x9': 0, 'x10': 0, 'x11': 0, 'x12': 1, 'x13': 0})
            elif (str(secondCard) == '13'):
                writer.writerow({'Card': str(secondCard),'CribScore': cribScore,
                        'x1': 0, 'x2': 0, 'x3': 0, 'x4': 0, 'x5': 0, 'x6': 0, 'x7': 0, 'x8': 0, 'x9': 0, 'x10': 0, 'x11': 0, 'x12': 0, 'x13': 1})
        elif (str(dealer) == 'Bill'):
        #writing the third card into the rows with the crib score
            if (str(thirdCard) == '1'):
                writer.writerow({'Card': str(thirdCard),'CribScore': cribScore,
                        'x1': 1, 'x2': 0, 'x3': 0, 'x4': 0, 'x5': 0, 'x6': 0, 'x7': 0, 'x8': 0, 'x9': 0, 'x10': 0, 'x11': 0, 'x12': 0, 'x13': 0})
            elif (str(thirdCard) == '2'):
                writer.writerow({'Card': str(thirdCard),'CribScore': cribScore,
                        'x1': 0, 'x2': 1, 'x3': 0, 'x4': 0, 'x5': 0, 'x6': 0, 'x7': 0, 'x8': 0, 'x9': 0, 'x10': 0, 'x11': 0, 'x12': 0, 'x13': 0})
            elif (str(thirdCard) == '3'):
                writer.writerow({'Card': str(thirdCard),'CribScore': cribScore,
                        'x1': 0, 'x2': 0, 'x3': 1, 'x4': 0, 'x5': 0, 'x6': 0, 'x7': 0, 'x8': 0, 'x9': 0, 'x10': 0, 'x11': 0, 'x12': 0, 'x13': 0})
            elif (str(thirdCard) == '4'):
                writer.writerow({'Card': str(thirdCard),'CribScore': cribScore,
                        'x1': 0, 'x2': 0, 'x3': 0, 'x4': 1, 'x5': 0, 'x6': 0, 'x7': 0, 'x8': 0, 'x9': 0, 'x10': 0, 'x11': 0, 'x12': 0, 'x13': 0})
            elif (str(thirdCard) == '5'):
                writer.writerow({'Card': str(thirdCard),'CribScore': cribScore,
                        'x1': 0, 'x2': 0, 'x3': 0, 'x4': 0, 'x5': 1, 'x6': 0, 'x7': 0, 'x8': 0, 'x9': 0, 'x10': 0, 'x11': 0, 'x12': 0, 'x13': 0})
            elif (str(thirdCard) == '6'):
                writer.writerow({'Card': str(thirdCard),'CribScore': cribScore,
                        'x1': 0, 'x2': 0, 'x3': 0, 'x4': 0, 'x5': 0, 'x6': 1, 'x7': 0, 'x8': 0, 'x9': 0, 'x10': 0, 'x11': 0, 'x12': 0, 'x13': 0})
            elif (str(thirdCard) == '7'):
                writer.writerow({'Card': str(thirdCard),'CribScore': cribScore,
                        'x1': 0, 'x2': 0, 'x3': 0, 'x4': 0, 'x5': 0, 'x6': 0, 'x7': 1, 'x8': 0, 'x9': 0, 'x10': 0, 'x11': 0, 'x12': 0, 'x13': 0})
            elif (str(thirdCard) == '8'):
                writer.writerow({'Card': str(thirdCard),'CribScore': cribScore,
                        'x1': 0, 'x2': 0, 'x3': 0, 'x4': 0, 'x5': 0, 'x6': 0, 'x7': 0, 'x8': 1, 'x9': 0, 'x10': 0, 'x11': 0, 'x12': 0, 'x13': 0})
            elif (str(thirdCard) == '9'):
                writer.writerow({'Card': str(thirdCard),'CribScore': cribScore,
                        'x1': 0, 'x2': 0, 'x3': 0, 'x4': 0, 'x5': 0, 'x6': 0, 'x7': 0, 'x8': 0, 'x9': 1, 'x10': 0, 'x11': 0, 'x12': 0, 'x13': 0})
            elif (str(thirdCard) == '10'):
                writer.writerow({'Card': str(thirdCard),'CribScore': cribScore,
                        'x1': 0, 'x2': 0, 'x3': 0, 'x4': 0, 'x5': 0, 'x6': 0, 'x7': 0, 'x8': 0, 'x9': 0, 'x10': 1, 'x11': 0, 'x12': 0, 'x13': 0})
            elif (str(thirdCard) == '11'):
                writer.writerow({'Card': str(thirdCard),'CribScore': cribScore,
                        'x1': 0, 'x2': 0, 'x3': 0, 'x4': 0, 'x5': 0, 'x6': 0, 'x7': 0, 'x8': 0, 'x9': 0, 'x10': 0, 'x11': 1, 'x12': 0, 'x13': 0})
            elif (str(thirdCard) == '12'):
                writer.writerow({'Card': str(thirdCard),'CribScore': cribScore,
                        'x1': 0, 'x2': 0, 'x3': 0, 'x4': 0, 'x5': 0, 'x6': 0, 'x7': 0, 'x8': 0, 'x9': 0, 'x10': 0, 'x11': 0, 'x12': 1, 'x13': 0})
            elif (str(thirdCard) == '13'):
                writer.writerow({'Card': str(thirdCard),'CribScore': cribScore,
                        'x1': 0, 'x2': 0, 'x3': 0, 'x4': 0, 'x5': 0, 'x6': 0, 'x7': 0, 'x8': 0, 'x9': 0, 'x10': 0, 'x11': 0, 'x12': 0, 'x13': 1})            
        #writing the fourth card into the rows with the same crib score    
            if (str(fourthCard) == '1'):
                writer.writerow({'Card': str(fourthCard),'CribScore': cribScore,
                        'x1': 1, 'x2': 0, 'x3': 0, 'x4': 0, 'x5': 0, 'x6': 0, 'x7': 0, 'x8': 0, 'x9': 0, 'x10': 0, 'x11': 0, 'x12': 0, 'x13': 0})
            elif (str(fourthCard) == '2'):
                writer.writerow({'Card': str(fourthCard),'CribScore': cribScore,
                        'x1': 0, 'x2': 1, 'x3': 0, 'x4': 0, 'x5': 0, 'x6': 0, 'x7': 0, 'x8': 0, 'x9': 0, 'x10': 0, 'x11': 0, 'x12': 0, 'x13': 0})
            elif (str(fourthCard) == '3'):
                writer.writerow({'Card': str(fourthCard),'CribScore': cribScore,
                        'x1': 0, 'x2': 0, 'x3': 1, 'x4': 0, 'x5': 0, 'x6': 0, 'x7': 0, 'x8': 0, 'x9': 0, 'x10': 0, 'x11': 0, 'x12': 0, 'x13': 0})
            elif (str(fourthCard) == '4'):
                writer.writerow({'Card': str(fourthCard),'CribScore': cribScore,
                        'x1': 0, 'x2': 0, 'x3': 0, 'x4': 1, 'x5': 0, 'x6': 0, 'x7': 0, 'x8': 0, 'x9': 0, 'x10': 0, 'x11': 0, 'x12': 0, 'x13': 0})
            elif (str(fourthCard) == '5'):
                writer.writerow({'Card': str(fourthCard),'CribScore': cribScore,
                        'x1': 0, 'x2': 0, 'x3': 0, 'x4': 0, 'x5': 1, 'x6': 0, 'x7': 0, 'x8': 0, 'x9': 0, 'x10': 0, 'x11': 0, 'x12': 0, 'x13': 0})
            elif (str(fourthCard) == '6'):
                writer.writerow({'Card': str(fourthCard),'CribScore': cribScore,
                        'x1': 0, 'x2': 0, 'x3': 0, 'x4': 0, 'x5': 0, 'x6': 1, 'x7': 0, 'x8': 0, 'x9': 0, 'x10': 0, 'x11': 0, 'x12': 0, 'x13': 0})
            elif (str(fourthCard) == '7'):
                writer.writerow({'Card': str(fourthCard),'CribScore': cribScore,
                        'x1': 0, 'x2': 0, 'x3': 0, 'x4': 0, 'x5': 0, 'x6': 0, 'x7': 1, 'x8': 0, 'x9': 0, 'x10': 0, 'x11': 0, 'x12': 0, 'x13': 0})
            elif (str(fourthCard) == '8'):
                writer.writerow({'Card': str(fourthCard),'CribScore': cribScore,
                        'x1': 0, 'x2': 0, 'x3': 0, 'x4': 0, 'x5': 0, 'x6': 0, 'x7': 0, 'x8': 1, 'x9': 0, 'x10': 0, 'x11': 0, 'x12': 0, 'x13': 0})
            elif (str(fourthCard) == '9'):
                writer.writerow({'Card': str(fourthCard),'CribScore': cribScore,
                        'x1': 0, 'x2': 0, 'x3': 0, 'x4': 0, 'x5': 0, 'x6': 0, 'x7': 0, 'x8': 0, 'x9': 1, 'x10': 0, 'x11': 0, 'x12': 0, 'x13': 0})
            elif (str(fourthCard) == '10'):
                writer.writerow({'Card': str(fourthCard),'CribScore': cribScore,
                        'x1': 0, 'x2': 0, 'x3': 0, 'x4': 0, 'x5': 0, 'x6': 0, 'x7': 0, 'x8': 0, 'x9': 0, 'x10': 1, 'x11': 0, 'x12': 0, 'x13': 0})
            elif (str(fourthCard) == '11'):
                writer.writerow({'Card': str(fourthCard),'CribScore': cribScore,
                        'x1': 0, 'x2': 0, 'x3': 0, 'x4': 0, 'x5': 0, 'x6': 0, 'x7': 0, 'x8': 0, 'x9': 0, 'x10': 0, 'x11': 1, 'x12': 0, 'x13': 0})
            elif (str(fourthCard) == '12'):
                writer.writerow({'Card': str(fourthCard),'CribScore': cribScore,
                        'x1': 0, 'x2': 0, 'x3': 0, 'x4': 0, 'x5': 0, 'x6': 0, 'x7': 0, 'x8': 0, 'x9': 0, 'x10': 0, 'x11': 0, 'x12': 1, 'x13': 0})
            elif (str(fourthCard) == '13'):
                writer.writerow({'Card': str(fourthCard),'CribScore': cribScore,
                        'x1': 0, 'x2': 0, 'x3': 0, 'x4': 0, 'x5': 0, 'x6': 0, 'x7': 0, 'x8': 0, 'x9': 0, 'x10': 0, 'x11': 0, 'x12': 0, 'x13': 1})

""" 

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
    clf = linear_model.Lasso(alpha=0.01, fit_intercept= True, max_iter = 2000,)
    clf.fit(x, y)
    print(clf.coef_)
    print(clf.intercept_)

"""
results = []
with open('oneCardIntoCrib.csv', 'r') as csvFile:
    reader = csv.DictReader(csvFile)
    
    for row in reader:
        #print(row['Card'], row['x1'], row['x2'], row['x3'], row['x4'], row['x5'], row['x6'], row['x7'], row['x8'], row['x9'], row['x10'], row['x11'] , row['x12'] , row['x13'], row['CribScore'])
        results.append(row)
    x = []
    y = []
    for i in range(0,len(results)):
        observation = []
        for j in range(1,14):
           observation.append(int(results[i]['x' + str(j)]))   
        y.append(int(results[i]['CribScore']))
        x.append(observation)
    clf = linear_model.Lasso(alpha=0.0001, fit_intercept= True, max_iter = 2000,)
    clf.fit(x, y)
    print(clf.coef_)
    print(clf.intercept_)
"""


"""
    clf = linear_model.Lasso(alpha=0.1)
    array = []
    for row in reader:
        var1 = row['x1']
        var2 = row['x2']
        var3 = row['x3']
        var4 = row['x4']
        var5 = row['x5']
        var6 = row['x6']
        var7 = row['x7']
        var8 = row['x8']
        var9 = row['x9']
        var10 = row['x10']
        var11 = row['x11']
        var12 = row['x12']
        var13 = row['x13']
        yVar = [row['CribScore']]
        array.append([[var1,var2,var3,var4,var5,var6,var7,var8,var9,var10,var11,var12,var13]], [yVar])
        #clf.fit([ [row['Card']], [row['x1']], [row['x2']], [row['x3']], [row['x4']], [row['x5']], [row['x6']], [row['x7']], [row['x8']], [row['x9']], [row['x10']], [row['x11']] , [row['x12']], [row['x13']] ], [row['CribScore']] )
        #
    #print(clf.coef_)
    #print(clf.intercept_)
    print(array)
"""
"""
clf = linear_model.Lasso(alpha=0.1)
clf.fit([[9,21], [4,26], [7,25]], [83, 95, 92])
print(clf.coef_)
print(clf.intercept_)
"""

"""
clf = linear_model.Lasso(alpha=1)
clf.fit([[9,21], [4,26], [7,25]], [83, 95, 92])
print(clf.coef_)
print(clf.intercept_)

clf = linear_model.Lasso(alpha=0.99)
clf.fit([[9,21], [4,26], [7,25]], [83, 95, 92])
print(clf.coef_)
print(clf.intercept_)
"""

