#!/usr/bin/env python
# coding: utf-8

# In[3]:


get_ipython().system('pip install requests')


# In[2]:


get_ipython().system('pip install bs4')


# In[6]:


import pandas as pd
from bs4 import BeautifulSoup
import requests


# In[7]:


url="https://quotes.toscrape.com/page/1/"


# In[8]:


response=requests.get(url)


# In[9]:


response.content


# In[10]:


soup=BeautifulSoup(response.content,'html.parser')


# In[11]:


print(soup.prettify())


# In[16]:


row=soup.find('div')
row


# In[17]:


quote=row.find_all('div',class_='quote')
quote


# In[18]:


#scapping quotes 
for quotes in quote:
    q = quotes.find('span', class_ = 'text').text
    print(q)


# In[20]:


# scrapping tags from content

for tag in quote:
    t = tag.find('meta')
    tags = t.attrs['content']
    print(tags)


# In[21]:


# Creating variable Contents to save the contents in a list.

page = row.find_all('div', class_ = 'quote')

list_1 = []

for items in page:
    q = items.find('span', class_ = 'text').text
    aut = items.find('small', class_ = 'author').text
    t = items.find('meta')
    tag = t.attrs['content']
    list_1.append([q,aut,tag])

print(list_1)


# In[22]:


list_1


# In[23]:


df = pd.DataFrame(list_1, columns=['Quote', 'Author', 'Tags'])

df


# In[24]:


# scrapping contents from all 10 pages available in the website.

list_2 = []

for i in range (1,10):
    url = f"http://quotes.toscrape.com/page/{i}/"
    r = requests.get(url)
    c = r.content
    html = BeautifulSoup(c,'html.parser')
    con = html.find(class_ = 'container')
    C = con.find_all('div', class_ = 'quote')
    for items in C:
        q = items.find('span', class_ = 'text').text
        n = items.find('small', class_ = 'author').text
        t = items.find('meta')
        tag = t.attrs['content']
        list_2.append([q,n,tag])


# In[25]:


list_2


# In[26]:


# turning list into dataframe
df1 = pd.DataFrame(list_2, columns=['Quote', 'Author', 'Tags'])
df1


# In[27]:


#conveting datafram into csv file

df1.to_csv('Quotes_to_Scrape.xlsx')


# In[28]:


df1


# In[ ]:




