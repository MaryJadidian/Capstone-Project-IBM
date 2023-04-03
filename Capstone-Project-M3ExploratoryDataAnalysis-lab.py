#!/usr/bin/env python
# coding: utf-8

# <p style="text-align:center">
#     <a href="https://skills.network/?utm_medium=Exinfluencer&utm_source=Exinfluencer&utm_content=000026UJ&utm_term=10006555&utm_id=NA-SkillsNetwork-Channel-SkillsNetworkCoursesIBMDA0321ENSkillsNetwork21426264-2022-01-01" target="_blank">
#     <img src="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/assets/logos/SN_web_lightmode.png" width="200" alt="Skills Network Logo"  />
#     </a>
# </p>
# 

# # **Exploratory Data Analysis Lab**
# 

# Estimated time needed: **30** minutes
# 

# In this module you get to work with the cleaned dataset from the previous module.
# 
# In this assignment you will perform the task of exploratory data analysis.
# You will find out the distribution of data, presence of outliers and also determine the correlation between different columns in the dataset.
# 

# ## Objectives
# 

# In this lab you will perform the following:
# 

# *   Identify the distribution of data in the dataset.
# 
# *   Identify outliers in the dataset.
# 
# *   Remove outliers from the dataset.
# 
# *   Identify correlation between features in the dataset.
# 

# ***
# 

# ## Hands on Lab
# 

# Import the pandas module.
# 

# In[12]:


import pandas as pd
import numpy as np
import seaborn as sns 
import matplotlib.pyplot as plt
from scipy.stats import norm
get_ipython().run_line_magic('matplotlib', 'inline')


# Load the dataset into a dataframe.
# 

# In[13]:


df = pd.read_csv("https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DA0321EN-SkillsNetwork/LargeData/m2_survey_data.csv")


# In[14]:


df.head()


# In[15]:


df.shape


# ## Distribution
# 

# ### Determine how the data is distributed
# 

# The column `ConvertedComp` contains Salary converted to annual USD salaries using the exchange rate on 2019-02-01.
# 
# This assumes 12 working months and 50 working weeks.
# 

# Plot the distribution curve for the column `ConvertedComp`.
# 

# In[16]:


plt.figure(figsize=(10, 5))
sns.distplot(a=df['ConvertedComp'], bins=20, hist=False)
plt.show()


# Plot the histogram for the column `ConvertedComp`.
# 

# In[17]:


plt.figure(figsize=(10, 5))
sns.distplot(a=df['ConvertedComp'], bins=20, kde=False)
plt.show()


# What is the median of the column `ConvertedComp`?
# 

# In[18]:


df['ConvertedComp'].median()


# How many responders identified themselves only as a **Man**?
# 

# In[19]:


df['Gender'].value_counts()


# Find out the  median ConvertedComp of responders identified themselves only as a **Woman**?
# 

# In[20]:


woman=df[df['Gender'] =='Woman']
woman['ConvertedComp'].median()


# Give the five number summary for the column `Age`?
# 

# **Double click here for hint**.
# 
# <!--
# min,q1,median,q3,max of a column are its five number summary.
# -->
# 

# In[26]:


#calculate a 5-number summary
data=np.array(df['Age'])
#calculate quartiles
quartiles=np.nanpercentile(data, [25, 50, 75])
#calculate min/max
data_min, data_max=data[0].min(), data[0].max()
#print 5-number summary
print('Min: %.3f' %data_min)
#print('Max: %.3f' %data_max)
print('Q1: %.3f' % quartiles[0])
print('Median: %.3f' % quartiles[1])
print('Q3 %.3f' % quartiles[2])
print('Max: %.3f' %data_max)


# Plot a histogram of the column `Age`.
# 

# In[29]:


df.hist(column='Age', bins=range (0, 80, 8), figsize=(10,5), color='#86bf91', rwidth=0.8)
plt.xlabel('Age')
plt.ylabel('Count')
plt.show()


# In[31]:


plt.figure(figsize=(15,5))
sns.boxplot(x=df.Age, data=df)
plt.show()


# ## Outliers
# 

# ### Finding outliers
# 

# Find out if outliers exist in the column `ConvertedComp` using a box plot?
# 

# In[30]:


plt.figure(figsize=(20,3))
sns.boxplot(x=df.ConvertedComp, data=df)
plt.show()


# Find out the Inter Quartile Range for the column `ConvertedComp`.
# 

# In[32]:


df['ConvertedComp'].describe()


# In[35]:


q1=df['ConvertedComp'].quantile(0.25)
q3=df['ConvertedComp'].quantile(0.75)
iqr=q3-q1
print("The interquartile range for 'ConvertedComp' is:", iqr)


# Find out the upper and lower bounds.
# 

# In[37]:


lower_bound=q1-(1.5*iqr)
upper_bound=q3+(1.5*iqr)
print("The lower bound for 'ConvertedComp is:", lower_bound)
print("The upper bound for 'ConvertedComp' is:", upper_bound)


# Identify how many outliers are there in the `ConvertedComp` column.
# 

# In[38]:


outliers = df[(df['ConvertedComp'] < lower_bound) | (df['ConvertedComp'] > upper_bound)]
num_outliers=len(outliers)
print("The number of outliers in'ConvertedComp' is:", num_outliers)


# Create a new dataframe by removing the outliers from the `ConvertedComp` column.
# 

# In[39]:


new_df = df[(df['ConvertedComp'] >= lower_bound) & (df['ConvertedComp'] <= upper_bound)]
num_outliers = len(df) - len(new_df)
num_data_points = len(new_df)

print("The number of outliers in 'ConvertedComp' is:", num_outliers)
print("The number of data points in the new dataframe is:", num_data_points)


# In[40]:


new_df.head()


# In[41]:


new_df['ConvertedComp'].median()


# In[42]:


new_df['ConvertedComp'].mean()


# ## Correlation
# 

# ### Finding correlation
# 

# Find the correlation between `Age` and all other numerical columns.
# 

# In[44]:


corr=df.corr()['Age']
print(corr)


# ## Authors
# 

# Ramesh Sannareddy
# 

# ### Other Contributors
# 

# Rav Ahuja
# 

# ## Change Log
# 

# | Date (YYYY-MM-DD) | Version | Changed By        | Change Description                 |
# | ----------------- | ------- | ----------------- | ---------------------------------- |
# | 2020-10-17        | 0.1     | Ramesh Sannareddy | Created initial version of the lab |
# 

# Copyright © 2020 IBM Corporation. This notebook and its source code are released under the terms of the [MIT License](https://cognitiveclass.ai/mit-license?utm_medium=Exinfluencer&utm_source=Exinfluencer&utm_content=000026UJ&utm_term=10006555&utm_id=NA-SkillsNetwork-Channel-SkillsNetworkCoursesIBMDA0321ENSkillsNetwork21426264-2022-01-01&cm_mmc=Email_Newsletter-\_-Developer_Ed%2BTech-\_-WW_WW-\_-SkillsNetwork-Courses-IBM-DA0321EN-SkillsNetwork-21426264&cm_mmca1=000026UJ&cm_mmca2=10006555&cm_mmca3=M12345678&cvosrc=email.Newsletter.M12345678&cvo_campaign=000026UJ).
# 
