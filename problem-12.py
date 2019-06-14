import pyqrcode
from pyqrcode import QRCode
import webbrowser
from googlesearch import search


data=input('Enter the website')
url=[]
webbrowser.open_new_tab('https://www.google.com/search?q='+data)
for i in search(data,num=3,stop=3):
    print(i)
    url.append(i)

# Generate QR code
for j in url:
    pyqrcode.create(j)
    print('sucess')

# Create and save the png file naming "myqr.png"
'''url.svg("myqr.svg", scale = 8)
f=open('myqr.svg','r')
print(f.read())'''
