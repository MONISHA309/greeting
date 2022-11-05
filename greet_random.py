#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# greet_random
from random import randint
def greet_random():
    n=0
    greetings=["hi","hey","hello","vanakam"]
    n=randint(0,len(greetings)-1)
    return(greetings[n])
# print a random greeting
greeting = greet_random()
print(greeting)


quit_msg=["quit","bye","exit"]
greeting = greet_random()
print(greeting, ',', "i am a coalbot. can do simple calculations for you")
while True:
    msg = input()
    if msg in quit_msg:
        break
    elif "add" in msg:
        print(msg)
        split_msg=msg.split()
        print(split_msg)
        p1=float(split_msg[1])
        p2=float(split_msg[2])
        print(p1+p2)
    elif "mul":
        split_msg=msg.split()
        print(split_msg)
        p1=float(split_msg[1])
        


# In[ ]:





# In[ ]:




