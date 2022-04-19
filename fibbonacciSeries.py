#!/usr/bin/env python
# coding: utf-8

# In[1]:


N=int(input("Number of elements in fibbonacci series,N,N>=2:"))


# In[4]:


#Initializing the list with starting elements 0,1
fibbonacciSeries=[0,1]


# In[5]:


if N>2:
    for i in range(2,N):
        #next element in series=sum of previous two numbers
        nextElement=fibbonacciSeries[i-1]+fibbonacciSeries[i-2]
        #append the element to the series
        fibbonacciSeries.append(nextElement)
        


# In[6]:


print(fibbonacciSeries)


# In[ ]:





# In[ ]:




