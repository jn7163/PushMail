#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
项目名称：
对象：
用途：群发邮件
时间：2016/3/4 13:35:43
作者: Liuker lt@liuker.xyz
"""



import sys
import DbConnect
import SendMail
import UserName_DAL
import MailServerConfig
import datetime
import Log

reload(sys) 
sys.setdefaultencoding('utf-8')


logo_url = "data:image/gif;base64,R0lGODlhrgAcAPf/AAoKCjIyMh8fHxYWFgQEBAICAl9fXwAAAP7+/nNzc6Kiovj4+P39/f8DA3l5efr6+r29vb+/v6+vr/b29mtra+Xl5U1NTWhoaMxpaewlJQ0NDfn5+W9vb+fn5+3t7f///zU1NWRkZNvb29ra2ouLi25ubvT09A8PD1lZWfz8/JGRkWpqaqenp7a2tru7u4aGhhMTE3Z2dmlpaZCQkHR0dG1tbYODg9LS0omJiff3915eXvDw8MzMzGBgYLi4uN3d3WZmZu/v74qKio2NjaioqPv7+8bGxmdnZxgYGCYmJiAgIJaWlnh4eLW1tfHx8ZKSkiMjI5ubm+7u7vX19YeHh8XFxY6OjmFhYdfX18LCwsDAwK2trampqVVVVbGxsXV1dYyMjHd3d6GhoePj47S0tObm5nBwcI+Pj+rq6jk5OfMZGfLy8hkZGdPT08/Pz7CwsFhYWJ2dnbOzsxAQEICAgCIiIhISEre3t/Pz8319fUFBQcrKyl1dXeDg4ISEhCgoKDY2NiUlJQcHBy8vL8CNjcxqapqamuwmJpWVlSQkJJiYmGNjYzo6Or6+vmVlZa6urp+fn4WFhdnZ2d/f33t7e39/f5ycnLq6utzc3Onp6cfHx5SUlMTExFtbW8vLy+jo6NXV1djY2IiIiNTU1FZWVp6ennx8fM3NzcnJySkpKXFxcaqqqpeXl1JSUk9PTw4ODioqKisrK7y8vFFRUc65udPAwDc3N+8fHz09PdbJycCLi8VsbNTExL+BgZmZmc9aWrm5uebi4uTk5MZhYfQYGFNTU8PDw/Py8uojI+zs7N8zM8B0dMZyctk9PUhISOHh4caPj3Jycjs7O+vo6PoNDf8ICOYqKuLi4ujk5KampsV7e0dHR8Z0dMq0tNbW1v8MDGJiYvAfH860tMHBwc7OzqysrNDAwIKCgsCFhd7e3rKyssjIyKurqz8/PxsbG0RERCwsLHp6elRUVM1ZWecoKOYlJecnJ+0eHh0dHb9xcb9ycicnJ1BQUCEhIQEBAf///yH/C1hNUCBEYXRhWE1QPD94cGFja2V0IGJlZ2luPSLvu78iIGlkPSJXNU0wTXBDZWhpSHpyZVN6TlRjemtjOWQiPz4gPHg6eG1wbWV0YSB4bWxuczp4PSJhZG9iZTpuczptZXRhLyIgeDp4bXB0az0iQWRvYmUgWE1QIENvcmUgNS4wLWMwNjAgNjEuMTM0Nzc3LCAyMDEwLzAyLzEyLTE3OjMyOjAwICAgICAgICAiPiA8cmRmOlJERiB4bWxuczpyZGY9Imh0dHA6Ly93d3cudzMub3JnLzE5OTkvMDIvMjItcmRmLXN5bnRheC1ucyMiPiA8cmRmOkRlc2NyaXB0aW9uIHJkZjphYm91dD0iIiB4bWxuczp4bXBNTT0iaHR0cDovL25zLmFkb2JlLmNvbS94YXAvMS4wL21tLyIgeG1sbnM6c3RSZWY9Imh0dHA6Ly9ucy5hZG9iZS5jb20veGFwLzEuMC9zVHlwZS9SZXNvdXJjZVJlZiMiIHhtbG5zOnhtcD0iaHR0cDovL25zLmFkb2JlLmNvbS94YXAvMS4wLyIgeG1wTU06T3JpZ2luYWxEb2N1bWVudElEPSJ4bXAuZGlkOkM4MjU4OURBMkU2M0U1MTE4N0EzQzMwQjQ3NDVFQjU1IiB4bXBNTTpEb2N1bWVudElEPSJ4bXAuZGlkOjhDNTYwQ0U1REJBMzExRTU5NTBDRjNENEFFQ0M3MzcyIiB4bXBNTTpJbnN0YW5jZUlEPSJ4bXAuaWlkOjhDNTYwQ0U0REJBMzExRTU5NTBDRjNENEFFQ0M3MzcyIiB4bXA6Q3JlYXRvclRvb2w9IkFkb2JlIFBob3Rvc2hvcCBDUzUgV2luZG93cyI+IDx4bXBNTTpEZXJpdmVkRnJvbSBzdFJlZjppbnN0YW5jZUlEPSJ4bXAuaWlkOjg5MzEzRjE0MzVDMEU1MTE4RTM0ODdGM0ZCQjc1MTFGIiBzdFJlZjpkb2N1bWVudElEPSJ4bXAuZGlkOkM2MjU4OURBMkU2M0U1MTE4N0EzQzMwQjQ3NDVFQjU1Ii8+IDwvcmRmOkRlc2NyaXB0aW9uPiA8L3JkZjpSREY+IDwveDp4bXBtZXRhPiA8P3hwYWNrZXQgZW5kPSJyIj8+Af/+/fz7+vn49/b19PPy8fDv7u3s6+rp6Ofm5eTj4uHg397d3Nva2djX1tXU09LR0M/OzczLysnIx8bFxMPCwcC/vr28u7q5uLe2tbSzsrGwr66trKuqqainpqWko6KhoJ+enZybmpmYl5aVlJOSkZCPjo2Mi4qJiIeGhYSDgoGAf359fHt6eXh3dnV0c3JxcG9ubWxramloZ2ZlZGNi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" #logo地址
download_url = "https://github.com/liuker0x007/hosts"  #hosts下载地址
# download_url = "https://raw.githubusercontent.com/liuker0x007/hosts/master/hosts" #hosts下载地址

try:
	# 连接数据库
	mysqlcont = DbConnect.Connect2DB('127.0.0.1', 'root', '123123', 'googlehosts')

	# 设置Bool_IsSend=0
	# where_cont="Bool_IsSend=1"
	# UserName_DAL.UpdateIsSend2False(mysqlcont, where_cont)

	# 设置Bool_IsSend=1
	# where_cont="Bool_IsSend=0"
	# UserName_DAL.UpdateIsSend2True(mysqlcont, where_cont)


	# 读取邮箱服务器信息
	file_path = "c:\PushMail\Src\MailServerConfig.txt"
	Log.WriteLog(u"读取“%s”文件中的邮箱服务器信息" % file_path)
	mail_servers = MailServerConfig.Save2Matrix(file_path)

	# 调用群发邮件接口 PushMail(mysqlcont, logo_url, download_url, mail_servers, rows, cols)
	Log.WriteLog(u"调用群发邮件接口 PushMail(mysqlcont, logo_url, download_url, mail_servers)")
	SendMail.PushMail(mysqlcont, logo_url, download_url, mail_servers)

	# 关闭数据库连接
	DbConnect.Close2DB(mysqlcont)

	print u"全部推送完毕！"
	Log.WriteLog(u"全部推送完毕！\n")
except Exception, e:
	print str(e)
	Log.WriteLog(u"错误：推送失败！错误原因：%s" % (e))
	print u"推送失败！"
