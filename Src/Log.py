#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
项目名称：
对象：日志
用途：写日志
时间：2016/3/4 18:17:25
作者: Liuker lt@liuker.xyz
"""


import sys 
 
reload(sys) 
sys.setdefaultencoding('utf-8')

import DbConnect
import UserName_DAL
import datetime


def WriteLog(s):
	try:
		# 日志文件
		now_time = datetime.datetime.now()
		write_time = now_time.strftime("%Y/%m/%d %H:%M:%S")
		micros = now_time.microsecond
		log_filename = now_time.strftime("%Y%m%d")
		log_path = 'c:\PushMail\Src\log\log_%s.txt' % (log_filename)

		# 打开文件
		fo = open(log_path, "a")
		fo.write(write_time)
		fo.write(u".%d\n\t%s\n" % (micros/1000, s))
		fo.close()

	except Exception, e:
		print str(e)