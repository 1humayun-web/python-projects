import random


target=random.randint(1,100)

while True:

   userchoice=input("enter number or quit the game:")
   if(userchoice=="quit"):
      break
   userchoice=int(userchoice)
   if(userchoice==target):
      print("succrs !True guess")
   elif(userchoice>target):
      print("the number is too large guess a smaller no")
   else:
      print("you guess a small no think of a bigger no")

print("__GAMEOVER__")  