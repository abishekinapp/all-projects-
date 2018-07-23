import string
def check():
    password = input('enter the password')
    passlen=len(password)
    lc= string.ascii_lowercase
    uc= string.ascii_uppercase
    n= string.digits
    spl='$#@'
    count=int(0)
    if passlen in range (6,12):
        if not any((c in lc) for c in password):
            print('..lowercase..')
            count+=1
        if not any((c in uc) for c in password):
            print('..uppercase.. ')
            count += 1
        if not any((c in n) for c in password):
            print('..number.. ')
            count += 1
        if not any((c in spl) for c in password):
            print('..$#@..')
            count += 1

        while count > 0:
            print('the above mentioned are on present....enter atleast one charecter of the mentioned above')
            check()
    else:
        print('the passwords must be betwwen the length 6-12 charecters')
        check()

check()

