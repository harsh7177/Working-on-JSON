#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests
from  bs4 import BeautifulSoup


# In[3]:


url = "https://cricbuzz-cricket.p.rapidapi.com/matches/v1/recent"

headers = {
	"X-RapidAPI-Key": "cd42f8ccfcmsh5057d212e7b1aa4p1c9c1ajsne4ee85f781de",
	"X-RapidAPI-Host": "cricbuzz-cricket.p.rapidapi.com"
}

response = requests.get(url, headers=headers)


# In[385]:


result=[]
t2_overs=[]
t2_wickets=[]
t2_runs=[]
t1_overs=[]
t1_wickets=[]
t1_runs=[]
title=[]
ODI=[]
ground=[]
T2_name=[]
T1_name=[]
series_name=[]
for i in range(4):
    a=d['typeMatches'][i]
    for j in range(len(a['seriesMatches'])):
        b=a['seriesMatches'][j]
        if 'seriesAdWrapper' in b:
            for k in range (len(b['seriesAdWrapper']['matches'])):
                c=b['seriesAdWrapper']['matches'][k]
                series_name.append(c['matchInfo']['seriesName'])
                T1_name.append(c['matchInfo']['team1']['teamName'])
                T2_name.append(c['matchInfo']['team2']['teamName'])
                ground.append(c['matchInfo']['venueInfo']['ground'])
                ODI.append(c['matchInfo']['matchDesc'])
                title.append(c['matchInfo']['stateTitle'])
                if 'matchScore' in c:
                    t1_runs.append(c['matchScore']['team1Score']['inngs1']['runs'])
                    t1_wickets.append(c['matchScore']['team1Score']['inngs1']['wickets'])
                    t1_overs.append(c['matchScore']['team1Score']['inngs1']['overs'])
                    t2_runs.append(c['matchScore']['team1Score']['inngs1']['runs'])
                    t2_wickets.append(c['matchScore']['team1Score']['inngs1']['wickets'])
                    t2_overs.append(c['matchScore']['team1Score']['inngs1']['overs'])
                    result.append(c['matchInfo']['status'])
                else:
                    t1_runs.append('?')
                    t1_wickets.append('?')
                    t1_overs.append('?')
                    t2_runs.append('?')
                    t2_wickets.append('?')
                    t2_overs.append('?')
                    result.append('?')
                
        else:
            pass
            
                


# In[389]:


w=[series_name,title,ODI,ground,T2_name,T1_name,t2_overs,t2_wickets,t2_runs,t1_overs,t1_wickets,t1_runs,result]
for i in w:
    print(len(i))
names=['Series','Title','ODI','Ground','T1_Name','T2_Name','T1_overs','T1_wickets','T1_runs','T2_overs','T2_wickets','T2_runs','Result']


# In[393]:


import pandas as pd
df=pd.DataFrame(zip(series_name,title,ODI,ground,T2_name,T1_name,t2_overs,t2_wickets,t2_runs,t1_overs,t1_wickets,t1_runs,result),columns=names)


# In[394]:


df

