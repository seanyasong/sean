### 关键词
    json数据转换
    怎么通俗理解json
    json解析
    json解析接口
    免费json解析地址
    json文件怎么创建
    json文件怎么变为图片
    在线json生成器
    json数据是什么意思
    json解析
    json语法
    json编辑器
    json格式
    json文件
    json教程
    json美化
### 常见问题
####    JSON 是用来做什么的？
        它是一种基于文本的方式来表示 JavaScript 对象字面量、数组和标量数据。 JSON相对容易读写，同时也易于软件解析和生成。 它通常用于序列化结构化数据并通过网络进行交换，通常在服务器和 Web 应用程序之间进行。
        JSON 是一种轻量级的、基于文本的、与语言无关的数据交换格式。它源自 Javascript/ECMAScript 编程语言，但独立于编程语言。 JSON 被认为是 XML 的轻量级替代品，如 JSON：The Fat-Free Alternative to XML，2006 年由 JSON 的开发者 Douglas Crockford 撰写的演示文稿。 JSON 为结构化数据的可移植表示定义了一小组结构化规则。 JSON 为表示对象、名称/值对的集合以及数组、值的有序列表提供了简单的表示法。通过嵌套这两个基本结构，可以表示树和其他复杂的数据结构。
        JSON 语法使用大括号（大括号：{}）、方括号（[]）、冒号和逗号将字符串（双引号中的字符序列）或数字（表示为数字序列）的值排列成两个基本结构。
        对象是一组无序的名称/值对。对象以 {（左大括号）开始，以 }（右大括号）结束。每个名称后跟 :（冒号），名称/值对用 ,（逗号）分隔。数组是值的有序集合。数组以 [（左括号）开头，以 ]（右括号）结尾。值用 ,（逗号）分隔。值可以是双引号中的字符串、数字、true 或 false 或 null，也可以是对象或数组。这些结构可以嵌套。
        尽管 JSON 的开发者在 2006 年声明 JSON 不是一种标记语言，但现在它经常被这样对待。通用 JSON 用作特定格式的基础，这些格式指定名称和更具体的值语法。示例包括 GeoJSON 及其扩展 TopoJSON。模式语言已在 json-schema-org 中记录，以支持 JSON 应用程序的规范和验证。
####    JSON 和 JavaScript 有什么区别？
        JavaScript 对象 VS JSON
        JSON 不能包含函数。 JavaScript 对象可以包含函数。 JSON 可以由其他编程语言创建和使用。 JavaScript 对象只能在 JavaScript 中使用。
        
        {
        "name": "中国",
        "province": [{
            "name": "黑龙江",
            "cities": {
                "city": ["哈尔滨", "大庆"]
            }
        }, {
            "name": "广东",
            "cities": {
                "city": ["广州", "深圳", "珠海"]
            }
        }, {
            "name": "台湾",
            "cities": {
                "city": ["台北", "高雄"]
            }
        }, {
            "name": "新疆",
            "cities": {
                "city": ["乌鲁木齐"]
            }
        }]
        }
#### json里所有的数据类型
    JSON 数据类型
    JSON 格式支持以下数据类型：
    类型	描述
    数字型（Number）	JavaScript 中的双精度浮点型格式
    字符串型（String）	双引号包裹的 Unicode 字符和反斜杠转义字符
    布尔型（Boolean）	true 或 false
    数组（Array）	有序的值序列
    值（Value）	可以是字符串，数字，true 或 false，null 等等
    对象（Object）	无序的键:值对集合
    空格（Whitespace）	可用于任意符号对之间
    null	空
    详情：https://www.w3cschool.cn/json/28yd1mw2.html