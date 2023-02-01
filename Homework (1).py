#!/usr/bin/env python
# coding: utf-8

# ## Data Types and Variables

# ### Integer
# - A whole number that is not a decimal, can go on forever

# ### Floating Point
# - Decimal number, used for precision. 

# ### String
# - A sequence of characters. 
# - A single character is a string with a length of 1

# ## What data type is each value? Use the type function to verify.

# In[2]:


type(3)


# In[3]:


type(6.0)


# In[4]:


type("3.14159")


# In[5]:


type(4.5)


# In[6]:


type("hello")


# In[11]:


type("math.pi")


# ## math.pi is a module

# ## Use the type function to identify the data type of each result. Are there any that do not work?

# In[17]:


print(3+7)


# In[18]:


type(10)


# In[14]:


print("Py" + "thon")


# In[16]:


type("Python")


# In[19]:


print(5 + 6.0)


# In[20]:


type(11.0)


# In[21]:


print(6.0 // 3.0)


# In[22]:


type(2.0)


# ### print("High" + 5)  - Produces an Error. Can not Concat 

# ### Which variable names are acceptable, and which are not? If a variable name is unacceptable, explain why. 
# 

# #### Acceptable
# - num
# - AGE
# - lambda
# - FiRsTnAmE
# - card_2
# - _count

# #### Not Acceptable
# - card 2
# - 2nd_card
# 

# In[30]:


var = "AGE"


# In[31]:


print(var)


# ### Choose a meaningful variable name to represent each scenario.
# 

# 1. The number of cards dealt to a player.  
# - num_player_cards
# 2. An employee's monthly salary.
# - emp_month_sal
# 3. The sum of the values rolled by two dice.
# - sum_val_dice
# 4. The temperature on a hot summer day.
# - temp_summer_hot

# #### Assign the values x="house", y="boat" and z="ha". What is the result of each statement? Which do not work, and why?
# 

# In[32]:


x = "house"
y = "boat"
z = "ha"


# 1. x+y
# 2. y+x
# 3. z*3
# 4. z*x
# 5. x+2
# 6. y+"2"

# In[33]:


print(x + y)


# In[34]:


print(y + x)


# In[35]:


print(z * 3)


# #### Can not join. The 2 needs to be in quotes to make it a string. 
# print(x + 2)  

# In[37]:


print(y + "2")


# #### Assign the values base=10 and height=5. Calculate the area of a triangle using the formula
# #### Area = 0.5(b)(h) , and assign the value to the variable area. Echo this value.

# In[38]:


b = 10
h = 5
Area = (0.5 * b * h)


# In[39]:


print(Area)


# #### Execute the following sequence of commands in the shell, then state the final value of k.

# In[40]:


k = 7


# In[41]:


k += 3


# In[42]:


print(k)


# In[43]:


k *= 2
print(k)


# In[44]:


k -= 5
print(k)


# In[45]:


k //= 6
print(k)


# #### Explain why the following run-time error occurs.
# >>> number = 8
# >>> Number += 1
# Traceback (most recent call last):
#  File "<pyshell>", line 1, in <module>
# NameError: name 'Number' is not defined

# ### number and Number are two different variables. Number is not defined. 

# #### Python is a dynamically-typed language: a variable’s data type can change as necessary. Assign the
# #### value x=4, then use check its type using the type function. What data type is it? Increment x by 1,
# #### using the += operator, then check its type again. Did it change? If so, what data type is it?
# #### Increment x by 1.0, then check its type. Did it change? If so, what data type is it?
# 
# 
# ## X remained an integer until the decimal increment. It became a float. 

# In[46]:


x = 4


# In[47]:


type(4)


# In[53]:


x = 4
x += 1
print(x)


# In[54]:


type(5)


# In[55]:


x = 4
x =+ 1.0
print(x)


# In[56]:


type(x)


# In[ ]:




