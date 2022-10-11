fileobj = open("C:\Python/test.txt")#default

fileobj = open("C:\Python/test.txt", 'r')#read mode

fileobj = open("C:\Python/test.txt", 'w')#write mode

fileobj = open("C:\Python/test.txt", 'a')#append mode

fileobj.close()#closing file

fileobj = open('C:/Python/test1.txt')#read file

print(fileobj.read())#reading whole file

#if you type again the print for reading complete file then it will not display the file because the cursor is in the end of the file

#bring the file to initial position
fileobj.seek(0)
print(fileobj.read())

#everytime need to place the cursor at the beginning after reading the file using seek menthod

#the number you mention in the brackets will be the position the file start to display.
fileobj.seek(7)
print(fileobj.read())

#to check limited output
fileobj.seek(0)
print(fileobj.read(22))

#to check the file cursor position
print(fileobj.tell())

#readline()-reads the line of the file
fileobj.seek(0)

print(fileobj.readline()) #reads first line

print(fileobj.readline()) #reads second line

#readlines() - read all lines of the file
fileobj.seek(0)
print(fileobj.readlines())

#read first 5 lines of a file using readlines()

fileobj.seek(0)
count=0
for i in fileobj.readlines():
    if(count<5):
        print(i)
    else:
        break
    count += 1

#----------------------------------------------
#Write file
fileobj1 = open('C:/Python/test2.txt', 'w')

#add content to existing file
fileobj1.write('This is the new content appended in the existing fle.')
fileobj1.close()

fileobj1=open('C:/Python/test2.txt', 'r')
print(fileobj1.read())

fileobj1.close()

#--------------------------------------

#open the file in append mode to add new data
fileobj2= open('C:/Python/test2.txt', 'a')
fileobj2.write('Open the file in append mode.add new.')
fileobj2.close()

fileobj2 = open('C:/Python/test2.txt', 'r')
print(fileobj2.read())
fileobj2.close()

#-------------------------------

#delete the file(cannot read again if deleted)
import os
os.remove("C:/Python/test2.txt")

#---------------------------------
#this is python code to take analogy of with()
with open('C:/Python/test.txt') as file:
    data = file.read()
with open('C:/Python/test.txt', "w") as file:
    file.write("Hello World")

#----------------------------------------------

#analogy for using split() function

with open("C:/Python/test.txt", "r") as file:
    data = file.readlines()
    for line in data:
        # splits each line sentence into words
        word = line.split()
        print(word)

