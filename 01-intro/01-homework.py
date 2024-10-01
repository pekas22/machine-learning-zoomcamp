import pandas as pd
import csv

##Q1. Pandas Version
np.__version__

##Q2. Records count
#Load table
df = pd.read_csv('laptops.csv')

df.shape[0]

##Q3. Laptop brands
len(pd.unique(df['Brand']))

##Q4. Missing values
df.isnull().sum()

##Q5. Maximum final price
#filter on dell
df_dell = df[df['Brand'] == 'Dell']
#find the max value
df_dell['Final Price'].max()

##Q6. Median value of Screen
#import numpy
import numpy as np
#median value
df.Screen.median()
#mode the most frequent value
#The most frequent value can also like this
df.Screen.value_counts()
#make a copy for not make changes on the base
new_df = df.Screen.fillna(df.Screen.median())
#Check if the nulls were filled 
new_df.isnull().sum()
#See if median has changed
new_df.median()

##Q7. Sum of weights
df_innjoo = df[df.Brand== 'Innjoo']
a = df_innjoo[['RAM','Storage','Screen']]

#get the array X
X = np.asarray(a)

#transpose
X_T = X.T
#multiply transpoose with X
XTX = np.dot(X_T, X) 
#invertion on XTX
XTX_1 = np.linalg.inv(XTX) 
#creat y array
y = np.array([1100, 1300, 800, 900, 1000, 1100])
#multiply the inverse of XTX with the transpose of X, and then multiply the result by y. Call the result w
W = np.dot(np.dot(XTX_1,X_T),y)
#sum of all elements
sum(W)
