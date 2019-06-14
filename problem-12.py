import qrcode
from googlesearch import search
data=input('Enter the website')
url=[]                                                                                                                           
f=open('/var/www/html/a.html','a')
for i in search(data,num=3,stop=3):
        print(i)
        url.append(i)                                                                                                            
# Generate QR code 
i=1
for j in url:                                                                                                                    
        image=qrcode.make(j)                                                                                                     
        print('sucess')                                                                                                          
        with open("/var/www/html/"+data+str(i)+".png",'wb') as k:
                image.save(k)                                                                                                    
        f.write('<img src="'+data+str(i)+".png"+'">')
        i+=1
f.close()                                                                                                                        
                                                                                                                         
