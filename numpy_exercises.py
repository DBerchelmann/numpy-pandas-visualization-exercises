#!/usr/bin/env python
# coding: utf-8

# In[15]:


import numpy as np


# In[16]:


import math


# In[17]:


import random


# In[18]:


import matplotlib.pyplot as plt


# In[19]:


import pandas as pd


# In[22]:


a = np.array([4, 10, 12, 23, -2, -1, 0, 0, 0, -6, 3, -7])


# In[23]:


# 1 How many negative numbers are there?

print('Here are the negative numbers: {}'.format(a[a < 0]))

print('The count is: {}'.format(len(a[a < 0])))  #use len to do a count, set up of evaluating array is the same


# In[39]:


get_ipython().run_cell_magic('time', '', "\n# 2 How many positive numbers are there?\n\nprint('Here are the positive numbers in the array: {}'.format(a[a > 0]))\n\nprint('The count is: {}'.format(len(a[a >0]))) # using a conditional to evaluate a one-dimensional array\n")


# In[41]:


get_ipython().run_cell_magic('time', '', "# 3 How many even positive numbers are there?\n\n\npos_nums = (a[a > 0])\n\nnew_list = np.array([pos_nums])\n\npos_evens = new_list[new_list % 2 == 0]\n\n\n\nprint('Here is the list of positive/even numbers in the array: {}'.format(pos_evens))\nprint('The count of positive/even number in the arrary is: {}'.format(len(pos_evens)))")


# In[26]:


# 4 If you were to add 3 to each data point, how many positive numbers would there be?

vaa = a + 3

# print(vaa)


new_pos_nums = (vaa[vaa > 0])

# print(new_pos_nums)

newest_list = np.array([new_pos_nums])

# print(newest_list)

new_pos_evens = newest_list[newest_list % 2 == 0]

# print(new_pos_evens)
 
print('After adding 3 to each data point the new list looks like this: {}'.format(new_pos_evens))
print('The updated count of positive/even number in the arrary is still: {}'.format(len(new_pos_evens)))


# In[27]:


# 5 If you squared each number, what would the new mean and standard deviation be?
vaa = a ** 2

print('This is the array squared: {} '.format(vaa))

print('This is new mean. {} '.format(vaa.mean()))


print('This is the new standard deviation: {}'.format(vaa.std()))


# In[51]:


# 6 A common statistical operation on a dataset is centering. 
#   This means to adjust the data such that the mean of the data is 0. 
#   This is done by subtracting the mean from each data point. 
#   Center the data set. 

# a.mean() is 3

a_mean = a.mean()
print(a_mean)

centered_variables = a - a_mean

centered_variables


# In[67]:


# 7 Calculate the z-score for each data point.

# variable - population mean

new_vars = a - a.mean() # [  1.   7.   9.  20.  -5.  -4.  -3.  -3.  -3.  -9.   0. -10.]

print(new_vars)

a.std()
print(a.std()) # 8.06225

z_score = new_vars / a.std()

print('the z_score is : {}'.format(z_score))


# In[ ]:


# Life w/o numpy to life with numpy


# In[116]:


import math

a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Exercise 1 - Make a variable called sum_of_a to hold the sum of all the numbers in above list

sum_of_a = 0
for n in a:
    sum_of_a += n

# Exercise 2 - Make a variable named min_of_a to hold the minimum of all the numbers in the above list

min_of_a = min(a)

# Exercise 3 - Make a variable named max_of_a to hold the max number of all the numbers in the above list

max_of_a = max(a)

# Exercise 4 - Make a variable named mean_of_a to hold the average of all the numbers in the above list

mean_of_a = sum_of_a / len(a)

# Exercise 5 - Make a variable named product_of_a to hold the product of multiplying all the numbers in the above list together


product_of_a = [math.prod(a[:pos]) for pos in range(1, len(a) + 1)]

product_of_a = math.prod(a)



# Exercise 6 - Make a variable named squares_of_a. It should hold each number in a squared like [1, 4, 9, 16, 25...]


squares_of_a = [number ** 2 for number in a]

# Exercise 7 - Make a variable named odds_in_a. It should hold only the odd number

odds_in_a = [number for number in a if number % 2 == 1]

# Exercise 8 - Make a variable named evens_in_a. It should hold only the evens.

evens_in_a = [number for number in a if number % 2 == 0]


# In[149]:


## What about life in two dimensions? A list of lists is matrix, a table, a spreadsheet, a chessboard...
## Setup 2: Consider what it would take to find the sum, min, max, average, sum, product, and list of squares for this list of two lists.

b = [
    [3, 4, 5],
    [6, 7, 8]
]

# Exercise 1 - refactor the following to use numpy. Use sum_of_b as the variable. **Hint, you'll first need to make sure that the "b" variable is a numpy array**


sum_of_b = np.array(b)

sum_of_b.sum()


# In[152]:


# Exercise 2 - refactor the following to use numpy. 
min_of_b = min(b[0]) if min(b[0]) <= min(b[1]) else min(b[1])  
b = np.array(b)
b.min()


# In[153]:


# Exercise 3 - refactor the following maximum calculation to find the answer with numpy.
max_of_b = max(b[0]) if max(b[0]) >= max(b[1]) else max(b[1])

b.max()


# In[154]:


# Exercise 4 - refactor the following using numpy to find the mean of b
mean_of_b = (sum(b[0]) + sum(b[1])) / (len(b[0]) + len(b[1]))

b.mean()


# In[156]:


# Exercise 5 - refactor the following to use numpy for calculating the product of all numbers multiplied together.
product_of_b = 1
for row in b:
    for number in row:
        product_of_b *= number
        
b.prod()


# In[158]:


# Exercise 6 - refactor the following to use numpy to find the list of squares 
squares_of_b = []
for row in b:
    for number in row:
        squares_of_b.append(number**2)
        
np.power(b, 2)


# In[162]:


# Exercise 7 - refactor using numpy to determine the odds_in_b
odds_in_b = []
for row in b:
    for number in row:
        if(number % 2 != 0):
            odds_in_b.append(number)
            
b[b % 2 == 1]


# In[163]:


# Exercise 8 - refactor the following to use numpy to filter only the even numbers
evens_in_b = []
for row in b:
    for number in row:
        if(number % 2 == 0):
            evens_in_b.append(number)

b[b % 2 == 0]


# In[164]:


# Exercise 9 - print out the shape of the array b.

b.shape # this shows (rows, columns) in an array


# In[181]:


# Exercise 10 - transpose the array b.

np.transpose(b)


# In[171]:


# Exercise 11 - reshape the array b to be a single list of 6 numbers. (1 x 6)

b.shape = (1, 6) # reformats the matrix to be 1 row with 6 columns


# In[173]:


# Exercise 12 - reshape the array b to be a list of 6 lists, each containing only 1 number (6 x 1)

b.shape = (6, 1) # this shapes the matrix into 6 row(lists) and 1 column


# In[175]:


## Setup 3
c = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

c = np.array(c)


# In[177]:


# Exercise 1 - Find the min, max, sum, and product of c.

c.min(), c.max(), c.sum(), c.prod()


# In[178]:


# Exercise 2 - Determine the standard deviation of c.

c.std()


# In[179]:


# Exercise 3 - Determine the variance of c.

np.var(c)


# In[184]:


# Exercise 4 - Print out the shape of the array c

c.shape
print(c.shape)


# In[183]:


# Exercise 5 - Transpose c and print out transposed result.

np.transpose(c)
print(np.transpose(c))


# In[186]:


# Exercise 6 - Get the dot product of the array c with c. 

np.dot(c, c)


# In[189]:


# Exercise 7 - Write the code necessary to sum up the result of c times c transposed. Answer should be 261

c_product = (c) * np.transpose(c)

c_product.sum() 


# In[191]:


# Exercise 8 - Write the code necessary to determine the product of c times c transposed. Answer should be 131681894400.

np.prod(c_product)

# answer is 131681894400


# In[192]:


## Setup 4
d = [
    [90, 30, 45, 0, 120, 180],
    [45, -90, -30, 270, 90, 0],
    [60, 45, -45, 90, -45, 180]
]

d = np.array(d)


# In[193]:


type(d)


# In[194]:


d.shape


# In[196]:


# Exercise 1 - Find the sine of all the numbers in d

np.sin(d)


# In[197]:


# Exercise 2 - Find the cosine of all the numbers in d

np.cos(d)


# In[198]:


# Exercise 3 - Find the tangent of all the numbers in d

np.tan(d)


# In[200]:


# Exercise 4 - Find all the negative numbers in d

d[d < 0]


# In[201]:


# Exercise 5 - Find all the positive numbers in d

d[d > 0]


# In[202]:


# Exercise 6 - Return an array of only the unique numbers in d.

np.unique(d)


# In[203]:


# Exercise 7 - Determine how many unique numbers there are in d.

len(np.unique(d))


# In[204]:


# Exercise 8 - Print out the shape of d.

d.shape


# In[206]:


# Exercise 9 - Transpose and then print out the shape of d.

np.transpose(d)

print(np.transpose(d))


# In[209]:


# Exercise 10 - Reshape d into an array of 9 x 2

d.shape = (9, 2)

print(d)


# In[ ]:




