a=input('enter the set of words , seperate the words by "," ')
b=a.split(',')
print('List with duplicate elements: ', a)

c = list(set(b))

print(" ".join(c))