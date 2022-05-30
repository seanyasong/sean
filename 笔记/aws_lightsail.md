aws服务器安装
    注册账户
    https://aws.amazon.com/free

轻量级服务器lightsail
    安装好后密钥会自动下载到本地，ssh远程登陆是需要设置
        vscode添加服务器设置，添加密钥路径
            Host 34.219.250.248
                HostName 34.219.250.248
                User centos
                IdentityFile /Users/jsc/Downloads/LightsailDefaultKey-us-west-2.pem

        对密钥路径设置拥有者可读写，其他人不可读写执行权限
            https://blog.csdn.net/u013197629/article/details/73608613
            chmod 600 密钥文件路径

LNMP一键安装
    https://lnmp.org/

修改MySQL数据库密码(以下操作都用最高权限root用户执行)
    vi /etc/my.cnf
        在[mysqld]下面添加一条命令：skip-grant-tables
    重启服务器
        reboot
    修改密码
        mysql -uroot -p
        update mysql.user set authentication_string=password('密码') where user='root'; 
        退出
            exit
        重启服务器
            reboot

创建wordpress数据库
    https://www.123067.xyz/2021/231/
    https://blog.51cto.com/u_15162069/2919897

    添加wordpress用户
        CREATE USER '用户名'@'localhost' IDENTIFIED BY 'PASSWORD';
    创建数据库
        create database 数据库名;
    赋予用户权限
        grant all privileges on  wordpress.* to 'wordpress'@'localhost';
    退出
        exit 
        or 
        quit;
    
    如何操作，如何选择数据库
        https://www.runoob.com/mysql/mysql-tutorial.html
        use 数据库名; （选择了数据库后，后续的操作都在该数据库下）
        查看数据库表内容
            show table;

下载wordpress
    https://cn.wordpress.org/download/
    下载到指定路径
        cd /home/www
    复制下载地址wget下载并解压
        wget https://cn.wordpress.org/latest-zh_CN.tar.gz
    解压
        tar -zxvf latest-zh_CN.tar.gz
    重命名网站名
        mv wordpress 域名 
    给服务器网站路径提权
        chmod -R 777 /home/www

修改Nginx conf文件
    添加新的conf文件
        server
        {
            listen 80;
            server_name www.globallearn.com *.globallearn.com;
            index index.php index.html index.htm;
            root /home/www/www.globallearn.com;
        location ~ \.php$
        {
        try_files $uri =404;
        fastcgi_pass  unix:/tmp/php-cgi.sock;
        fastcgi_index index.php;
        include fastcgi.conf;
        }
        }
    重启Nginx
        去到Nginx sbin目录下
        cd /usr/local/nginx/sbin
        ./nginx -s reload

登陆wordpress后台
    http://域名/wp-admin/install.php
    





    





    
        


