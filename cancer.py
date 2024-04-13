# -*- coding: utf-8 -*-
"""cancer.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/gist/gopsthv/78971847bc51d662113a7a159fcca2d1/copy-of-untitled4.ipynb
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("/content/drive/MyDrive/data.csv")

df.head(10)

df.shape

df.isna().sum()

df.drop(['Unnamed: 32','id'],axis='columns',inplace=True)

df['diagnosis'].value_counts()

sns.countplot(df['diagnosis'])

from sklearn.preprocessing import LabelEncoder

df.iloc[:,0:5].corr()

sns.heatmap(df.iloc[:,0:5].corr(), annot=True)

X = df.iloc[:,1:31].values
Y = df.iloc[:,0].values

from sklearn.model_selection import train_test_split
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size = 0.2, random_state = 0)

from sklearn.neighbors import KNeighborsClassifier
clf = KNeighborsClassifier()
clf.fit(X_train, Y_train)

clf.score(X_test, Y_test)