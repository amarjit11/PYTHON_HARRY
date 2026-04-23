#1. Write a program using functions to find greatest of three numbers.

def greatest(a,b,c):
	if a>b and a>c:
		print(a)
	elif b>a and b>c:
		print(b)
	else:
		print(c)

a=int(input())
b=int(input())
c=int(input())
greatest(a,b,c)