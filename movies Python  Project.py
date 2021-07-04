#!/usr/bin/env python
# coding: utf-8

# In[2]:


# Importing required libraries for this Project.

import pandas as pd
import numpy as np
import seaborn as sns

import matplotlib.pyplot as plt
import matplotlib.mlab as mlab
import matplotlib
plt.style.use('ggplot')
from matplotlib.pyplot import figure

get_ipython().run_line_magic('matplotlib', 'inline')
matplotlib.rcParams['figure.figsize'] = (12,8)

pd.options.mode.chained_assignment = None

# Now need to read the data file from system

df = pd.read_csv(r'D:\movies2.csv')


                    


# In[42]:


# Now lets look at the data
df


# In[46]:


# Serching for Missing data
for col in df.columns:
    pct_missing=np.mean(df[col].isnull())
    print(col,pct_missing)
    
    


# In[48]:


# Data Types of the column

df.dtypes


# In[57]:


# Creating another row of  year  as 'Correctyear'. we can see some of the year's from release date and year are no matching

df['correctyear']=df['released'].astype(str).str[6:10]
df


# In[64]:


pd.set_option('display.max_rows',None)
df.sort_values(by='gross' ,ascending=False)


# In[65]:


# Drop any duplictes

df.drop_duplicates()


# In[36]:


# Plot Bugget vs gross using seabord
plt.scatter(x=df['budget'], y=df['gross'], alpha=0.5)
plt.title('Budget vs Gross Earnings')
plt.xlabel('Gross Earnings')
plt.ylabel('Budget for Film')
plt.show()

sns.regplot(x="gross", y="budget",data=df, line_kws={"color":"blue"})


# In[13]:


# Plot Score vs gross using seabord
sns.regplot(x="score", y="gross", data=df , line_kws={"color":"black"})


# In[14]:


# Correlation Matrix between all numeric columns

df.corr()
# default  correlation method is pearson


# In[18]:


# Visualization corelation

correlation_matrix = df.corr()
sns.heatmap(correlation_matrix, annot = True)
plt.title("Correlation Feature for Numeric Features")
plt.xlabel("Movie features")
plt.ylabel("Movie features")
plt.show()


# ### High Corelation between Gross and Budget (0.71)

# In[25]:


df_numerized=df
for col_name in df_numerized.columns:
    if(df_numerized[col_name].dtype =='object'):
        df_numerized[col_name] = df_numerized[col_name].astype('category')
        df_numerized[col_name]=df_numerized[col_name].cat.codes
        
df_numerized        


# In[27]:


df_numerized.corr()


# In[28]:


correlation_matrix = df_numerized.corr()

sns.heatmap(correlation_matrix, annot = True)

plt.title("Correlation matrix for Movies")

plt.xlabel("Movie features")

plt.ylabel("Movie features")

plt.show()


# In[44]:


pd.set_option('display.max_rows',None)
correlation_mat=df_numerized.corr()
corr_pairs=correlation_mat.unstack()
corr_pairs


# In[43]:


pd.set_option('display.max_rows',None)
sorted_pairs=corr_pairs.sort_values()
sorted_pairs


# In[42]:


pd.set_option('display.max_rows',None)
high_corr=sorted_pairs[(sorted_pairs)>.05]
high_corr


# ###  Votes and Budget have the higest corellation to gross earnings

# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




