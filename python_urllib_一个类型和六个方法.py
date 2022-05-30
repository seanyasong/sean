import urllib.request

from urllib3 import HTTPResponse

url = 'http://www.baidu.com'
#模拟服务器发送请求
response = urllib.request.urlopen(url)

#一个类型和六个方法
#response是 HTTPResponse的类型
#print(type(response))


#方法
#按照一个字节一个字节的去读 如果在括号里输入数字代表返回多少个字节
# content= response.read(5)
# print(content)

#读取一行
# content = response.readline()
# print(content)

#读取全部行
# content = response.readlines()
# print(content)

#返回页面状态码  如果是200  那么证明可以打开
#print(response.getcode())

#返回网址
# print(response.geturl())

#get 状态信息  响应头
print(response.getheaders())

# 一个类型 HTTPResponse
# 六个方法 read  readline readlines  getcode  geturl  getdeaders