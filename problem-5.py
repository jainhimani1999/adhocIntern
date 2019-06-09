import datetime
name = input('USER NAME')
d = datetime.datetime.now()
if(d.hour>=6 and d.hour < 12):
    print(name+'GOOD MORNING')
elif(d.hour >=12 and d.hour<18):
    print(name+'GOOD NOON')
elif(d.hour >=18 and d.hour<21):
    print(name+'GOOD EVENING')
else:
    print(name+'GOOD NIGHT')    
