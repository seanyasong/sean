# coding:utf-8
import re #正则模块
import requests #请求模块
import time #时间模块
from bs4 import BeautifulSoup  #调用对象的属性来解析数据

# 获取网页内容
for page in range(2,3): #循环页码
    r = requests.get('https://h-webtoon.com/page/' + str(page)) # 循环打开链接
    data = r.text # 获取页面信息text参数接受字符串正则
    link_list =re.findall(r'(<a.*?href="(.*?)" title="(.*?)">)' ,data) # 正则提取首页列表链接
    for url in link_list: # 循环获取首页列表链接
        if "webtoon.com" in url[1]: # 判断必须包含该网址才要
            url_list = [url[1]] # 正则出来是有关键词跟链接所以提取出链接来赋值到新的变量
            for urls in url_list: # 获取到首页列表的链接,在循环列表的链接获取内页链接
                r1 = requests.get(urls) # 循环打开列表的链接
                data1 = r1.text # 获取页面信息text参数接受字符串正则
                link_list1 =re.findall(r'(<a.*?href="(.*?)" rel=")' ,data1) # 正则提取列表页的文章链接链接
                for url_1 in link_list1: # 循环获取列表页的文章链接
                    if "webtoon.com" in url_1[1]: # 判断必须包含该网址才要
                        url_list1 = [url_1[1]] # 正则出来是有关键词跟链接所以提取出链接来赋值到新的变量
                        for urls_1 in url_list1: # 获取到列表里的文章链接,在循环打开文章链接
                            r2 = requests.get(urls_1) # 循环打开文章链接
                            data2 = r2.text  # 获取页面信息text参数接受字符串正则
                            link_list2 =re.findall(r'<h1 class="g1-mega g1-mega-1st entry-title" itemprop="headline">(.*?)</h1>' ,data2)[0] # 正则提取文章标题
                            charpter_soup = BeautifulSoup(data2,'html.parser') # 网页抓取数据解析器
                            content = charpter_soup.find('div',class_='g1-content-narrow') # 通过抓取数据找到需要抓取的位置
                            content1 = content.find_all("p") # 通过抓取位置抓取出带p标签的内容,相当于正则
                            wenzhang = '' # 空值赋值到新的变量,等待接收正则循环好的内容
                            for article in content1: # 循环获取正则的文章
                                wenzhang += str(article)  # 将获取的所有正文内容进行拼接,一个正文里面有很多的p标签，循环拼接保存到wenzhang变量
                            lujing = "C:/chengxu/111/" + str(link_list2) + ".txt"  # 保存文本路径
                            f = open(lujing,"w")        # 打开以建好的文本
                            f.write(wenzhang)  # 写入文章保存
                            print(link_list2 , "  写入成功!")   # 提示保存成功
                            time.sleep(2)    # 获取一篇文章停留两秒                 

