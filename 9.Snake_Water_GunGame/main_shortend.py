#PROJECT 1: SNAKE, WATER, GUN GAME
#We all have played snake, water gun game in our childhood. If you haven’t, google the rules of this game and write a python program capable of playing this game with the user
import random
'''
1 for snake
-1 for water
0 for gun
'''
computer= random.choice([0,-1,1])
mystr=input("entering my choice: w s g\n")
mydict={"s":1, "w":-1,"g":0}
reversedict={1:"snake",-1:"water",0:"gun"}

me=mydict[mystr]
print(f"Me chose: {reversedict[me]}\nComputer chose: {reversedict[computer]}")

if (computer==me):
	print("It's a Draw")
	
	
if(computer-me==1 or computer -me== -2):
	print("you win")
if(computer-me==-1 or computer -me== 2):
	print("you lose")


