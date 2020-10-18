# -*- coding: utf-8 -*-
"""
Created on Sat Oct 10 09:26:10 2020

@author: MAYANK
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd



# Data Loading
dataset = pd.read_csv('Market_Basket_Optimisation.csv', header = None)

# Adding all customers into a list of lists
transactions = []
for i in range(0, 7501):
    transactions.append([str(dataset.values[i,j]) for j in range(0, 20)])
    
from apyori import apriori
rules = apriori(transactions, min_support = 0.003, min_confidence = 0.2, min_lift = 3, min_length =2 )
results=list(rules)




lift = []
association = []
for i in range (0, len(results)):
    lift.append(results[:len(results)][i][2][0][3])
    association.append(list(results[:len(results)][i][0]))



for i in association:
    if "nan" in i:
        i.remove("nan")
#print(rules)

with open('your_file.txt', 'w') as f:
    for item in association:
        for i in item:
            f.write("%s" % i)
            f.write("-")
        f.write("\n")
rank = pd.DataFrame([association, lift]).T
rank.columns = ['Association', 'Lift']

# Show top 10 higher lift scores
rank.sort_values('Lift', ascending=False).head(10)


print(rank)