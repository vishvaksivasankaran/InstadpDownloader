import requests 
import urllib.request
from bs4 import BeautifulSoup
def downloader(url):
    name=input("Enter the file name")
    name=name+".jpg"
    urllib.request.urlretrieve(url,name)
username=input("Enter the username:")
link="https://www.picuki.com/profile/"+username
page=requests.get(link)
s=BeautifulSoup(page.content,'html.parser')
l=s.find_all('img')
post=[]
for i in l:
    if 'src' in i.attrs:
        print(str(i.attrs['src'])+"\n")
        post.append(str(i.attrs['src']))
print(len(post))
print("Enter 19 if you want his profile")
h=int(input("Enter the post to be downloaded:"))
downloader(post[len(post)-h])


