a=input('enter the date in format dd/mm/yy')
months={1:'JAN',2:'FEB',3:'MAR',4:'APR',5:'MAY',6:'JUN',7:'JUL',8:'AUG',9:'SEPT',10:'OCT',11:'NOV',12:'DEC'}
b =a.split("-")
date=b[0]
for i in months:
    if int(b[1]) == i:
        month=months[i]
    else:
        continue
year="20"+b[2]
print(date," ",month,' ',year)