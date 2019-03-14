#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np


# In[2]:


Election="election_data.csv"


# In[3]:


Election2=pd.read_csv(Election)


# In[4]:


Election2


# In[5]:


totalvotes=Election2["Voter ID"].count()


# In[6]:


Candidate=Election2["Candidate"].value_counts()
Candidate


# In[7]:


CandidateSum=Candidate.sum()
CandidateSum


# In[8]:


Khan=((2218231/CandidateSum)*100)
Correy=((704200/CandidateSum)*100)
Li=((492940/CandidateSum)*100)
Otooley=((105630/CandidateSum)*100)
print(Khan)
print(Correy)
print(Li)
print(Otooley)


# In[9]:


Candidate.max()


# In[13]:


print("Total Votes:", totalvotes, "\n", "Khan: 63.000% (2218231)", "\n","Correy: 20.000% (704200)", "\n", "Li: 14.000% (492940)", "\n", "O'Tooley: 3.000% (105630)", "\n", "Winner: Khan")


# In[12]:





# In[ ]:




