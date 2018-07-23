a=1
b=2
c=1
print (id(a))
print (id(b))
print (id(c))

c=c+2;

print (id(a))
print (id(b))
print (id(c))

a=a+2
b=b+1

print (id(a))
print (id(b))
print (id(c))