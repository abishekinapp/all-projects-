import random

words=["tokyo","delhi","paris","miami"]
selected = random.choice(words)
print(selected)
fill=['-','-','-','-','-']
indexlist=[]

for c in selected:
    b=selected.index(c)
    indexlist.append(b)

listed = list(selected)

dictionary = dict()
for i in listed:
    if i in dictionary:
        dictionary[i] += 1
    else:
        dictionary[i] = 1

count=int(0)
#print(dictionary)
#print(count)
#print(sorted(dictionary,key=selected.index))
dictionary1=sorted(dictionary,key=selected.index)
for i in range (0,5):
    a=input('enter the charecter')
    #print(list(dictionary).index(a))
    if a in selected:
        print('the the charecter is present in the word')
        count=count+dictionary[a]
        print("only ", 4 - i, 'chances left')

        for d in range (0,5):
            if indexlist[d] == list(dictionary1).index(a):
                fill[d]=a;


        print(fill)

    else :
        print('the charecter ',a,' is not present in the word...!!! TRY AGAIN')
        print("only ",4-i,'chances left')
    if count==5:
        print('you WON the game.!!.. The word is ' ,selected)
        break
    if i==4:
        print('your chances are over')
        break
print ('game over')
