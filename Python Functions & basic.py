#!/usr/bin/env python
# coding: utf-8

# In[1]:


var1 = 100 #variable with global scope
# define a function
def myfunc():
    print(var1)
    
myfunc()
print(var1)


# In[2]:


def func1():
    var2 = 100
    print(var2) #variable with local scope
    
def myfunc2():
    print(var2) # will throw error bcz of var2 has a local scope 
    
# Call a function
myfunc1()
myfunc2()


# In[9]:


var1 = 100
def myfunc():
    var1 = 90
    return var1
    
print(myfunc())
print(var1)


# In[10]:


var1 = 100
def myfunc():
    var1 = var1 + 10
    print(var1)
    
myfunc()
print(var1 + 100)


# In[11]:


# args & kwargs
def summation(a,b,c):
    return a+b+c
print(summation(10, 20, 30))


# In[12]:


def summation(*args):
    return sum(args)

print(summation(10,11)) #sum of 2 args
print(summation(10,15,20))
print(summation(10,20,30,40))
print(summation(10,20,30,40,50))


# In[1]:


def summation(*args):
    return sum(args)

list_1 = [10,20,30,40,50,60,70]

print(summation(*list_1))


# In[3]:


def summation(*args):
    return sum(args)

list_1 = [10,20,30,40,50,60,70]
tuple1 = (10,20,30,40,50,60,70)

print(summation(*list_1))
print(summation(*tuple1))


# In[4]:


list_1 = [10,20,30,40,50,60,70]
list_2 = [10,20,30,40,50,60]
list_3 = [1,2,3,4,5,6,7]
list_4 = [10,11,12,13,14,15]

summation(*list_1, *list_2, *list_3, *list_4)


# In[5]:


def userdetails (*args):
    print(args)
    
userdetails('Pooja',76112, 110088, 24, 'India', 'English')

'''
For the above examples we have no idea about parameters passed. In such case we can use key worded arguments(*kwargs)
'''


# In[7]:


def userdetails(**kwargs):
    print(kwargs)
    
userdetails(Name ='Pooja', ID = 76112, Pincode=110088, Age = 24, Country ='India', Language = 'English')


# In[10]:


def userdetails(**kwargs):
    for key, value in kwargs.items():
        print("{}: {}".format(key,value))


# In[11]:


userdetails(Name = 'Pooja', ID = 76112, Pincode = 110088, Age = 24, Country = 'India', Language = 'English')


# # Write a program that takes user details , *args, **kwargs, and default values.

# In[16]:


def userdetails(licenseNo, *args, contact=0, **kwargs):
    print('License No. : ',licenseNo)
    j = ''
    for i in args:
        j = j + i
        print('Full name : ',j)
        print('phone Number : ',contact)
    
    for key, val in kwargs.items():
        print("{} : {}".format(key,val))
    
name = ['Haroon','Baig']
mydict ={'Name' : 'Haroon', 'ID': 191569, 'Pincode':110001, 'Age':26, "Country":'India'}
userdetails('DLT2022', *name, contact = 9845448747, **mydict)


# Lambda , Filter , Map and reduce

# In[17]:


addition = lambda a: a + 10
print(addition(10))


# In[18]:


product = lambda a,b : a*b
print(product(10,15))


# In[19]:


result = (lambda *args :sum(args))
result(10,20), result(10,20,30,40), result(10,20,30,40,50,60)


# In[20]:


#filter
list_1 = [1,2,3,4,5,6,7,8,9]

def odd(n):
    if n%2 ==1:
        return True
    else:
        return False


# In[21]:


oddnum = list(filter(odd,list_1))
oddnum


# In[23]:


odd_num = list(filter(lambda num : num%2 == 1, list_1))
odd_num


# In[24]:


def twice(num):
    return num*2
doubles = list(map(twice,odd_num))
doubles     


# In[25]:


doubles = list(map(lambda num : num*2, odd_num))
doubles


# In[26]:


from functools import reduce

def summation(a,b):
    return a+b

sum_all = reduce(summation,doubles)
sum_all
    


# In[36]:


sum_all = reduce(lambda a,b:a+b,doubles)
sum_all


# In[37]:


list1 = [22,34,54,21,22,42,11,2,34,6667,8,89]




eve = list(filter(lambda a : a % 2 == 0, list1))



print(eve)


# In[38]:


sum_all = reduce(lambda a, b : a + b, list(map(lambda num : num ** 3, list(filter(lambda num : num % 2 == 0, list_1)))))
sum_all


# In[39]:


list_2 = [1,2,3,4,5]

min_list = reduce(lambda a,b : a if a<b else b, list_2)


# In[40]:


print(min_list)


# In[41]:


#max number in the list
max_list = reduce(lambda a,b : a if a>b else b, list_2)
max_list


# In[43]:


#frozenset() method
list_1 = ['Apple','Banan','grapes','vanilla']
frozenset(list_1)


# In[44]:


fsets.add('eclairs')


# In[45]:


#random dictionary
person = {"name":"Baig","salary":50000,"gender":"Male"}
fsets = frozenset(person)
print(fsets)


# In[46]:


#frozenset operations

A = frozenset([10,20,30])
B = frozenset([20,30,40,50])

#copying a frozenset
c = A.copy()
print(c)


# In[47]:


#uninon

A.union(B)


# In[48]:


#intersection

A.intersection(B)


# In[49]:


python_libs = ['python','math','numpy','pandas','datetime','sys']

upper_python_libs = []

for lib in python_libs:
    upper_python_libs.append(lib.upper())
    
print(upper_python_libs)


# In[52]:


python_libs = ['python','math','numpy','pandas','datetime','sys']

upper_python_libs = list(map(str.upper ,python_libs))
upper_python_libs


# In[53]:


#palindrome
mylist = ['php', 'madam','python','numpy','class','rewire','salas']



palindromed_list =[]

for i in mylist:

    temp = i

    temp1 = temp[::-1]



    if temp == temp1:

        palindromed_list.append(temp1)





print(palindromed_list)


# In[56]:


#palindrome
mylist = ['php', 'madam','python','numpy','class','rewire','salas']
result = list(filter(lambda x: (x == "".join(reversed(x))), mylist))
print(palindromed_list)


# In[61]:


#program to read file from the poem and scan it to search star

file = open('poem.txt','r')
text = file.read()
if 'star' in text:
    print('star is present')
else:
    print('star is not present')
file.close()


# In[ ]:


# Create a game of Snake Water Gun using Python

# Import random module
import random
print('Snake - Water - Gun')


# Input no. of rounds
n = int(input('Enter number of rounds: '))


# List containing Snake(s), Water(w), Gun(g)
options = ['s', 'w', 'g']

# Round numbers
rounds = 1

# Count of computer wins
comp_win = 0

# Count of player wins
user_win = 0


# There will be n rounds of game
while rounds <= n:

	# Display round
	print(f"Round :{rounds}\nSnake - 's'\nWater - 'w'\nGun - 'g'")

	# Exception handling
	try:
		player = input("Choose your option: ")
	except EOFError as e:
		print(e)

	# Control of bad inputs
	if player != 's' and player != 'w' and player != 'g':
		print("Invalid input, try again\n")
		continue

	# random.choice() will randomly choose
	# item from list- options
	computer = random.choice(options)

	# Conditions based on the game rule
	if computer == 's':
		if player == 'w':
			comp_win += 1
		elif player == 'g':
			user_win += 1

	elif computer == 'w':
		if player == 'g':
			comp_win += 1
		elif player == 's':
			user_win += 1

	elif computer == 'g':
		if player == 's':
			comp_win += 1
		elif player == 'w':
			user_win += 1

	# Announce winner of every round
	if user_win > comp_win:
		print(f"You Won round {rounds}\n")
	elif comp_win > user_win:
		print(f"Computer Won round {rounds}\n")
	else:
		print("Draw!!\n")

	rounds += 1


# Final winner based on the number of wons
if user_win > comp_win:
	print("Congratulations!! You Won")
elif comp_win > user_win:
	print("You lose!!")
else:
	print("Match Draw!!")


# In[ ]:




