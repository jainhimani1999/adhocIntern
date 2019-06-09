#!/usr/bin/python3
import os
import crypt
user = input('Emter the user name')
if(type(user) == str):
        os.system('useradd '+user)
        unpass=crypt.crypt('hello '+user,'123')
        os.system('passwd '+unpass)
        print('user created')
else:
        print('invalid user')

