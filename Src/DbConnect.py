#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
项目名称：
对象：数据库
用途：数据库连接与关闭操作
时间：2016/3/3 10:40:38
作者: Liuker lt@liuker.xyz
"""


import sys 
import MySQLdb
import Log
 
reload(sys) 
sys.setdefaultencoding('utf-8')


#函数名称：Connect2DB
#函数功能：连接数据库
#函数参数：
#  hostname：服务器
#  uname：用户名
#  pwd：密码
#  dbname：数据库名
#返回值：
#  数据库连接结果
def Connect2DB(hostname, uname, pwd, dbname):
	try:
		# 打开数据库连接
		mysqlcont = MySQLdb.connect(host=hostname, user=uname, passwd=pwd, db=dbname, charset='utf8')
		Log.WriteLog(u"数据库连接成功！")
		return mysqlcont
	except Exception, e:
		Log.WriteLog(u"错误：数据库连接失败！文件\"DbConnect.py\"，函数\"Connect2DB(hostname, uname, pwd, dbname)\"，错误原因：%s" % (e))
		print u"数据库连接失败！"
		return None


#函数名称：Close2DB
#函数功能：关闭数据库连接
#函数参数：
#  mysqlcont：连接名
#返回值：
#  关闭连接的结果(True、False)
def Close2DB(mysqlcont):
	try:
		# 关闭数据库连接
		mysqlcont.close()
		Log.WriteLog(u"数据库关闭成功！")
		return True
	except Exception, e:
		Log.WriteLog(u"错误：数据库关闭失败！文件\"DbConnect.py\"，函数\"Close2DB(mysqlcont)\"，错误原因：%s" % (e))
		print u"数据库关闭失败！"
		return False