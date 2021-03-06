
# coding: utf-8

# In[72]:


import os
get_ipython().magic('matplotlib inline')
import matplotlib
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression


# In[103]:


data = pd.read_csv("C:/Users/Santhoshkumar/Desktop/Abhi/pbp-2016.csv")
data = data.drop(['Minute','Second','IsTwoPointConversionSuccessful','RushDirection','YardLineFixed','YardLineDirection', 'IsPenaltyAccepted', 'PenaltyTeam','PenaltyType','PenaltyYards'], axis =1)
data = data.drop(['IsFumble','IsInterception','IsMeasurement','Challenger','IsChallengeReversed','PassType','IsTouchdown','SeriesFirstDown','Unnamed: 10','ToGo','YardLine'], axis = 1)
data = data.drop(['NextScore','Description','Unnamed: 17', 'SeasonYear','IsIncomplete','IsChallenge'], axis = 1)
data = data.drop(['Unnamed: 12','Unnamed: 16','TeamWin','GameId'],axis = 1)
data = data.dropna()
#ata = pd.concat([data, pd.get_dummies(data['Formation'])], axis =1)
#ata = data.drop(['Formation'], axis = 1)
data = pd.concat([data, pd.get_dummies(data['PlayType'])], axis =1)
data = data.drop(['PlayType'], axis = 1)
column_a = data['Yards']
column_a
b = []

# print (data.groupby(['Formation','Yards']).groups)
data


# In[121]:


df = pd.read_csv("Madden-NFL-17-Launch-Ratings-Full-League.csv")
df = df[["First", "Last", "Team", "Position", "OVR"]]

df = df.sort_values("OVR", ascending=False)

teams =  np.unique(df[['Team']])

posi = np.unique(df[['Position']])



# In[130]:


filtered = []

for i in teams:
    for p in posi:
        filtered.append((df[(df["Team"]==i) & (df["Position"] == p)].head(1).values))


# In[132]:


filtered

