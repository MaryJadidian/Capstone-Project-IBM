#!/usr/bin/env python
# coding: utf-8

# <p style="text-align:center">
#     <a href="https://skills.network/?utm_medium=Exinfluencer&utm_source=Exinfluencer&utm_content=000026UJ&utm_term=10006555&utm_id=NA-SkillsNetwork-Channel-SkillsNetworkCoursesIBMDA0321ENSkillsNetwork928-2022-01-01" target="_blank">
#     <img src="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/assets/logos/SN_web_lightmode.png" width="200" alt="Skills Network Logo"  />
#     </a>
# </p>
# 

# # **Web Scraping Lab**
# 

# Estimated time needed: **30** minutes
# 

# ## Objectives
# 

# After completing this lab you will be able to:
# 

# * Download a webpage using requests module
# * Scrape all links from a web page
# * Scrape all image urls from a web page
# * Scrape data from html tables
# 

# ## Scrape www.ibm.com
# 

# Import the required modules and functions
# 

# In[1]:


from bs4 import BeautifulSoup # this module helps in web scrapping.
import requests  # this module helps us to download a web page


# Download the contents of the web page
# 

# In[2]:


url = "http://www.ibm.com"


# In[3]:


# get the contents of the webpage in text format and store in a variable called data
data  = requests.get(url).text 


# Create a soup object using the class BeautifulSoup
# 

# In[4]:


soup = BeautifulSoup(data,"html5lib")  # create a soup object using the variable 'data'


# Scrape all links
# 

# In[5]:


for link in soup.find_all('a'):  # in html anchor/link is represented by the tag <a>
    print(link.get('href'))


# Scrape  all images
# 

# In[6]:


for link in soup.find_all('img'):# in html image is represented by the tag <img>
    print(link.get('src'))


# ## Scrape data from html tables
# 

# In[ ]:


#The below url contains a html table with data about colors and color codes.


# In[7]:


url = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DA0321EN-SkillsNetwork/labs/datasets/HTMLColorCodes.html"


# Before proceeding to scrape a web site, you need to examine the contents, and the way data is organized on the website. Open the above url in your browser and check how many rows and columns are there in the color table.
# 

# In[8]:


# get the contents of the webpage in text format and store in a variable called data
data  = requests.get(url).text


# In[9]:


soup = BeautifulSoup(data,"html5lib")


# In[10]:


#find a html table in the web page
table = soup.find('table') # in html table is represented by the tag <table>


# In[11]:


#Get all rows from the table
for row in table.find_all('tr'): # in html table row is represented by the tag <tr>
    # Get all columns in each row.
    cols = row.find_all('td') # in html a column is represented by the tag <td>
    color_name = cols[2].getText() # store the value in column 3 as color_name
    color_code = cols[3].getText() # store the value in column 4 as color_code
    print("{}--->{}".format(color_name,color_code))


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

# |  Date (YYYY-MM-DD) |  Version | Changed By  |  Change Description |
# |---|---|---|---|
# | 2020-10-17  | 0.1  | Ramesh Sannareddy  |  Created initial version of the lab |
# 

#  Copyright &copy; 2020 IBM Corporation. This notebook and its source code are released under the terms of the [MIT License](https://cognitiveclass.ai/mit-license/?utm_medium=Exinfluencer&utm_source=Exinfluencer&utm_content=000026UJ&utm_term=10006555&utm_id=NA-SkillsNetwork-Channel-SkillsNetworkCoursesIBMDA0321ENSkillsNetwork928-2022-01-01).
# 
