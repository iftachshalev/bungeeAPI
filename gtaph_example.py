#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import matplotlib.pyplot as plt


# In[5]:


a = np.arange(10)
b = a**2
plt.plot(b)
# plt.show()

# In[7]:


plt.scatter(a,b)


# In[9]:


names = ['nadav','iftach', 'biga', 'ama']
players = [4,2,7,5]
plt.bar(names,players)

