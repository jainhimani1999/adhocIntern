#for cat command
file = open("file.txt", "r")
#print(file.read())

#for cat -E command
'''for line in file:
    print(line.strip() + "$")

#for cat -n command
count = 1
for line in file:
    print(str(count)+line.strip())
    count+=1
#for output redirection cat file > file1
'''
location = input('Enter the file to be overwritten')
file2 = open(location,"w")
file2.write(file.read())
print(file2)
file2.close()

#for output redirection cat file >> file1
file.seek(0)
locationR = input('Enter the files to be append')
myfile = open(locationR,"a")
myfile.write(file.read())
file.close()
myfile.close()
