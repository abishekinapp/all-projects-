n= int(input("input the number whoes sum is to be calculated"))
sum =0
while n>0:
    r=int(n%10)
    sum=sum+r
    n=int(n/10)
print("the sum of the numers are " , sum)