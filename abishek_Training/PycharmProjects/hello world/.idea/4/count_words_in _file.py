#count words in a file

from collections import Counter
abc=open('countword.txt','r+')

a=abc.read().split()
print(a)
print(Counter(a))