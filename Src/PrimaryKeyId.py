#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
项目名称：
对象：
用途：生成主键ID
时间：2016/3/3 10:40:38
作者: Liuker lt@liuker.xyz
"""



import datetime
import random
import Log

#函数名称：CreateNewID
#函数功能：生成ID
#函数参数：
#  
#返回值：
#  ID(长度为30位) eg.201603022151026600006944189497
def CreateNewID():
	id = ""
	try:
		now_time = datetime.datetime.now()
		#2016-03-02 17:08:25.856000
		date_time = now_time.strftime("%Y%m%d%H%M%S")
		date_time += str(now_time.microsecond)[0:3]
		date_time += str(random.randint(100,999))

		random_ten = str(random.randint(0,9)) 
		random_ten += str(random.randint(10,99))
		random_ten += str(random.randint(100,999))
		random_ten += str(random.randint(1000,9999))

		id = date_time + random_ten
		Log.WriteLog(u"生成ID失败！ID=%s" % (id))

		return id
	except Exception, e:
		Log.WriteLog(u"生成ID失败！文件\"PrimaryKeyId.py\"，函数\"CreateNewID()\"，错误原因：%s" % (e))
		return id
