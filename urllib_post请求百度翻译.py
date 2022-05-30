import urllib.request
import urllib.parse

from requests import request
import json

url = 'https://fanyi.baidu.com/sug'

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.64 Safari/537.36 Edg/101.0.1210.53'
}

data = {
    'kw':'spider'
}

#post请求的参数 必须要进行编码

data = urllib.parse.urlencode(data).encode('utf-8')

# post的请求的参数 是不会拼接在url后面的  而是需要放在请求对象定制的参数中
request = urllib.request.Request(url=url,data=data,headers=headers)

#模拟浏览器向服务器发送请求
response = urllib.request.urlopen(request)

#获取响应数据
content = response.read().decode('utf-8')

#post请求方式的参数 必须编码  data = urllib.parse.urlencode(data).encode('utf-8)
#参数是放在请求对象定制的方法中 request = urllib.request.Request(url=url,data=data,headers=headers)

obj = json.loads(content)
print(obj)


