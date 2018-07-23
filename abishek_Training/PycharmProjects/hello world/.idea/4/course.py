#course

abc=open('course_file.txt','r+')

course=abc.read()
someDict = {}
print(course)
course=list(course.split('\n'))
#print(course)

for i in range (0,len(course)):
    someDict[course[i]]=i
print(someDict)