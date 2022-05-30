### 一个看了就能学会的python教程 
    首先要学习python，英语不是必备技能，不会英语也能学会，\
    但是会英语的话学习肯定能事半功倍，我整理一下python的英语\
    总共也就50+个，每天认识一两个对任何人来说都是很容易的事情。

### 首先认识所有的数据类型
    数据类型总共有14种，但是常用的总共也就7-8种，主要就是要理解数据可以分类的类型
    my_str="字符串"
    my_int = 12
    my_float = 222.3333
    my_complex = 2333j
    my_list = ["苹果", "香蕉", "葡萄"]
    my_tuple = ("apple", "banana", "cherry")
    my_range = range(13)
    my_dict = {"name" : "Bill", "age" : 63}
    my_set = {"apple", "banana", "cherry"}
    my_frozenset = frozenset({"apple", "banana", "cherry"})
    my_bool = True
    my_bytes = b"Hello"
    my_bytearray = bytearray(4)
    my_memoryview = memoryview(bytes(5))
    alltypes = [my_str,my_int,my_float,my_complex,my_list,my_tuple,my_range,my_dict,my_set,my_frozenset,my_bool,my_bytes,my_bytearray,my_memoryview]

### python基础语法
    python的语法比较简单，采用缩进的方式，写出来的代码就像下面的样子：
    a = 100
    if a >= 0:
        print(a)
    else:
        print(-a)
#### 字符串和编码
    以#开头的语句是注释，注释是给人看的，可以是任意内容，解释器会忽略掉注释。其他每一行都是一个语句，当语句以冒号:结尾时，缩进的语句视为代码块。

    缩进有利有弊。好处是强迫你写出格式化的代码，但没有规定缩进是几个空格还是Tab。按照约定俗成的惯例，应该始终坚持使用4个空格的缩进。

    缩进的另一个好处是强迫你写出缩进较少的代码，你会倾向于把一段很长的代码拆分成若干函数，从而得到缩进较少的代码。

    缩进的坏处就是“复制－粘贴”功能失效了，这是最坑爹的地方。当你重构代码时，粘贴过去的代码必须重新检查缩进是否正确。此外，IDE很难像格式化Java代码那样格式化Python代码。

    最后，请务必注意，Python程序是大小写敏感的，如果写错了大小写，程序会报错。
#### 格式化
    在python中，采用的格式话方式和C语言是一致的，用%来实现，for example
    >>> 'Hello, %s' % 'world'
    'Hello, world'
    >>> 'Hi, %s, you have $%d.' % ('Michael', 1000000)
    'Hi, Michael, you have $1000000.'

#### 占位符	替换内容
    %d	整数
    %f	浮点数
    %s	字符串
    %x	十六进制整数
    其中，格式化整数和浮点数还可以指定是否补0和整数与小数的位数：
    print('%2d-%02d' % (3, 1))
    print('%.2f' % 3.1415926)

#### format()
    另一种格式化字符串的方法是使用字符串的format()方法，它会用传入的参数依次替换字符串内的占位符{0}、{1}……，不过这种方式写起来比%要麻烦得多：


    小明的成绩从去年的72分提升到了今年的85分，请计算小明成绩提升的百分点，并用字符串格式化显示出'xx.x%'，只保留小数点后1位：
    >>> 'Hello, {0}, 成绩提升了 {1:.1f}%'.format('小明', 17.125)
    'Hello, 小明, 成绩提升了 17.1%'

### list
    Python内置的一种数据类型是列表：list。list是一种有序的集合，可以随时添加和删除其中的元素。

    比如，列出班里所有同学的名字，就可以用一个list表示：

    >>> classmates = ['Michael', 'Bob', 'Tracy']
    >>> classmates
    ['Michael', 'Bob', 'Tracy']

### 函数
    def element(x):
        print(type(x))
        print(dir(x))
        print([help(x)])
        return




### 循环
    for cycle in my_list:
        element(cycle)


### 判断
    for i in my_list:
        if isinstance(i,dict):
            print(i,'-- this is of type dict')
        else:
            print(i,'-- this is not of type dict , but is',type(i))

    a = 100
    if a >= 0:
        print(a)
    else:
        print(-a)

    elif是else if的缩写，完全可以有多个elif，所以if语句的完整形式就是：
        if <条件判断1>:
            <执行1>
        elif <条件判断2>:
            <执行2>
        elif <条件判断3>:
            <执行3>
        else:
            <执

### 类的定义 
    类的定义：简单的说类就像是一个柜子，这个柜子有很多层抽屉，一个函数就是一个抽屉，一个抽屉有一个抽屉的功能
    class human:
        def __init__(self,name,age,height):
            self.name = name
            self.age = age
            self.height = height
            self.man = True
            self.woman = False

        def sayhello():
            self.hello = print('hello')
    student_1 = human('xiu','18','191')
    print(student_1.name,student_1.age,student_1.height,student_1.man)


