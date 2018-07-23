#Importing the nessasary modules
import string
import random

#Funtion to generate random password
def generatepassword():
    lc = list(string.ascii_lowercase)
    uc = list(string.ascii_uppercase)
    n = list(string.digits)
    spl = '#,$,%,^,&,*'
    char = spl.split(',')
    password = []
    for i in range(0,3):
        password+=random.choice(lc) # random lowercase charecter is selected
        password+=random.choice(uc) # random uppercase charecter is selected
        password+= random.choice(n) # random digits charecter is selected
        password+= random.choice(char)# random special charecter is selected

    pas="".join(password) # joining all the selected elements in the password list
    return pas # The random password generated is returned


# This loop is used to produce a random password whenever the user asks
while True:
    new=input('Do u wish to generate a new password..[y/n] : ')
    if new=="y":
        password_new=generatepassword()
        print('The new password is ',password_new)

