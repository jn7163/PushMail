#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
项目名称：
对象：邮箱用户名、密码、服务器
用途：读取邮箱的用户名、密码、服务器
时间：2016/3/5 14:58:26
作者: Liuker lt@liuker.xyz
"""



import sys 
import Log
 
reload(sys) 
sys.setdefaultencoding('utf-8')


#函数名称：GetColumns
#函数功能：获取列的内容，并存于list中
#函数参数：
#  col_str：待分割的字符串
#  splitstr：分割符
#返回值：
#  分割后的结果lists
def GetColumns(col_str, splitstr):
	try:
		lists = col_str.split("%c" % (splitstr))
		Log.WriteLog(u"分割“%s”成功！" % (col_str))
		return lists
	except Exception, e:
		Log.WriteLog(u"错误：分割“%s”失败！文件\"ReadFile.py\"，函数\"GetColumns(col_str, splitstr)\"，错误原因：%s" % (col_str, e))
		return None


#函数名称：Save2Matrix
#函数功能：创建二维数组，存储数据
#函数参数：
#  file_path：文件路径
#返回值：
#  二维数组
def Save2Matrix(file_path):
	try:
		fo = open(file_path, 'r') #读取文件
		flist = fo.readlines()
		rows = len(flist)
		cols = len(GetColumns(flist[0], ";"))
		matrix = [[0 for col in range(cols)] for row in range(rows)]
		for i in range(rows):
			rows_con = flist[i].strip()
			rows_list = GetColumns(rows_con, ";")  #获取列的内容
			for j in range(cols):
				matrix[i][j] = rows_list[j]
		Log.WriteLog(u"邮件服务器信息“%s”存储为二维数组成功！" % (file_path))
		return matrix
	except Exception, e:
		Log.WriteLog(u"错误：邮件服务器信息存储为二维数组失败！文件\"ReadFile.py\"，函数\"Save2Matrix(file_path)\，错误原因：%s" % (e))
		return None
	