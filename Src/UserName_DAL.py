#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
项目名称：
对象：UserName表
用途：UserName表的数据操作
时间：20016/3/2 10:47:54
作者: Liuker lt@liuker.xyz
"""

import sys 
import MySQLdb
import PrimaryKeyId
import Log
 
reload(sys) 
sys.setdefaultencoding('utf-8')


#函数名称：IsRxistsByID
#函数功能：查询ID是否存在
#函数参数：
#  mysqlcont: 数据库连接
#  pkid：主键ID
#返回值：
#  执行结果(True、False)
def IsRxistsByID(mysqlcont, pkid):
	try:
		# 使用cursor()方法获取操作游标 
		cursor = mysqlcont.cursor()
		ret = False
		sql = "SELECT COUNT(1) \
            FROM googlehosts.username WHERE Char_Id='%s' " % (pkid)

	        try:
	    		# 执行SQL语句
				cursor.execute(sql)
		    	# 提交到数据库执行
				results = cursor.fetchone()
				if results[0] > 0:
					ret = True
					Log.WriteLog(u"执行“%s”成功！" % (sql))
	    	except Exception, e:
	    		Log.WriteLog(u"错误：无法获取数据！文件\"UserName_DAL.py\"，函数\"IsRxistsByID(mysqlcont, pkid)\"，错误原因：%s" % (e))
	   	cursor.close()
	   	return ret
	except Exception, e:
		Log.WriteLog(u"错误：无法获取数据！文件\"UserName_DAL.py\"，函数\"IsRxistsByID(mysqlcont, pkid)\"，错误原因：%s" % (e))
		return False


#函数名称：IsRxistsByUname
#函数功能：查询VChar_Name是否存在
#函数参数：
#  mysqlcont: 数据库连接
#  uname：用户昵称
#返回值：
#  执行结果(True、False)
def IsRxistsByUname(mysqlcont, uname):
	try:
		# 使用cursor()方法获取操作游标 
		cursor = mysqlcont.cursor()
		ret = False
		sql = "SELECT COUNT(1) \
            FROM googlehosts.username WHERE VChar_Name='%s' " % (uname)

	        try:
	    		# 执行SQL语句
				cursor.execute(sql)
		    	# 提交到数据库执行
				results = cursor.fetchone()
				if results[0] > 0:
					ret = True
					Log.WriteLog(u"执行“%s”成功！" % (sql))
	    	except Exception, e:
	    		Log.WriteLog(u"错误：无法获取数据！文件\"UserName_DAL.py\"，函数\"IsRxistsByUname(mysqlcont, uname)\"，错误原因：%s" % (e))
	   	cursor.close()
	   	return ret
	except Exception, e:
		Log.WriteLog(u"错误：无法获取数据！文件\"UserName_DAL.py\"，函数\"IsRxistsByUname(mysqlcont, uname)\"，错误原因：%s" % (e))
		return False


#函数名称：IsRxistsByEmail
#函数功能：查询VChar_Email是否存在
#函数参数：
#  mysqlcont: 数据库连接
#  email：邮箱地址
#返回值：
#  执行结果(True、False)
def IsRxistsByEmail(mysqlcont, email):
	try:
		# 使用cursor()方法获取操作游标 
		cursor = mysqlcont.cursor()
		ret = False
		sql = "SELECT COUNT(1) \
            FROM googlehosts.username WHERE VChar_Email='%s' " % (email)

	        try:
	    		# 执行SQL语句
				cursor.execute(sql)
		    	# 提交到数据库执行
				results = cursor.fetchone()
				if results[0] > 0:
					ret = True
					Log.WriteLog(u"执行“%s”成功！" % (sql))
	    	except Exception, e:
	    		Log.WriteLog(u"错误：无法获取数据！文件\"UserName_DAL.py\"，函数\"IsRxistsByEmail(mysqlcont, email)\"，错误原因：%s" % (e))
	   	cursor.close()
	   	return ret
	except Exception, e:
		Log.WriteLog(u"错误：无法获取数据！文件\"UserName_DAL.py\"，函数\"IsRxistsByEmail(mysqlcont, email)\"，错误原因：%s" % (e))
		return False


#函数名称：CreateNewPkId
#函数功能：生成一个有用的新主键ID
#函数参数：
#  mysqlcont: 数据库连接
#返回值：
#  ID(长度为30位)
def CreateNewPkId(mysqlcont):
    try:
    	pkid = PrimaryKeyId.CreateNewID() #获取pkid
    	# 使用cursor()方法获取操作游标 
    	cursor = mysqlcont.cursor()
        while 1:
        	#查询pkid是否存在的SQL语句
    		sql_select_id = "select COUNT(*) from username WHERE Char_Id='%s'" %(pkid)
    		
    		# 执行SQL语句
    		cursor.execute(sql_select_id)
        	# 获取所有记录列表
        	results = cursor.fetchone()  #results的值为一个元组

        	if results[0] <= 0 and pkid != None:
        		break
        	else:
        		pkid = PrimaryKeyId.CreateNewID() #获取pkid

        	Log.WriteLog(u"成功生成新主键ID，其为“%s”！" % (pkid))
        cursor.close() #关闭
        return pkid
    except Exception, e:
    	Log.WriteLog(u"错误：主键ID生成失败！文件\"UserName_DAL.py\"，函数\"CreateNewPkId(mysqlcont)\"，错误原因：%s" % (e))
        return None


#函数名称：SelectAllByWhere
#函数功能：按照条件查询所有字段
#函数参数：
#  mysqlcont: 数据库连接
#  where_cont：条件
#返回值：
#  查询结果(元组)，查询失败则为None
def SelectAllByWhere(mysqlcont, where_cont):
	try:
		# 使用cursor()方法获取操作游标 
		cursor = mysqlcont.cursor()
		results = None
		sql = "SELECT Char_Id, VChar_Name, VChar_Email, Bool_IsSend, VChar_GithubUName, VChar_Github, VChar_Address, Text_Oranizations \
            FROM googlehosts.username WHERE %s " % (where_cont)

	        try:
	    		# 执行SQL语句
				cursor.execute(sql)
		    	# 提交到数据库执行
				results = cursor.fetchall()

				Log.WriteLog(u"执行“%s”成功！" % (sql))
	    	except Exception, e:
	    		Log.WriteLog(u"错误：无法获取数据！文件\"UserName_DAL.py\"，函数\"SelectAllByWhere(mysqlcont, where_cont)\"，错误原因：%s" % (e))
	    		results = None
	   	cursor.close()
	   	return results
	except Exception, e:
		Log.WriteLog(u"错误：无法获取数据！文件\"UserName_DAL.py\"，函数\"SelectAllByWhere(mysqlcont, where_cont)\"，错误原因：%s" % (e))
		return None


#函数名称：SelectByWhere
#函数功能：按照条件查询相关字段
#函数参数：
#  mysqlcont: 数据库连接
#  filed_cont：要查询的字段名，可选择(Char_Id, VChar_Name, VChar_Email, Bool_IsSend, VChar_GithubUName, VChar_Github, VChar_Address, Text_Oranizations)
#  where_cont：条件
#返回值：
#  查询结果(元组)，查询失败则为None
def SelectByWhere(mysqlcont, filed_cont, where_cont):
	try:
		# 使用cursor()方法获取操作游标 
		cursor = mysqlcont.cursor()
		results = None
		sql = "SELECT %s \
            FROM googlehosts.username WHERE %s " % (filed_cont, where_cont)

	        try:
	    		# 执行SQL语句
				cursor.execute(sql)
		    	# 提交到数据库执行
				results = cursor.fetchall()

				Log.WriteLog(u"执行“%s”成功！" % (sql))
	    	except Exception, e:
	    		Log.WriteLog(u"错误：无法获取数据！文件\"UserName_DAL.py\"，函数\"SelectByWhere(mysqlcont, filed_cont, where_cont)\"，错误原因：%s" % (e))
	    		results = None
	   	cursor.close()
	   	return results
	except Exception, e:
		Log.WriteLog(u"错误：无法获取数据！文件\"UserName_DAL.py\"，函数\"SelectByWhere(mysqlcont, filed_cont, where_cont)\"，错误原因：%s" % (e))
		return None


#函数名称：AddOne
#函数功能：插入数据
#函数参数：
#  mysqlcont: 数据库连接
#  pkid：主键ID
#  uname：昵称
#  email：邮箱地址
#  issend：是否发送
#  githubuname：github昵称
#  github：github账号
#  address：所在城市
#  org：公司
#返回值：
#  执行结果(True、False)
def AddOne(mysqlcont, pkid, uname, email, issend, githubuname, github, address, org):
	try:
		# 使用cursor()方法获取操作游标 
		cursor = mysqlcont.cursor()
		results = False
		sql = "INSERT INTO googlehosts.username(Char_Id, VChar_Name, VChar_Email, Bool_IsSend, VChar_GithubUName, VChar_Github, VChar_Address, Text_Oranizations) \
	        VALUES ('%s', '%s', '%s', %d, '%s','%s','%s','%s')" % (pkid, uname, email, issend, githubuname, github, address, org)

	        try:
	    		# 执行SQL语句
				cursor.execute(sql)
		    	# 提交到数据库执行
				mysqlcont.commit()
				results = True

				Log.WriteLog(u"执行“%s”成功！" % (sql))
	    	except Exception, e:
	    		Log.WriteLog(u"错误：数据插入失败！文件\"UserName_DAL.py\"，函数\"AddOne(mysqlcont, pkid, uname, email, issend, githubuname, github, address, org)\"，错误原因：%s" % (e))
	    		mysqlcont.rollback() # 数据回滚
	   	cursor.close()
	   	return results
	except Exception, e:
		Log.WriteLog(u"错误：数据插入失败！文件\"UserName_DAL.py\"，函数\"AddOne(mysqlcont, pkid, uname, email, issend, githubuname, github, address, org)\"，错误原因：%s" % (e))
		return False


#函数名称：Update
#函数功能：更新数据
#函数参数：
#  mysqlcont: 数据库连接
#  obj_filed：对象字段名，可选择(Char_Id, VChar_Name, VChar_Email, Bool_IsSend, VChar_GithubUName, VChar_Github, VChar_Address, Text_Oranizations)
#  where_cont：条件，"VChar_Name='%s'" % (old_char)
#  new_chr：新数据
#返回值：
#  执行结果(True、False)
def Update(mysqlcont, obj_filed, where_cont, new_chr):
	try:
		# 使用cursor()方法获取操作游标 
		cursor = mysqlcont.cursor()
		results = False
		sql = "UPDATE googlehosts.username SET %s='%s' \
            WHERE %s " % (obj_filed, new_chr, where_cont)

	        try:
	    		# 执行SQL语句
				cursor.execute(sql)
		    	# 提交到数据库执行
				mysqlcont.commit()
				results = True

				Log.WriteLog(u"执行“%s”成功！" % (sql))
	    	except Exception, e:
	    		Log.WriteLog(u"错误：更新数据失败！文件\"UserName_DAL.py\"，函数\"Update(mysqlcont, obj_filed, where_cont, new_chr)\"，错误原因：%s" % (e))
	   			# 数据回滚
	    		mysqlcont.rollback()
	   	cursor.close()
	   	return results
	except Exception, e:
		Log.WriteLog(u"错误：更新数据失败！文件\"UserName_DAL.py\"，函数\"Update(mysqlcont, obj_filed, where_cont, new_chr)\"，错误原因：%s" % (e))
		return False


#函数名称：UpdateByUname
#函数功能：通过VChar_Name更新数据
#函数参数：
#  mysqlcont: 数据库连接
#  obj_filed：对象字段名，可选择(Char_Id, VChar_Name, VChar_Email, Bool_IsSend, VChar_GithubUName, VChar_Github, VChar_Address, Text_Oranizations)
#  old_char：旧用户名
#  new_char：新用户名
#返回值：
#  执行结果(True、False)
def UpdateByUname(mysqlcont, obj_filed, old_char, new_char):
	try:
		where_cont = "VChar_Name='%s'" % (old_char)
		return Update(mysqlcont, obj_filed, where_cont, new_char)
	except Exception, e:
		Log.WriteLog(u"错误：通过用户名更新数据失败！文件\"UserName_DAL.py\"，函数\"UpdateByUname(mysqlcont, obj_filed, old_char, new_char)\"，错误原因：%s" % (e))
		return False


#函数名称：UpdateByEmail
#函数功能：通过VChar_Email更新数据
#函数参数：
#  mysqlcont: 数据库连接
#  obj_filed：对象字段名，可选择(Char_Id, VChar_Name, VChar_Email, Bool_IsSend, VChar_GithubUName, VChar_Github, VChar_Address, Text_Oranizations)
#  old_char：旧邮箱地址
#  new_char：新邮箱地址
#返回值：
#  执行结果(True、False)
def UpdateByEmail(mysqlcont, obj_filed, old_char, new_char):
	try:
		where_cont = "VChar_Email='%s'" % (old_char)
		return Update(mysqlcont, obj_filed, where_cont, new_char)
	except Exception, e:
		Log.WriteLog(u"错误：通过邮箱地址更新数据失败！文件\"UserName_DAL.py\"，函数\"UpdateByEmail(mysqlcont, obj_filed, old_char, new_char)\"，错误原因：%s" % (e))
		return False


#函数名称：UpdateIsSend
#函数功能：更新Bool_IsSend数据
#函数参数：
#  mysqlcont: 数据库连接
#  where_cont：条件，"VChar_Name='%s'" % (old_char)
#  new_chr：新数据
#返回值：
#  执行结果(True、False)
def UpdateIsSend(mysqlcont, where_cont, new_chr):
	try:
		# 使用cursor()方法获取操作游标 
		cursor = mysqlcont.cursor()
		results = False
		sql = "UPDATE googlehosts.username SET Bool_IsSend=%d \
            WHERE %s " % (new_chr, where_cont)

	        try:
	    		# 执行SQL语句
				cursor.execute(sql)
		    	# 提交到数据库执行
				mysqlcont.commit()
				results = True

				Log.WriteLog(u"执行“%s”成功！" % (sql))
	    	except Exception, e:
	    		Log.WriteLog(u"错误：更新Bool_IsSend数据失败！文件\"UserName_DAL.py\"，函数\"UpdateIsSend(mysqlcont, where_cont, new_chr)\"，错误原因：%s" % (e))
	   			# 数据回滚
	    		mysqlcont.rollback()
	   	cursor.close()
	   	return results
	except Exception, e:
		Log.WriteLog(u"错误：更新Bool_IsSend数据失败！文件\"UserName_DAL.py\"，函数\"UpdateIsSend(mysqlcont, where_cont, new_chr)\"，错误原因：%s" % (e))
		return False


#函数名称：UpdateIsSend2True
#函数功能：更新Bool_IsSend数据为True
#函数参数：
#  mysqlcont: 数据库连接
#  where_cont：条件，"VChar_Name='%s'" % (old_char)
#返回值：
#  执行结果(True、False)
def UpdateIsSend2True(mysqlcont, where_cont):
	try:
		return UpdateIsSend(mysqlcont, where_cont, 1)
	except Exception, e:
		Log.WriteLog(u"错误：更新Bool_IsSend数据为True失败！文件\"UserName_DAL.py\"，函数\"UpdateIsSend2True(mysqlcont, where_cont)\"，错误原因：%s" % (e))
		return False


#函数名称：UpdateIsSend2False
#函数功能：更新Bool_IsSend数据为True
#函数参数：
#  mysqlcont: 数据库连接
#  where_cont：条件，"VChar_Name='%s'" % (old_char)
#返回值：
#  执行结果(True、False)
def UpdateIsSend2False(mysqlcont, where_cont):
	try:
		return UpdateIsSend(mysqlcont, where_cont, 0)
	except Exception, e:
		Log.WriteLog(u"错误：更新Bool_IsSend数据为False失败！文件\"UserName_DAL.py\"，函数\"UpdateIsSend2False(mysqlcont, where_cont)\"，错误原因：%s" % (e))
		return False


#函数名称：DeleteOne
#函数功能：删除一条数据
#函数参数：
#  mysqlcont: 数据库连接
#  where_cont：条件
#返回值：
#  执行结果(True、False)
def DeleteOne(mysqlcont, where_cont):
	try:
		# 使用cursor()方法获取操作游标 
		cursor = mysqlcont.cursor()
		results = False
		sql = "DELETE FROM googlehosts.username WHERE %s " % (where_cont)

	        try:
	    		# 执行SQL语句
				cursor.execute(sql)
		    	# 提交到数据库执行
				mysqlcont.commit()
				results = True

				Log.WriteLog(u"执行“%s”成功！" % (sql))
	    	except Exception, e:
	    		Log.WriteLog(u"错误：删除失败！文件\"UserName_DAL.py\"，函数\"DeleteOne(mysqlcont, where_cont)\"，错误原因：%s" % (e))
	    		mysqlcont.rollback()
	   	cursor.close()
	   	return results
	except Exception, e:
		Log.WriteLog(u"错误：删除失败！文件\"UserName_DAL.py\"，函数\"DeleteOne(mysqlcont, where_cont)\"，错误原因：%s" % (e))
		return False


#函数名称：DeleteList
#函数功能：批量删除
#函数参数：
#  mysqlcont: 数据库连接
#  where_filed：字段名，可选择(Char_Id, VChar_Name, VChar_Email, Bool_IsSend, VChar_GithubUName, VChar_Github, VChar_Address, Text_Oranizations)
#  list_cont：条件
#返回值：
#  执行结果(True、False)
def DeleteList(mysqlcont, where_filed, list_cont):
	try:
		# 使用cursor()方法获取操作游标 
		cursor = mysqlcont.cursor()
		results = False
		sql = "DELETE FROM googlehosts.username WHERE %s in(%s) " % (where_filed, list_cont)

	        try:
	    		# 执行SQL语句
				cursor.execute(sql)
		    	# 提交到数据库执行
				mysqlcont.commit()
				results = True

				Log.WriteLog(u"执行“%s”成功！" % (sql))
	    	except Exception, e:
	   			mysqlcont.rollback() # 数据回滚
	   			Log.WriteLog(u"错误：删除失败！文件\"UserName_DAL.py\"，函数\"DeleteList(mysqlcont, where_filed, list_cont)\"，错误原因：%s" % (e))
	   	cursor.close()
	   	return results
	except Exception, e:
		Log.WriteLog(u"错误：删除失败！文件\"UserName_DAL.py\"，函数\"DeleteList(mysqlcont, where_filed, list_cont)\"，错误原因：%s" % (e))
		return False
