说明
----

本系统是用于Google Hosts更新时，对关注的朋友进行消息推送。其源码结构如下：
```
PushMail
├── AddSubscriber2DB.bat      //新写入订阅者
├── BackupDb2File.bat         //备份数据库数据
├── Push.bat                  //群发邮件
└── Src
    ├── backup
    │   └── backup_20160306204156.txt  //备份文件backup_20160306204156.txt
    ├── html
    │   └── MailContent.html  //邮件内容html文件
    ├── log
    │   └── log_20160306.txt  //日志文件log_20160306.txt
    ├── sql
    │   └── UserName_googlehosts.sql  //创建username表的SQL语句
    ├── BackupDb2File.py      //备份数据库数据到本地
    ├── DbConnect.py          //数据库连接
    ├── Log.py                //写日志
    ├── MailServerConfig.py   //邮箱服务配置信息
    ├── MailServerConfig.txt  //邮箱服务配置文件
    ├── NewSubscriber.txt     //新订阅者信息文件
    ├── Open CMD.bat          //当前目录打开CMD
    ├── PrimaryKeyId.py       //生成主键ID
    ├── Push.py               //群发邮件
    ├── ReadFile2DB.py        //读取订阅者信息并写入数据库
    ├── ReadFile.py           //读取文件
    ├── SendMail.py           //发送邮件
    └── UserName_DAL.py       //数据操作类

5 directories, 20 files
```


运行环境
--------

### Python2.7

系统采用的是Python开发的，所以首先要安装[Python2.7](http://www.python.org/)。详细安装过程：[安装Python - 廖雪峰的官方网站](http://www.liaoxuefeng.com/wiki/001374738125095c955c1e6d8bb493182103fac9270762a000/001374738150500472fd5785c194ebea336061163a8a974000)


### Mysql

系统用的数据库是Mysql，下载地址：[MySQL Community Server 5.5.48](http://dev.mysql.com/downloads/mysql/5.5.html)。详细的安装过程：[MySQL 安装 | 菜鸟教程](http://www.runoob.com/mysql/mysql-install.html)


配置
----

1、配置文件BackupDb2File.py、Push.py、ReadFile2DB.py中`mysqlcont = DbConnect.Connect2DB('127.0.0.1', 'root', 'lt.2015', 'googlehosts')`的MySQL连接信息。

2、配置文件BackupDb2File.py中的`bk_path`，文件Log.py中的`log_path`，文件ReadFile2DB.py中的`file_path`。


联系我
------

  * E-mail: [lt@liuker.xyz](mailto:lt@liuker.xyz)
  * QQ: [2523417411](http://wpa.qq.com/msgrd?v=3&uin=2523417411&site=qq&menu=yes)
