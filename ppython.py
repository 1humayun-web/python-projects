import random 
import os

respect=random.randint (1,6)
 
while True:

    userchoice=input("enter number or foff")

    if(userchoice=="foff"):
         print("over") 
         break
    userchoice=int(userchoice)
    if (userchoice==respect):
         print("hello world")
    else:
         print("no helllo world")      
