#!/usr/bin/env python
# coding: utf-8

# # write 20 methods that are used in python with examples

# In[4]:


#append() - Adds an element to the end of the list.

#Example code

my_list = [4, 8, 12]
my_list.append(16)
print(my_list)  


# In[5]:


#pop() - Removes and returns the last element from the list.

# Example code

my_list = [4, 8, 12, 16]
last_element = my_list.pop()
print(last_element)


# In[3]:


#sort() - Sorts the list in ascending order.

# Example code

numbers = [7, 1, 4, 1, 4, 9, 11]
numbers.sort()
print(numbers) 


# In[6]:


#reverse() - Reverses the order of elements in the list.

# Example code

my_list = [4, 8, 12, 16]
my_list.reverse()
print(my_list)


# In[7]:


#split() - Splits a string into a list based on a specified delimiter.

#Example code

sentence = 'Hello World'
words = sentence.split()
print(words)


# In[8]:


#capitalize() - Converts the first character of a string to uppercase.

# Example code

word = 'charity'
capitalized_word = word.capitalize()
print(capitalized_word)


# In[16]:


#index() - Returns the index of the first occurrence of a value in an object eg list, tuple.

# Example code

my_tuple = (2, 4, 6, 8, 10)
index_of_4 = my_tuple.index(4)
print(index_of_4)


# In[17]:


#count() - Returns the number of occurrences of a value in an object eg list, tuple.

# Example code

my_tuple = (2, 4, 6, 8, 10, 4)
count_of_4 = my_tuple.count(4)
print(count_of_4)


# In[11]:


#len() - Returns the length of an object eg tuple, list.

#Example code

my_tuple = (10, 20, 30, 40)
length = len(my_tuple)
print(length)  


# In[18]:


# get() - Returns the value for a specified key, or a default value if the key is not present.

#example code

my_dict = {'name': 'Ada', 'age': 31}
age = my_dict.get('age', 0)
print(age)  


# In[19]:


# keys() - Returns a list of all keys in the dictionary.

#example code

my_dict = {'name': 'Ada', 'age': 21}
keys_list = list(my_dict.keys())
print(keys_list)  


# In[20]:


# values() - Returns a list of all values in the dictionary.

#example code

my_dict = {'name': 'Ada', 'age': 31}
values_list = list(my_dict.values())
print(values_list)  


# In[21]:


# items() - Returns a list of key-value pairs (tuples) in the dictionary.

#example code

my_dict = {'name': 'Ada', 'age': 31}
items_list = list(my_dict.items())
print(items_list)


# In[22]:


#upper() - Converts the string to uppercase.

#example code

word = 'technology'
upper_word = word.upper()
print(upper_word)  


# In[23]:


#lower() - Converts the string to lowercase.

#example code

word = 'TECHNOLOGY'
lower_word = word.lower()
print(lower_word)  


# In[24]:


#replace() - Replaces occurrences of a substring with another substring.

#example code

sentence = 'Hello, World!'
new_sentence = sentence.replace('Hello', 'Ndewo')
print(new_sentence)  


# In[25]:


#add() - Adds an element to the set.

#example code

my_set = {1, 2, 3}
my_set.add(4)
print(my_set)  


# In[26]:


#remove() - Removes a specified element from the set.

#example code

my_set = {1, 2, 3, 4}
my_set.remove(3)
print(my_set)  


# In[27]:


#update(other_dict) - Updates the dictionary with elements from another dictionary or from an iterable of key-value pairs.

#example code

my_dict = {'name': 'Ada', 'age': 25}
my_dict.update({'city': 'Makurdi', 'age': 26})
print(my_dict)


# In[29]:


#clear() - Removes all items from the dictionary.

#example code

my_dict = {'name': 'Alice', 'age': 25}
my_dict.clear()


# In[ ]:




