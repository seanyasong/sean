from webbrowser import get
from pyrsistent import b
import requests  #导入请求模块
from bs4 import BeautifulSoup  #导入bs4模块
import os   #导入标准库os. 利用其中的API
from contextlib import closing 



url = ["http://bizhi360.com/youxi/list_{}.html".format(u)for u in range(2,16)]
# print(url)

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.64 Safari/537.36'
}

for i in url:
    
    r = requests.get(i,headers=headers)
    r.encoding = "UTF-8"
    soup = BeautifulSoup(r.text,"html.parser")
    lis = soup.find_all('li')
    
    for li in lis:
        img_href = li.find('a').get('href')
        img_name = li.find('a').get('title')
    #     print(img_href)
    #     break
    # break


        url = "http://bizhi360.com"+img_href
        result = requests.get(url)#请求结果赋值于result这个变量
        html = result.text#把返回结果赋值给变量
        
        bf = BeautifulSoup(html,'html.parser')
        targets_url_1 = bf.find_all(id='main')
        
        url_src = targets_url_1[0].find('img').get('src')
        # print(url_src)
        

    


        with closing(requests.get(url_src, headers=headers, stream=True)) as response:
            chunk_size = 1980  

            if response.status_code == 200:
                path = '游戏背景'
                if not os.path.exists(path):
                    os.mkdir(path)
                new_file = f'{path}/{img_name}.jpg'
                with open(new_file, "wb") as file:  #写入文件夹里
                    for data in response.iter_content(chunk_size=chunk_size):  
                        file.write(data)  
            