#4. Write a recursive function to calculate the sum of first n natural numbers.

'''
sum(1)=1
sum(2)=2+1

sum(n)=n+sum(n-1)
'''

def sum(n):
	if (n==1):
		return 1
	return n+sum(n-1)

n=int(input())
print(sum(n))