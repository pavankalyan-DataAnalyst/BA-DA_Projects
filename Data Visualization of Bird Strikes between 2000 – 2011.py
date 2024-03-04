#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np


# In[5]:


df= pd.read_excel('Bird Strikes_Final.xlsx')


# In[6]:


df


# In[8]:


df.shape


# In[9]:


df.ndim


# In[11]:


df.describe()


# In[12]:


df.isnull().sum()


# In[22]:


df['Remarks'].unique()


# In[23]:


df['Origin State'].unique()


# In[24]:


df['When: Phase of flight'].unique()


# In[25]:


df['Aircraft: Type'].unique()


# In[17]:


df.columns


# In[18]:


df.size


# In[19]:


df.info()


# In[20]:


df1 = df.copy()


# In[21]:


df1


# In[26]:


df1.dropna(subset=['Aircraft: Type','Airport: Name', 'Altitude bin','Wildlife: Number struck','Effect: Impact to flight','FlightDate','Aircraft: Number of engines?','Aircraft: Airline/Operator','Origin State','When: Phase of flight','Wildlife: Size','Pilot warned of birds or wildlife?','Feet above ground','Is Aircraft Large?'],inplace=True)


# In[29]:


df1.isnull().sum()


# In[30]:


df1.describe()


# In[36]:


df1.drop(labels='Remarks', axis=1,inplace=True)


# In[37]:


df1.isnull().sum()


# In[38]:


df1


# In[50]:


df1.to_excel(r'C:\Users\Anurag\bird_strile_cleaned.xlsx',index = False)


# In[ ]:




