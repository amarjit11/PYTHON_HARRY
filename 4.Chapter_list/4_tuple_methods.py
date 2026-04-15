#a=(1)		# type int
#a=(1,)		# type tuple
a=(1,34,45,54,53354,"Rohan",45,"shivam") #tuple is immutable list is mutable
#print(type(a))
print(a)
no=a.count(45)
i=a.index(53354)
len=len(a)
print("Length of this tuple is ",len)
print("index number of this element in this tuple is",i)
result=tuple(x for x in a if isinstance(x,int))
print(result)
print(max(result))
# slicing gives a new tuple
sliced= a[0:5]
print(sliced)

#unpacking gives variable to elements inside tuple

b,c,d,e,f,g,h,i=a
print(b,c,d,e,f,g,h,i)