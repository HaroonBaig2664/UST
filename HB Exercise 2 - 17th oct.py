#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from genericpath import exists

import os

add_location = input(r"")

# add_loc = ''.join(('r',add_location))

# print(add_loc)
file_name = 'demofile.txt'
pathh = os.path.join(add_location,file_name)
if os.path.exists(pathh):
    os.remove(pathh)
    print("%s has been removed successfully" %file_name)
else:
    print("files doesnt exists")  


# In[ ]:




