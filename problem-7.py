#Creating an new file
location=input('Enter the location of file')
file = open(location,"w")
file.close()

#Creating multiple file together
num=int(input("Enter Number of new files to create"))
for i in range(num):
    location=input("Enter name of file ")
    myfile=open(location,"w")
myfile.close()

#To check the access and modification time and update it
import os
location=input('Enter the location of file')
stinfo = os.stat(location)
print(stinfo)

print(os.utime(location,(stinfo.st_atime,stinfo.st_mtime)))

# upadate the modification time of one file with the other file
loc1=input("Enter File path from which upadated date and time is extracted")
loc2=input("Enter File path To Update date and time")

os.utime(loc2(os.path.getmtime(loc1),os.path.getmtime(loc2)))
