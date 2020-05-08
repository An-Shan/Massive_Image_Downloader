import requests
from bs4 import BeautifulSoup

def download_pic(url,path):
    pic=requests.get(url)
    path+=url[url.rfind('.'):]#¥[¤JªþÀÉ¦W
    with open(path,'wb') as f:
        f.write(pic.content)
url='https://hips.hearstapps.com/hmg-prod.s3.amazonaws.com/images/dog-puppy-on-garden-royalty-free-image-1586966191.jpg'
pic_path='download'
download_pic(url,pic_path)

url='https://pixabay.com/zh/images/search/dog/'
header={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36'}
html=requests.get(url,headers=header)
html.encoding='utf-8'
print(html.status_code)
bs=BeautifulSoup(html.text,'lxml')
photo_item=bs.find_all('div',class_='item')
photo_lst=[]
print(photo_item)
for i in range(len(photo_item)):
    photo=photo_item[i].find('img')['src']
    photo_lst.append(photo)
print(photo_lst)    
