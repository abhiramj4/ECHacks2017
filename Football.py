
# coding: utf-8

# In[66]:


import os
get_ipython().magic('matplotlib inline')
import matplotlib
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression


# In[71]:


data = pd.read_csv("C:/Users/Santhoshkumar/Desktop/Abhi/pbp-2016.csv")
data = data.drop(['Minute','Second','IsTwoPointConversionSuccessful','RushDirection','YardLineFixed','YardLineDirection', 'IsPenaltyAccepted', 'PenaltyTeam','PenaltyType','PenaltyYards'], axis =1)
data = data.drop(['IsFumble','IsInterception','IsMeasurement','Challenger','IsChallengeReversed','PassType','IsTouchdown','SeriesFirstDown','Unnamed: 10','ToGo','YardLine'], axis = 1)
data = data.drop(['NextScore','Description','Unnamed: 17', 'SeasonYear','IsIncomplete','IsChallenge'], axis = 1)
data = data.drop(['Unnamed: 12','Unnamed: 16','TeamWin','GameId'], axis = 1)
data = data.dropna()
data = pd.concat([data, pd.get_dummies(data['Formation'])], axis =1)
data = data.drop(['Formation'], axis = 1)
data = pd.concat([data, pd.get_dummies(data['PlayType'])], axis =1)
data = data.drop(['PlayType'], axis = 1)
data


