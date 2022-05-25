

# 起初美国有关标准组织制定了一套编码叫ASCII码,用了一个字节低7位,最高位二进制位0,编码范围是00000000-0xxxxxxx，总共有128状态,表示了大小写字母,数字,标点符号以及特殊的控制字符.

# 0~31以及127(共33个)是控制字符,例如:LF(换行),CR(回车).

# 32~156(共95个)是字符,48~57为0到9共十个阿拉伯数字,65~122是大小的英文字母,其余的是字符,运算符等.

# 0-127 标准ascii码，127-255扩展ascii码，扩展主要存储西欧国家的一些字符

# 最终，美国人意识到他们应该提出一种标准方案来展示世界上所有语言中的所有字符，出于这个目的，Unicode诞生了，或叫UCS，分为UCS-2和UCS-4.分别代表用2或4个字节存储。

# Unicode 给所有的字符指定了一个数字用来表示该字符。

# 现目前 Unicode 支持 3种编码方式，UTF-8，UTF-16，UTF-32。

# 编码方式字节数

# UTF-81 - 4

# UTF-162 or 4

# UTF-324

# UTF-8

# 目前互联网上使用最广泛的一种 Unicode 编码方式，它的最大特点就是可变长。它可以使用 1 - 4 个字节表示一个字符，根据字符的不同变换长度。编码规则如下：

# 对于单个字节的字符，第一位设为 0，后面的 7 位对应这个字符的 Unicode 码点。因此，对于英文中的 0 - 127 号字符，与 ASCII 码完全相同。这意味着 ASCII 码那个年代的文档用 UTF-8 编码打开完全没有问题。

# 对于需要使用 N 个字节来表示的字符（N > 1），第一个字节的前 N 位都设为 1，第 N + 1 位设为0，剩余的 N - 1 个字节的前两位都设位 10，剩下的二进制位则使用这个字符的 Unicode 码点来填充。

# 编码规则如下：
# Unicode 十六进制码点范围 UTF-8 二进制

# 0x00- 0x7F                       0xxxxxxx

# 0x80-0x7FF                     110xxxxx 10xxxxxx

# 0x800-0xFFFF                1110xxxx 10xxxxxx 10xxxxxx

# 0x10000 - 0x10FFFF      11110xxx 10xxxxxx 10xxxxxx 10xxxxxx

# 根据上面编码规则对照表，进行 UTF-8 编码和解码就简单多了。下面以汉字“汉”为利，具体说明如何进行 UTF-8 编码和解码。

# “汉”的 Unicode 码点是 0x6c49（110 1100 0100 1001），通过上面的对照表可以发现，0x0000 6c49 位于第三行的范围，那么得出其格式为 1110xxxx 10xxxxxx 10xxxxxx。接着，从“汉”的二进制数最后一位开始，从后向前依次填充对应格式中的 x，多出的 x 用 0 补上。这样，就得到了“汉”的 UTF-8 编码为 11100110 10110001 10001001，转换成十六进制就是 0xE6 0xB7 0x89。

# 解码的过程也十分简单：如果一个字节的第一位是 0 ，则说明这个字节对应一个字符；如果一个字节的第一位1，那么连续有多少个 1，就表示该字符占用多少个字节。


#   需求    获取    https://www.baidu.com/s?wd=%E5%91%A8%E6%9D%B0%E4%BC%A6   的网页源码

import urllib.request
import urllib.parse


url = "https://www.baidu.com/s?wd="


#请求对象定制未来解决反扒的第一种手段
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.64 Safari/537.36 Edg/101.0.1210.53'
}

#  将周杰伦三个字变成unicode编码的格式
#  我们需要依赖于urllib.parse
name = urllib.parse.quote('周杰伦')

url = url + name
print(url)

#请求对象的定制
request = urllib.request.Request(url=url,headers=headers)

#模拟浏览器想服务器发送请求
response = urllib.request.urlopen(request)

#获取响应内容
content = response.read().decode('utf-8')

#打印数据
print(content)