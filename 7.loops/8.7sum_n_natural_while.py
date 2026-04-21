#5. Write a program to find the sum of first n natural numbers using while loop.
n=int(input("enter the number"))

i=1
sum=0
while(i<n+1):
	sum=sum+i
	i+=1
print(f"sum of {n} natural number is {sum}")