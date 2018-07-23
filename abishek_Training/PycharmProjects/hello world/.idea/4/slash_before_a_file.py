#put slash befor ' a '

abc = open('hello.txt','r+')
sentence    = abc.read()
print(sentence)
print(sentence.replace("a","/a"))