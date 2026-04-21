# 1. Write a program to print multiplication table of a given number using for loop.

'''num=int(input())
for i in range(num,(num*10+1),num):
	print(i)'''


num=int(input("enter the number "))

for i in range (1,11):
	print(f"{num} X {i} = {num*i}")