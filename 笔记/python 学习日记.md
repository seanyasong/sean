##  centos
    ifcongif -a
    ipadd 
    打开/etc/sysconfig/network-scripts
    vi ifcfg-ens33 修改静态ip
    BOOTPROTO=static 动态改成静态
    点i进入编辑 修改ip地址成为我们自己本机的网关Ip geteway修改成自己家的地址
    DNS1修改成和ipadd一样的
    退出编辑是esc：+w是写q是保存 保存之后就重启命令：systemctl restart network
    检查防火墙状态：systemctl status firewalld
    vi /etc/hosts.allow  sshd:ALL

    更换源的地址：https://www.cnblogs.com/lyh233/p/12637970.html#_label4

    更换好源之后就下载宝塔文章地址：https://www.bt.cn/bbs/thread-19376-1-1.html

##  下载好的宝塔链接地址
    外网面板地址: http://140.240.39.206:8888/d7e77b8b
    内网面板地址: http://192.168.124.89:8888/d7e77b8b
    username: 2ai9ar9l
    password: 6cd61ebd
    17384607653
    88888888@A
    腾讯云 搬瓦工 甲骨文

    搭建好之后修改hosts 本地的hosts和服务器的hosts都要修改

    sudo vi /etc/hosts 按i是编辑 按o是增加一行
    实例192.168.124.89   www.pythonstudydiary.com

127.0.0.1       localhost
127.0.1.1       sean-G1

192.168.124.89   www.pythonstudy.com
# The following lines are desirable for IPv6 capable hosts
::1     ip6-localhost ip6-loopback
fe00::0 ip6-localnet
ff00::0 ip6-mcastprefix
ff02::1 ip6-allnodes
ff02::2 ip6-allrouters	

    nginx.org
    


