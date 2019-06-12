import os
from shutil import which
#all the commands given by user either wrong or right must be store in a file
location=input('Enter the location of file in which data must be stored')
file=open(location,"a")
command=input('Enter the command')
file.write(command)
# output of success command will be shown to monitor
if(which(command)):
    print('sucsess')
    os.system(command)
file.close()
fr=open(location,'r')
print(fr.read())
fr.close()
