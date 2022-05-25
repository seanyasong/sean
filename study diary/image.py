import re
import requests  #导入请求模块
from bs4 import BeautifulSoup  #导入bs4模块
import os   #导入标准库os. 利用其中的API
from contextlib import closing 

url = ['https://www.tupianzj.com/meinv/xinggan/list_176_{}.html'.format(i) for i in range(1,355)]#获取页面url
# print(url)

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.64 Safari/537.36'
}


for i in url:
    r = requests.get(i,headers=headers)#请求头
    r.encoding = 'gb2312'  #页面编码
    soup = BeautifulSoup(r.text,'html.parser')
    
    lis = soup.find_all('ul')
    # print(lis)
    for a in lis:
        img_hers = a.find('a').get('href')
        img_name = a.find('a').get('title')
        print(img_hers)
        print(img_name)
    # bss = lis.find_all('a').get('href')
    # print(bss)
        # image_link = a['src']   #获取image里面的link
        # image_name = a['alt']   #获取image里面的title
        # print(a)
        
    break

        

        # with closing(requests.get(image_link, headers=headers, stream=True)) as response:
        #     chunk_size = 1024  

            
        #     if response.status_code == 200:  #如果这个页面请求等于200
                
        #         path = '美女图片'  #找到美女图片这个文件夹
        #         if not os.path.exists(path):   #如果没有这个文件夹
        #             os.mkdir(path)    #就创建这个文件夹
        #         new_file = f'{path}/{image_name}.jpg'  #保存image的名字
        #         with open(new_file, "wb") as file:  #写入文件夹里
        #             for data in response.iter_content(chunk_size=chunk_size):  
        #                 file.write(data)  
        #     else:
        #         print('链接异常')
        #         print('下载完成！')



        
        


        
        
        
    


 





