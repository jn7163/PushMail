#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
项目名称：
对象：新订阅者
用途：将新订阅者的信息写入数据库
时间：2016/3/3 14:13:49
作者: Liuker lt@liuker.xyz
"""



import MySQLdb
import DbConnect
import ReadFile

mysqlcont = DbConnect.Connect2DB('127.0.0.1', 'root', '123123', 'googlehosts')
file_path = "c:\PushMail\Src\NewSubscriber.txt"  #订阅者

"""
# 函数SplitString1，格式：Liuker(Beijing,China)#lt@liuker.xyz
ReadFile.Save2DB(mysqlcont, file_path, "SplitString1")
	print u"插入成功！"
else:
	print u"插入失败！"
"""

# 函数SplitString2，格式：Liuker#lt@liuker.xyz#Liuker#liuker0x007#Beijing,China#]Liuker Team[
if ReadFile.Save2DB(mysqlcont, file_path, "SplitString2"):
	print u"插入成功！"
else:
	print u"插入失败！"

DbConnect.Close2DB(mysqlcont)
