#!/usr/bin/env python
# coding: utf-8

# zip() 函数用于将可迭代的对象作为参数，将对象中对应的元素打包成一个个元组，然后返回由这些元组组成的对象，这样做的好处是节约了不少的内存。
# 
# 我们可以使用 list() 转换来输出列表。
# 
# 如果各个迭代器的元素个数不一致，则返回列表长度与最短的对象相同，利用 * 号操作符，可以将元组解压为列表。

# In[7]:


a = [1,2,3]
b = [5,6,7]
zipped = zip(a,b)
zipped


# In[8]:


liste = list(zipped)
liste


# In[9]:


c = [7,8,9,10]
zipped2 = zip(a,c)


# 此处c比a多一项，被省去

# In[10]:


liste2 = list(zipped2)
liste2


# 解压方法

# In[13]:


a1, a2 = zip(*liste)


# In[14]:


a1 


# In[15]:


a2


# In[16]:


a1,a3 = zip(*liste2)


# In[17]:


a1


# In[18]:


a2


# 注意：此处a3与原来相比少了一项

# In[20]:


a3


# In[ ]:




