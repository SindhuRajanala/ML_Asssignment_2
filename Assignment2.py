#!/usr/bin/env python
# coding: utf-8

# In[68]:


import numpy as np
x = np.random.randint(1,20,15)
print(x)


# In[69]:


x=x.reshape(3,5)
print(x)


# In[70]:


x.shape


# In[72]:


a=np.where(x==x.max(axis=1)[:,None],0,x)
print(a)


# In[65]:


import pandas as pd

da = pd.read_csv("data.csv")
da


# In[38]:


da.describe()


# In[39]:


da.isnull().any()


# In[40]:


da.fillna(da.mean(), inplace=True)
da.isnull().any()


# In[41]:


da.agg({'Duration':['min','max','count','mean'],'Pulse':['min','max','count','mean']})


# In[42]:


da.loc[(da['Calories']>500)&(da['Calories']<1000)]


# In[43]:


da.loc[(da['Calories']>500)&(da['Pulse']<100)]


# In[64]:


df_modified = da[['Duration','Pulse','Calories']]
df_modified


# In[66]:


df=da.drop('Maxpulse',axis=1)
df


# In[63]:


da['Calories'] = da['Calories'].astype(np.int64)
da.dtypes


# In[52]:


da.plot.scatter(x='Duration',y='Calories',c='DarkBlue')


# In[54]:


import matplotlib.pyplot as pl
Programming_languages = 'Java', 'Python', 'PHP', 'JavaScript', 'C#', 'C++'
popularity = [22.2, 17.6, 8.8, 8, 7.7, 6.7]
color = ["#1f77b4", "#ff7f0e", "#2ca02c", "#d62728", "#9467bd", "#8c564b"]
explode = (0.1, 0, 0, 0,0,0)  
pl.pie(popularity, explode=explode, labels=Programming_languages, colors=color,
autopct='%1.1f%%', shadow=True, startangle=140)
pl.axis('equal')
pl.show()

