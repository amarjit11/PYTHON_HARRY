#6. Write a program to calculate the factorial of a given number using for loop.

n=int(input("enter the number : "))

factorial=1
for i in range(1,n+1):
	factorial*=i
print(factorial)
