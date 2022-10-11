import sys
try:
    print(100/0) # zerodivisionerror
except:
    print(sys.exc_info()[1], 'Exception occurred') #this statement will be executed only if exception error occurs
else:
    print('No exception occured!!')
finally:
    print('Run this block of code always')# this statement will be executed always
