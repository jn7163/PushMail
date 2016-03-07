#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
项目名称：
对象：数据库数据
用途：备份数据库数据到本地
时间：2016/3/4 13:37:06
作者: Liuker lt@liuker.xyz
"""


import sys 
import Log
 
reload(sys) 
sys.setdefaultencoding('utf-8')

import DbConnect
import UserName_DAL
import datetime

now_time = datetime.datetime.now()
date_time = now_time.strftime("%Y%m%d%H%M%S")
bk_path = 'F:\Liuker\MyBlog\hosts\PushMail\Src\\backup\\backup_%s.txt' % (date_time)

try:
	mysqlcont = DbConnect.Connect2DB('127.0.0.1', 'root', 'lt.2015', 'googlehosts')

	filed_cont = "VChar_Name, VChar_Email, VChar_GithubUName, VChar_Github, VChar_Address, Text_Oranizations"
	where_cont = " Char_Id <>'' "
	results = UserName_DAL.SelectByWhere(mysqlcont, filed_cont, where_cont)

	# 打开文件
	fo = open(bk_path, "a")

	for row in results:
		bkstr = "%s#%s#%s#%s#%s#%s\n" % (row[0], row[1], row[2], row[3], row[4], row[5])
		Log.WriteLog(u"备份数据：“%s”成功！" % (bkstr))
		fo.write(bkstr.decode("utf-8").encode("gbk"))
	fo.close()

	DbConnect.Close2DB(mysqlcont)
	Log.WriteLog(u"备份数据库信息成功！备份路径为“%s”" % (bk_path))
	print u"备份成功！\n路径“%s”" % (bk_path)
except Exception, e:
	Log.WriteLog(u"%s" % (e))