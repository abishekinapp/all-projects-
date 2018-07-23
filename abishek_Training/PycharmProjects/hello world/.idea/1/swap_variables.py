a=int(input("enter the first variable"))
b=int(input("enter the second variable"))
print("before swapping")
print("a= " , a , "& b= " , b)

a = a+b
b = a-b
a = a-b

print ("after swappint" )
print("a= " , a ,"& b= ", b)