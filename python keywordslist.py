import keyword
print(keyword.kwlist)
print(len(keyword.kwlist))

#o/p - ['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']

#35 - 3.8.6 version contains


#identifiers
#False = 10
_var1 = 10
print(_var1)

_=20
print(_)

#sets
myset = {1,2,3,4,5,6,7 }
print(myset)

#length of the set
print(len(myset))

#duplicate elements are not allowed
myset = {1,2,2,3,4,5,6,6,6,7,8}
print(myset)

#set of float numbers
myset1= {1.78,2.08,3.56,4.77,5.45,6.23}
print(myset1)

#set of strings
myset2 = {'mickey','jerry','donald'}
print(myset2)

#mixed datatypes - sets are heterogeneous collection of datatypes
myset3 = {10,20, 'Hi Sets', (123.45,992233, 2345),('Aple','Banana','Grapes'), True ,False}
print(myset3)

#create an empty set
myset4 = set()
print(type(myset4))

myset5 = set(('one','two','three','four'))

for i in myset5:
    print(i)

#enumerate - returns item's index position & value

for i in enumerate(myset5):
    print(i)
    
