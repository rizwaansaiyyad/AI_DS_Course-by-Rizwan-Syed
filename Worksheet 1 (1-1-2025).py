#!/usr/bin/env python
# coding: utf-8

# In[ ]:


number = float(input("what is your age: "))

# Check if the number is positive, negative, or zero
if number > 18:
    print("you are eligable to drive.")
elif number < 18:
    print("You are not eligable to drive.")
else:
    print("putar chutti karo.")
    



# In[8]:


print (2023.2)


# In[9]:


#strings  text
#integar whole value
#float decimal point value

print (2023.2)


# In[40]:


#modulor is a value which is remaining value when we divide a value


# In[9]:


rizwan = "10"+"10"

print(rizwan)



# In[4]:


syed = "awaz do humko hum kho gaey"

print(syed)


# In[2]:


an = 2022 
print(an)


# In[20]:


rose = 2022
print(rose)


# In[22]:


Rose =2022
print(rose)


# In[24]:


my_name_khan  = 2024
print(my_name_khan)


# In[35]:


age =20
age +=20
print(age)


# In[3]:


ali = 200+200+200
print(ali)


# In[7]:


aas = 200 
print(aas)


# In[14]:


# Define a variable to store if the user is logged in
is_logged_in = False

# Use the boolean value to check login status
if is_logged_in:
    print("Welcome, you are logged in!")
else:					
    print("Please log in to continue.")


# In[18]:


x = 5.2        # Float
y = int(x) # Casting to Integar
print(y)     # Output: 5.0


# In[20]:


x = 5        # Integer
y = float(x) # Casting to float
print(y)     # Output: 5.0


# In[21]:


x = 10
y = str(x)   # Casting to string
print(y)     # Output: "10"


# In[22]:


x = "42"
y = int(x)   # Casting to integer
print(y)     # Output: 42


# In[23]:


x = "3.14"
y = float(x) # Casting to float
print(y)     # Output: 3.14


# In[32]:


ahmed = 220+220
print(ahmed)


# In[33]:


220+200-100*400/2


# In[38]:


12.2//13.5


# In[40]:


12%6


# In[43]:


12**2


# In[44]:


# Arithmetic Operators
a = 10
b = 5
print(a + b)  # Output: 15 (Addition)
print(a - b)  # Output: 5 (Subtraction)

# Comparison Operators
print(a == b)  # Output: False (Equal to)
print(a != b)  # Output: True  (Not equal to)
print(a > b)   # Output: True  (Greater than)

# Logical Operators
x = True
y = False
print(x and y)  # Output: False (Logical AND)
print(x or y)   # Output: True  (Logical OR)
print(not x)    # Output: False (Logical NOT)


# In[46]:


string1 = "Hello"
string2 = "World"
result = string1 + " " + string2  # Adding a space in between
print(result)  # Output: "Hello World"



# In[47]:


text = "Hello World"
slice1 = text[0:5]     # Slices from index 0 to 4
slice2 = text[6:]      # Slices from index 6 to the end
slice3 = text[:5]      # Slices from the beginning to index 4
print(slice1)  # Output: "Hello"
print(slice2)  # Output: "World"
print(slice3)  # Output: "Hello"


# In[48]:


text = "Hello World"
slice4 = text[-5:]    # Slices the last 5 characters
print(slice4)  # Output: "World"


# In[49]:


name = "John"
age = 30
formatted_string = f"My name is {name} and I am {age} years old."
print(formatted_string)  # Output: "My name is John and I am 30 years old."


# In[50]:


name = "Jane"
age = 25
formatted_string = "My name is {} and I am {} years old.".format(name, age)
print(formatted_string)  # Output: "My name is Jane and I am 25 years old."


# In[51]:


name = "Ali"
age = 28
formatted_string = "My name is %s and I am %d years old." % (name, age)
print(formatted_string)  # Output: "My name is Ali and I am 28 years old."


# In[54]:


#len(): Returns the length of a string.
text = "Hello"
print(len(text))  # Output: 5
#upper(): Converts all characters to uppercase.
text = "hello"
print(text.upper())  # Output: "HELLO"
#lower(): Converts all characters to lowercase.
text = "HELLO"
print(text.lower())  # Output: "hello"
#replace(): Replaces occurrences of a substring with another.
text = "Hello World"
new_text = text.replace("World", "Python")
print(new_text)  # Output: "Hello Python"
#strip(): Removes leading and trailing whitespace.
text = "  Hello  "
print(text.strip())  # Output: "Hello"


# In[ ]:




