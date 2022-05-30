import urllib.request

from requests import request

url = 'https://www.baidu.com'

#url的组成https://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=1&rsv_idx=周杰伦
# http/https     www.baidu.com    80/443     s      ie=utf-8&f=8&rsv_bp=1&rsv_idx=周杰伦
#    协议             主机        端口号      路劲        参数                              锚点
#   端口号
#   http    80 
#   https   443
#   mysql   3306
#   oracle  1521
#   redis   6379
#   mongodb 27017

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.64 Safari/537.36 Edg/101.0.1210.53'
}
#因为urlopen的发给发中不能存储字典 所以headers不能传递进去
#请求对象的定制
#注意 因为参数顺序的问题  不能直接写url 和headers  中间还有data   所以我们需要关键字传参

request = urllib.request.Request(url=url,headers=headers)

response = urllib.request.urlopen(request)

content = response.read().decode('utf-8')

print(content)

