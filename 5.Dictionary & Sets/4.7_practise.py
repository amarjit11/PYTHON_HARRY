# 7. If the names of 2 friends are same; what will happen to the program in problem 6?
# --->the last value will be assigned to key

d={}

name=input("enter the friend name: ")
lang=input("enter favorite language: ")
d.update({name:lang})
name=input("enter the friend name: ")
lang=input("enter favorite language: ")
d.update({name:lang})
name=input("enter the friend name: ")
lang=input("enter favorite language: ")
d.update({name:lang})
name=input("enter the friend name: ")
lang=input("enter favorite language: ")
d.update({name:lang})

print(d)