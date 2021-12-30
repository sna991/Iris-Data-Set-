#!/usr/bin/env python
# coding: utf-8

# In[3]:


import numpy as np 
import pandas as pd 
import seaborn as sns 
import matplotlib.pyplot as plt 
get_ipython().run_line_magic('matplotlib', 'inline')
import warnings 
warnings.filterwarnings('ignore')


# In[4]:


iris= pd.read_csv(r"C:\Users\sna99\Documents\Data Science\Projects\IRIS DATASET _ ADVANCE VISUALIZATION _ EDA 2\Iris.csv")


# In[5]:


iris


# In[6]:


iris.drop('Id',axis=1)


# In[9]:


iris.info() 


# In[11]:


list(iris)


# In[12]:


iris['Species'].value_counts()


# In[21]:


sns.countplot('Species',data=iris)
plt.title('Different Types of Species / Count')
plt.show()


# In[26]:


fig=sns.jointplot(x='SepalLengthCm',y='SepalWidthCm',data = iris)
fig=sns.jointplot(x='SepalLengthCm',y='SepalWidthCm',data = iris,kind='reg')
fig=sns.jointplot(x='SepalLengthCm',y='SepalWidthCm',data = iris,kind='hex')

