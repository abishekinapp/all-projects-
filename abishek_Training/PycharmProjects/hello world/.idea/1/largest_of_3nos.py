a=int(input("enter the 1st number"))
b=int(input('enter the 2nd number'))
c=int(input('enter the 3rd number'))
if a>b and a>c:
    print('the largest number is ',a)
elif b>a and b>c :
    print('the largest number is ' , b)
else:
    print('the largest number is ' ,c)