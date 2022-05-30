import urllib.request
#download web
url_page = 'http://www.baidu.com'
#在python中 可以写变量的名字  也可以直接写值
#urlretrieve里有两个参数 url代表的是下载的路径，filename文件的名字
urllib.request.urlretrieve(url_page,'baidu.html')

#download picture
url_img = "https://img3.utuku.imgcdc.com/505x0/ent/20210918/b21cc0d2-e639-4501-9dc9-9d594eecae8c.jpg"
urllib.request.urlretrieve(url= url_img,filename='lisa.jpg')

#download video
url_video = 'https://vd3.bdstatic.com/mda-nemd2bmcc5ey4bjz/sc/cae_h264/1653210986193109188/mda-nemd2bmcc5ey4bjz.mp4'
urllib.request.urlretrieve(url_video,'职业选手质量局.mp4')