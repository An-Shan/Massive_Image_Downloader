import requests
from bs4 import BeautifulSoup
import t as chsagt

def download_pic(url,path):
    pic=requests.get(url)
    path+=url[url.rfind('.'):]#加入附檔名
    with open(path,'wb') as f:
        f.write(pic.content)
#url='https://hips.hearstapps.com/hmg-prod.s3.amazonaws.com/images/dog-puppy-on-garden-royalty-free-image-1586966191.jpg'
#pic_path='download'
#download_pic(url,pic_path)

#url='https://www.google.com/search?q=dog&sxsrf=ALeKk00kH_oK75O3BBIqtY2VhzasWyK47Q:1589031103371&source=lnms&tbm=isch&sa=X&ved=2ahUKEwjE6c-T8qbpAhUlw4sBHckcB-gQ_AUoAXoECBkQAw&biw=1536&bih=754'
url='https://pixabay.com/images/search/dog/'
#header={'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36'}
#header={'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36', 'Accept-Encoding': 'gzip, deflate', 'Accept': '*/*', 'Connection': 'keep-alive'}
header={'User-Agent': chsagt.get_user_agent() }
html=requests.get(url,headers=header)
print(html.request.headers)
html.encoding='utf-8'
print(html.status_code)
bs=BeautifulSoup(html.text,'lxml')
#photo_item=bs.find_all('div',class_='bRMDJf islir')
photo_item=bs.find_all('div',class_='item')
photo_lst=[]
#print(photo_item)
for i in range(len(photo_item)):
    photo=photo_item[i].find('img')['src']
    photo_lst.append(photo)
print(photo_lst)

for photo_url in photo_lst:
    download_pic(photo_url,'download')
