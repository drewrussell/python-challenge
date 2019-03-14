#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np


# In[2]:


Budget="Budget_Data.csv"


# In[3]:


Budget2=pd.read_csv(Budget)


# In[4]:


TotalMonths=Budget2["Date"].count()


# In[5]:


TotalMonths


# In[6]:


NetAmount=Budget2["Profit/Losses"].sum()


# In[7]:


NetAmount


# In[8]:


listpl=list(Budget2["Profit/Losses"])
listpl


S=pd.Series([867884,
 984655,
 322013,
 -69417,
 310503,
 522857,
 1033096,
 604885,
 -216386,
 477532,
 893810,
 -80353,
 779806,
 -335203,
 697845,
 793163,
 485070,
 584122,
 62729,
 668179,
 899906,
 834719,
 132003,
 309978,
 -755566,
 1170593,
 252788,
 1151518,
 817256,
 570757,
 506702,
 -1022534,
 475062,
 779976,
 144175,
 542494,
 359333,
 321469,
 67780,
 471435,
 565603,
 872480,
 789480,
 999942,
 -1196225,
 268997,
 -687986,
 1150461,
 682458,
 617856,
 824098,
 581943,
 132864,
 448062,
 689161,
 800701,
 1166643,
 947333,
 578668,
 988505,
 1139715,
 1029471,
 687533,
 -524626,
 158620,
 87795,
 423389,
 840723,
 568529,
 332067,
 989499,
 778237,
 650000,
 -1100387,
 -174946,
 757143,
 445709,
 712961,
 -1163797,
 569899,
 768450,
 102685,
 795914,
 60988,
 138230,
 671099])



    
    
    


# In[9]:


diff=S.diff()
pd.set_option('display.max_rows', 86)
diff


# In[10]:


averagediff=diff.mean()
averagediff


# In[11]:


maxpl=diff.max()
maxpl


# In[12]:


minpl=diff.min()
minpl


# In[ ]:





# In[15]:


listd=list(Budget2["Date"])
listd
maxdate=listd[25]
maxdate


# In[16]:


mindate=listd[44]
mindate


# In[55]:


print("Total Months:", TotalMonths, "\n", "Total:", NetAmount, "\n", "Average Change:", averagediff, "\n", "Greatest Increase in Profits:", maxdate, "(", "$", maxpl, ")", "\n", "Greatest Decrease in Profits:", mindate, "(", "$", minpl, ")")


# In[ ]:




