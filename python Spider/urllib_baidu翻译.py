import urllib.request
import urllib.parse
 
# url是上图黄线处文件的Request URL:
url = 'https://fanyi.baidu.com/v2transapi?from=en&to=zh'
 
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.64 Safari/537.36 Edg/101.0.1210.53'
}
 
data = {
    'from': 'en',
    'to': 'zh',
    'query': 'spide',
    'transtype': 'realtime',
    'simple_means_flag': '3',
    'sign': '894007.608006',
    'token': '7eab9fb613c8ee66bd7d8a8e7fd3f838',
    'domain': 'common',
}
 
# post请求的参数必须要进行编码，并调用encode方法
data = urllib.parse.urlencode(data).encode('utf-8')
 
# 请求对象的定制
request = urllib.request.Request(url=url, data=data, headers=headers)
 
# 模拟浏览器向服务器发送请求
response = urllib.request.urlopen(request)
 
# 获取响应的数据
content = response.read().decode('utf-8')
 
import json
 
obj = json.loads(content)
print(obj)