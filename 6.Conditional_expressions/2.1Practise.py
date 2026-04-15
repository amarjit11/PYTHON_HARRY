#1. Write a program to find the greatest of four numbers entered by the user.
a=int(input("Enter the number1: "))
b=int(input("Enter the number2: "))
c=int(input("Enter the number3: "))
d=int(input("Enter the number4: "))

if (a>b and a>c and a>d):
	print("greatest of them is:", a)
elif(b>a and b>c and b>d):
	print("greatest of them is:", b)
elif(c>a and c>b and c>d):
	print("greatest of them is:", c)
else:
	print("greatest of them is:", d)


