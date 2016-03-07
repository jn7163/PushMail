#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
项目名称：
对象：文档
用途：读取文件的内容
时间：2016/3/3 14:13:49
作者: Liuker lt@liuker.xyz
"""



import sys 
import UserName_DAL
import Log
 
reload(sys) 
sys.setdefaultencoding('utf-8')


#函数名称：SplitString1
#函数功能：分割字符串，格式：Liuker(Beijing,China)#lt@liuker.xyz
#函数参数：
#  s：待分割的字符串，格式：Liuker(Beijing,China)#lt@liuker.xyz
#返回值：
#  分割后的结果，(用户名, 邮箱地址, github昵称, github账号, 地址, 组织)
def SplitString1(s):
	name = ""
	mail = ""
	address = ""
	try:
		findstr = '#'
		mail_index = s.find(findstr) #获取邮件开始的位置
		mail = s[mail_index + 1:]
		name_address = s[0:mail_index]
		
		findstr = '('
		address_index = name_address.find(findstr) #获取地址开始的位置
		if address_index > -1:
			address = name_address[address_index + 1:-1]
			name = name_address[0:address_index]
		else:
			name = name_address
		Log.WriteLog(u"分割“%s”成功！" % (s))
		return (name, mail, "", "", address, "")
	except Exception, e:
		Log.WriteLog(u"错误：分割字符串失败！文件\"ReadFile.py\"，函数\"SplitString1(s)\"，错误原因：%s" % (e))
		return (name, mail, "", "", address, "")


#函数名称：SplitString2
#函数功能：分割字符串，格式：Liuker#lt@liuker.xyz#Liuker#liuker0x007#Beijing,China#]Liuker Team[
#函数参数：
#  s：待分割的字符串，格式：Liuker#lt@liuker.xyz#Liuker#liuker0x007#Beijing,China#]Liuker Team[
#返回值：
#  分割后的结果，(用户名, 邮箱地址, github昵称, github账号, 地址, 组织)
def SplitString2(s):
	uname = ""
	email = ""
	githubuname = ""
	github = ""
	address = ""
	org = ""
	try:
		list_results = s.split("#")
		name = list_results[0]
		mail = list_results[1]
		githubuname = list_results[2]
		github = list_results[3]
		address = list_results[4]
		org = list_results[5]
		Log.WriteLog(u"分割“%s”成功！" % (s))
		return (name, mail, githubuname, github, address, org)
	except Exception, e:
		Log.WriteLog(u"错误：分割字符串失败！文件\"ReadFile.py\"，函数\"SplitString2(s)\"，错误原因：%s" % (e))
		return (name, mail, githubuname, github, address, org)


#函数名称：ReadFile2List
#函数功能：读取文件的内容到list中
#函数参数：
#  file_path：文件路径
#  filelist：list的地址
#返回值：
#  读取的内容，即列表
def ReadFile2List(file_path, filelist):
	try:
		f = open(file_path, 'r') #读取文件
		for line in f.readlines():  #逐行读取文件
			filelist.append(line.strip())
	except Exception, e:
		Log.WriteLog("错误：读取文件“%s”失败！文件\"ReadFile.py\"，函数\"ReadFile2List(file_path, filelist)\"，错误原因：%s" % (file_path, e))
	finally:
		if f:
			f.close()
			Log.WriteLog("关闭文件“%s”成功！" % (file_path))



#函数名称：Save2DB
#函数功能：把数据保存到数据库中
#函数参数：
#  mysqlcont：数据库连接
#  file_path：文件路径
#  split_fun：分割的函数名称
#返回值：
#  执行结果(True, False)
def Save2DB(mysqlcont, file_path, split_fun):
	try:
		filelist = []
		ReadFile2List(file_path, filelist) #把文件内容读取到list中

		num_ok = 0
		for row in filelist:
			pkid = UserName_DAL.CreateNewPkId(mysqlcont)
			issend = 1
			(uname, email, githubuname, github, address, org) = eval(split_fun)(row)
			uname = uname.decode("gbk").encode("utf-8") #转码
			email = email.decode("gbk").encode("utf-8") #转码
			githubuname = githubuname.decode("gbk").encode("utf-8") #转码
			github = github.decode("gbk").encode("utf-8") #转码
			address = address.decode("gbk").encode("utf-8") #转码
			org = org.decode("gbk").encode("utf-8") #转码
			#存入数据库
			if UserName_DAL.AddOne(mysqlcont, pkid, uname, email, issend, githubuname, github, address, org):
				num_ok += 1
		Log.WriteLog(u"成功插入 %s 条记录！" % (num_ok))
		print u"成功插入 %s 条记录！" % (num_ok)
		return True
	except Exception, e:
		Log.WriteLog(u"错误：数据保存到数据库失败！文件\"ReadFile.py\"，函数\"Save2DB(mysqlcont, file_path, split_fun)\"，错误原因：%s" % (e))
		return False
