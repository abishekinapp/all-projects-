import random

inp=open('scramble_input.txt','r+')
out=open('scramble_output.txt','r+')

read=inp.read().split()

def scramble(scr):

    l=len(scr)
    m = l - 1
    first=scr[0]
    last=scr[m]
    scr=list(scr)
    m_index=0
    middle=""
    for i in range (l-2):
        m_index=random.randint(1,(m-1))
        middle=middle+scr[m_index]
        scr.pop(m_index)
        m=m-1
    return (first+middle+last)

for i in read:
    if len(i) > 3:
                a = 1
    else:
        a = 0

    if a==1:
        b=scramble(i)

        out.write(b)
        out.write(" ")
    else:
         out.write(i)
         out.write(" ")
