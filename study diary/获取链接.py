import requests

all_urls = []  #我们拼接好的列表路径
class Spider():
    #构造函数，初始化数据使用
    def __init__(self,target_url,headers):
        self.target_url = target_url
        self.headers = headers

    #获取所有的想要抓取的URL
    def getUrls(self,start_page,page_num):

        global all_urls
        #循环得到URL
        for i in range(start_page,page_num+1):
            url = self.target_url  % i
            all_urls.append(url)

if __name__ == "__main__":
    headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.67 Safari/537.36',
            'HOST':'www.baidu.com'
    }
    target_url = 'https://www.tupianzj.com/meinv/xinggan/list_176_%d.html' #列表规则

    spider = Spider(target_url,headers)
    spider.getUrls(1,15)
    print(all_urls)

