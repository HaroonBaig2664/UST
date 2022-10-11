import os
import sys
try:
    os.remove("C:/Python/test3.txt")
except:
    print("Below Exception Occurred")
    print(sys.exc_info()[1])

else:
    print('No Excetion Occurred!')

finally:
    print('Run this block of code always.')

#-----------

try:
    x= int(input("Enter the first number:"))
    y= int(input("Enter the second number:"))
    print(x/y)
    os.remove("C:/Python/test3.txt")

except NameError:
    print('NameError exception occurred')

except FileNotFoundError:
    print('FileNotFoundError exception occurred')

except ZeroDivisionError:
    print('ZeroDivisionError exception occurred')
    
