import datetime
k=input('Enter your name')
l = int(input('Enter your age'))
now = datetime.datetime.now()
print(k +'will turn 95 by the year :'+ str((95-l)+now.year))
