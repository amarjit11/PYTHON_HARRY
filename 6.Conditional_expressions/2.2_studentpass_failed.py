
s1=int(input("enter the marks: "))
s2=int(input("enter the marks: "))
s3=int(input("enter the marks: "))
marks= (s1+s2+s3)/3
if marks>=40:
	if(s1>33 and s2>33 and s3>33):
		print("student has passed the exam")
else:
	print("student has failed the exam")