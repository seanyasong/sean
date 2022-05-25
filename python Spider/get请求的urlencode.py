#   urlencode的应用场景：多个参数的时候

#   https://www.baidu.com/s?wd=周杰伦&sex=男

# from re import A
import urllib.request
import urllib.parse

from requests import request



# a = urllib.parse.urlencode(data)
# print(a)

base_url = 'https://www.baidu.com/s?'

data = {
    'wd':'周杰伦',
    'sex':'男',
    'location':'中国台湾省'
}

new_data = urllib.parse.urlencode(data)
# print(new_data)
#请求资源路径
url = base_url + new_data

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.64 Safari/537.36 Edg/101.0.1210.53'
}

#请求对象的定制
request = urllib.request.Request(url=url,headers=headers)

#模拟浏览器向服务器发送请求
response = urllib.request.urlopen(request)

#获取网页源码的数据
content = response.read().decode('utf-8')

#打印数据
print(content)