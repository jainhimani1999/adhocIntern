import webbrowser
from googlesearch import search
data=input("type your search :--->  ")
url = []
webbrowser.open_new_tab('https://www.google.com/search?q='+data)
for i in range(10):
    for j in search(data,num=10, stop=1):
        print(j)
        url.append(j)
