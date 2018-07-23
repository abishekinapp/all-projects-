'''This is the program to search a element from a list using BINARY SEARCH method'''

#The list from which the element has to be  serched
a= input('enter the list from which the element has to be serched')

a=a.split(",") #The string entered is converted into list

a=sorted(a) #The list is sorted for doing binary sort

print('The list in accending order : ',a)

b=input('enter the element to be serched')#The element to be serched from the list is given as input

#Initialising parameters for doing BINARY SEARCH
l=len(a)
first=int(0)
last=int(l-1)
found=int(0)

#The BINARY SEARCH takes place inside this loop
while found==0:
    middle=int(last/2)
    if b==a[middle]:
        found=1
        print(b,' was found in the list a postion :', middle)
    if b>a[middle]:
        first = middle
    else:
        last=middle

    for i in range(first,last):
        if b==a[i]:
            print(b, ' was found in the list a postion :', i+1)
            found=1
