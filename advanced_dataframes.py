#!/usr/bin/env python
# coding: utf-8

# In[317]:


import pandas as pd
import numpy as np
import math
import matplotlib.pyplot as plt 


# In[2]:


from pydataset import data


# In[3]:


mpg = data('mpg')


# In[5]:


data('mpg', show_doc=True)


# In[6]:


mpg.head(5)


# In[10]:


mpg["average_per_gallon"] = (mpg['cty'] + mpg['hwy']) /2

mpg.head(1)


# In[42]:


mpg.groupby('manufacturer').average_per_gallon.mean().sort_values(ascending = False)


# In[43]:


# 1 Load the mpg dataset. Read the documentation for it, and use the data to answer these questions:

# On average, which manufacturer has the best miles per gallon?

mpg.groupby('manufacturer').average_per_gallon.agg('mean').sort_values( ascending = False)


# In[50]:


# How many different manufacturers are there?

man_list = mpg['manufacturer'].unique()

len(man_list)


# In[59]:


# How many different models are there?

model_list = mpg['model'].unique()
len(model_list)


# In[58]:


mpg.groupby('model').manufacturer.max().value_counts().sum()


# In[65]:


# Do automatic or manual cars have better miles per gallon?

mpg.groupby(['trans']).average_per_gallon.agg('mean').sort_values(ascending=False)

# Auto's carry the top two spots followed by a manual after.


# In[66]:


# 2 Joining and Merging

users = pd.DataFrame({
    'id': [1, 2, 3, 4, 5, 6],
    'name': ['bob', 'joe', 'sally', 'adam', 'jane', 'mike'],
    'role_id': [1, 2, 3, 3, np.nan, np.nan]
})
users


# In[67]:


roles = pd.DataFrame({
    'id': [1, 2, 3, 4],
    'name': ['admin', 'author', 'reviewer', 'commenter']
})
roles


# In[68]:


# Copy the users and roles dataframes from the examples above. What do you think a right join would look like? 
# An outer join? What happens if you drop the foreign keys from the dataframes and try to merge them?

pd.merge(users, roles, left_on='role_id', right_on='id', how='left') # everything on left included, only matching from right


# In[69]:


pd.merge(users, roles, left_on='role_id', right_on='id', how='right') # everything on right included, only matching from left


# In[70]:


pd.merge(users, roles, left_on='role_id', right_on='id', how='inner') # no null values


# In[71]:


pd.merge(users, roles, left_on='role_id', right_on='id', how='outer') # everything included


# In[79]:


pd.merge(users, roles, how='outer') # when foreign keys are dropped, name_x and name_y are no longer matched


# In[82]:


# 3 Getting data from SQL databases

# (a) Create a function named get_db_url. 
# It should accept a username, hostname, password, and database name and return a url formatted like in the examples in this lesson.

def get_db_url(database):
    from env import host, user, password
    url = f'mysql+pymysql://{user}:{password}@{host}/{database}'
    return url




# In[83]:


# (b) get connection to employees

pd.read_sql('SELECT * FROM employees LIMIT 5 OFFSET 50', get_db_url('employees'))


# In[ ]:


# (c) Once you have successfully run a query:
# Intentionally make a typo in the database url. What kind of error message do you see?

# Answer below

# OperationalError: (pymysql.err.OperationalError) 
# (1044, "Access denied for user 'easley_1264'@'%' to database 'employes'")

pd.read_sql('SELECT * FROM employees LIMIT 5 OFFSET 50', get_db_url('employes')) 


# In[ ]:


# (c) Intentionally make an error in your SQL query. What does the error message look like?

# ProgrammingError: (1064, "You have an error in your SQL syntax; 
# check the manual that corresponds to your MySQL server version for the right syntax to use 
# near '* FROM employees LIMIT 5 OFFSET 50' at line 1")

pd.read_sql('SELECT ** FROM employees LIMIT 5 OFFSET 50', get_db_url('employees'))


# In[108]:


# (d) Read the employees and titles tables into two separate dataframes



titles = pd.read_sql('SELECT * FROM titles;', get_db_url('employees'))

titles.head(5)


# In[99]:


employees = pd.read_sql('SELECT * FROM employees;', get_db_url('employees'))


# In[100]:


employees.head(5)


# In[106]:


current_employees = titles[titles.to_date == titles.to_date.max()]


# In[120]:


current_employees_with_titles = current_employees.groupby('title').emp_no.agg(['count'])


# In[321]:


current_employees_with_titles


# In[367]:


# (e) Visualize the number of employees with each title.


current_employees_with_titles.plot.barh(edgecolor='black', alpha=0.6, color='lime')

plt.grid(True, ls = ':')
plt.xlabel('# of Employees in Thousands', fontsize = 10)
plt.ylabel('Job Titles', fontsize = 10)
plt.title('Job Title Count')
plt.xticks([10_000, 20_000, 30_000, 40_000, 50_000, 60_000, 70_000, 80_000, 90_000], rotation = 45)

plt.show()


# In[336]:


# (f) Join the employees and titles dataframes together.

e_t = pd.merge(employees, titles, on='emp_no')

e_t


# In[199]:


# (g) Visualize how frequently employees change titles.

employees_change = titles[titles.to_date <= titles.to_date.max()]

title_changes = employees_change.groupby('emp_no').to_date.count().value_counts()

title_changes


# In[378]:



title_changes.plot.bar(edgecolor='black', alpha=0.6, color='pink')

plt.grid(True, ls = ':')
plt.xlabel('# of Title Changes', fontsize = 10)
plt.ylabel('# of Employees in Thousands', fontsize = 10)
plt.title('Job Title Changes')
plt.yticks([3_014, 137_256, 159_754], rotation = 45)
plt.xticks(rotation = 45)
plt.show()


# In[183]:


# (h) For each title, find the hire date of the employee that was hired most recently with that title.

current_hire = e_t.groupby('title').hire_date.agg(['max'])


current_hire


# In[205]:


# (i) Write the code necessary to create a cross tabulation of the number of titles by department. 
# (Hint: this will involve a combination of SQL and python/pandas code)


title_query = '''
select dept_name, title
from dept_emp
join titles using(emp_no)
join departments using(dept_no)
where titles.to_date > curdate()
and dept_emp.to_date > curdate();
'''

departments_and_titles = pd.read_sql(title_query, get_db_url('employees'))

pd.crosstab(departments_and_titles.dept_name, departments_and_titles.title)


# In[ ]:


# 4 Use your get_db_url function to help you explore the data from the chipotle database. 
# Use the data to answer the following questions:



# In[208]:


chipotle_orders = pd.read_sql('SELECT * FROM orders', get_db_url('chipotle'))


# In[211]:


chipotle_orders.head()


# In[316]:


# What is the total price for each order?

# .groupby(“order_id”).column_name.agg(“mean”)# .groupby(“order_id”).column_name.agg(“mean”) or 

working_price = chipotle_orders.assign(real_money = chipotle_orders['item_price'].str.strip('$').astype(float))

working_price = chipotle_orders.assign(total_price = working_price['quantity'] * working_price['real_money'])

working_price.head(10)


# In[301]:


# What are the most popular 3 items?

popular_items = chipotle_orders[['item_name', 'quantity']].sort_values(by='quantity', ascending=False).reset_index().head(3)


popular_items


# In[313]:


# Which item has produced the most revenue?

most_revenue = working_price[['item_name', 'quantity', 'total_price']].agg(['max'])

most_revenue


# In[ ]:




