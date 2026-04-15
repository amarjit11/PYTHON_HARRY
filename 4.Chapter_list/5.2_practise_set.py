#Write a program to accept marks of 6 students and display them in a sorted manner.
'''
Marks=[]

student1=int(input("enter the marks"))
Marks.append(student1)
student2=int(input("enter the marks"))
Marks.append(student2)
student3=int(input("enter the marks"))
Marks.append(student3)
student4=int(input("enter the marks"))
Marks.append(student4)
student5=int(input("enter the marks"))
Marks.append(student5)
student6=int(input("enter the marks"))
Marks.append(student6)


Marks.sort()
print(Marks)'''

# using for lloop

marks=[]

for i in range(7):
	m=int(input(f"enter the marks of student {i+1}"))
	marks.append(m)
marks.sort()
print(marks)