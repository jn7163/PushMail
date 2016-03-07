#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
项目名称：
对象：邮件
用途：发送邮件
时间：2016/3/4 13:37:06
作者: Liuker lt@liuker.xyz
"""

import sys 
import smtplib  
from email.mime.text import MIMEText
import datetime
import time
import UserName_DAL
import Log

reload(sys) 
sys.setdefaultencoding('utf-8')

#函数名称：SendMail
#函数功能：发送邮件
#函数参数：
#  mail_to：收件人
#  mail_subject：邮件主题
#  mail_content：邮件内容
#  mail_host：SMTP服务器
#  mail_user：用户名
#  mail_pass：密码
#  mail_port：端口号
#返回值：
#  发送结果Boolean（True, False）
def SendMail(mail_to, mail_subject, mail_content, mail_host, mail_user, mail_pass, mail_port): 
    # mail_from = "Liuker Team<lt@liuker.xyz>" #可以任意设置，收到信后，将按照设置显示
    mail_from = "Liuker Team<%s>" % (mail_user)
    msg = MIMEText(mail_content, _subtype='html', _charset='UTF-8')  #创建一个实例，这里设置为html格式邮件  gb2312，UTF-8
    msg['Subject'] = mail_subject #邮件主题
    # msg['From'] = mail_from       #发件人
    msg['From'] = "Liuker Team<lt@liuker.xyz>"
    msg['To'] = mail_to           #收件人
    # msg['cc'] = "Liuker<lzq@liuker.xyz>"  #抄送
    try:  
        s = smtplib.SMTP_SSL(mail_host, "%s" % (mail_port))  #连接服务器
        Log.WriteLog(u"连接“%s:%s”服务器成功！" % (mail_host, mail_port))
        # s.set_debuglevel(1)   #显示日志
        s.login(mail_user, mail_pass)   #登录服务器
        Log.WriteLog(u"帐号“%s”登录服务器成功！" % (mail_user))
        s.sendmail(mail_from, mail_to, msg.as_string())   #发送邮件
        Log.WriteLog(u"“%s”给“%s”发送邮件成功！主题：" % (mail_user, mail_to, mail_subject))
        s.close()  
        return True  
    except Exception, e: 
        Log.WriteLog(u"错误：发送邮件失败！文件\"SendMail.py\"，函数\"SendMail(mail_to, mail_subject, mail_content)\"，错误原因：%s" % (e))
        return False  


#函数名称：CreateMailContent
#函数功能：生成邮件主题和内容
#函数参数：
#  logo_url：logo地址
#  download_url：下载地址
#返回值：
#  (mail_subject, mail_content)。mail_subject：邮件主题；mail_content：邮件内容
def CreateMailContent(logo_url, download_url):
    mail_subject = ""
    mail_content = ""
    try:
        now_time = datetime.datetime.now() #获取当前时间
        update_time = now_time.strftime("%Y年%m月%d日")
        mail_subject = "【Hosts更新通知】Google Hosts已更新！By：" + update_time
        
        mail_content = "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD XHTML 1.0 Transitional//EN\" \"http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd\">"
        mail_content += "<html xmlns=\"http://www.w3.org/1999/xhtml\"><head><meta http-equiv=\"Content-Type\" content=\"text/html;charset=utf-8\" /></head>"
        mail_content += "<body style=\"margin:0;\"><table cellpadding=\"0\" cellspacing=\"0\" border=\"0\" width=\"100%\" bgcolor=\"#e1e8ed\" style=\"background-color:#e1e8ed;padding:0;margin:0;line-height:1px;font-size:1px;\" class=\"body_wrapper\"><tbody><tr><td align=\"center\" style=\"padding:0;margin:0;line-height:1px;font-size:1px;\">"
        mail_content += "<table class=\"collapse\" id=\"header\" align=\"center\" width=\"500\" style=\"width:500px;background-color:#ffffff;padding:0;margin:0;line-height:1px;font-size:1px;\" bgcolor=\"#ffffff\" cellpadding=\"0\" cellspacing=\"0\" border=\"0\"><tbody><tr><td height=\"15\" style=\"height:15px;padding:0;margin:0;line-height:1px;font-size:1px;\" class=\"logo_space\">&nbsp;</td></tr><tr align=\"center\"><td style=\"padding:0;margin:0;line-height:1px;font-size:1px;\"><table cellpadding=\"0\" cellspacing=\"0\" border=\"0\" align=\"center\" style=\"padding:0;margin:0;line-height:1px;font-size:1px;\"><tbody><tr align=\"center\"><td align=\"center\" style=\"padding:0;margin:0;line-height:1px;font-size:1px;\"> <a href=\"https://github.com/liuker0x007/hosts\" style=\"text-decoration:none;border-style:none;border:0;padding:0;margin:0;\" target=\"_blank\"><img align=\"center\" src=\""
        mail_content += logo_url  #logo地址
        mail_content += "\" style=\"width:174px;padding-bottom:2px;margin:0;padding:0;display:block;-ms-interpolation-mode:bicubic;border:none;outline:none;\" /></a></td></tr></tbody></table></td></tr><tr><td height=\"14\" style=\"height:14px;padding:0;margin:0;line-height:1px;font-size:1px;\" class=\"logo_space\"> &nbsp;</td></tr></tbody></table>"
        mail_content += "<table class=\"collapse\" align=\"center\" width=\"500\" style=\"width:500px;background-color:#ffffff;padding:0;margin:0;line-height:1px;font-size:1px;\" cellpadding=\"0\" cellspacing=\"0\" border=\"0\"><tbody><tr id=\"border\"><td colspan=\"2\" height=\"1\" style=\"line-height:1px;display:block;height:1px;background-color:#e1e8ed;padding:0;margin:0;line-height:1px;font-size:1px;\"></td></tr></tbody></table>"
        mail_content += "<table class=\"collapse\" align=\"center\" width=\"500\" style=\"width:500px;background-color:#ffffff;padding:0;margin:0;line-height:1px;font-size:1px;\" cellpadding=\"0\" cellspacing=\"0\" border=\"0\"><tbody><tr><td width=\"50\" style=\"width:50px;padding:0;margin:0;line-height:1px;font-size:1px;\" class=\"margins\"></td><td align=\"center\" style=\"padding:0;margin:0;line-height:1px;font-size:1px;\"><table width=\"100%\" align=\"center\" cellpadding=\"0\" cellspacing=\"0\" border=\"0\" class=\"collapse\" style=\"padding:0;margin:0;line-height:1px;font-size:1px;\"><tbody><tr><td height=\"30\" style=\"height:45px;padding:0;margin:0;line-height:1px;font-size:1px;\"></td></tr><tr><td align=\"center\" class=\"display\" style=\"padding:0;margin:0;line-height:1px;font-size:1px;font-family:'Helvetica Neue', Helvetica, Arial, sans-serif;font-size:24px;line-height:30px;font-weight:700;-webkit-font-smoothing:antialiased;-webkit-text-size-adjust:none;text-align:center;color:#292f33;\">互联网是自由平等的！</td></tr><tr><td style=\"height:20px;padding:0;margin:0;line-height:1px;font-size:1px;\"></td></tr><tr><td align=\"center\" class=\"display\" style=\"padding:0;margin:0;line-height:1px;font-size:1px;font-family:'Helvetica Neue', Helvetica, Arial, sans-serif;font-size:18px;line-height:30px;font-weight:300;-webkit-font-smoothing:antialiased;-webkit-text-size-adjust:none;text-align:center;color:#555;\">Hosts值得你拥有！无需翻墙即可让您的Google、Gmail、Twitter、Facebook等各大被墙的网站迅速跑起来。</td></tr><tr><td height=\"30\" style=\"height:30px;padding:0;margin:0;line-height:1px;font-size:1px;\"></td></tr><tr><td align=\"center\" style=\"padding:0;margin:0;line-height:1px;font-size:1px;\"><table border=\"0\" cellspacing=\"0\" cellpadding=\"0\" style=\"padding:0;margin:0;line-height:1px;font-size:1px;\"><tbody><tr><td style=\"padding:0;margin:0;line-height:1px;font-size:1px;\"><table width=\"100%\" border=\"0\" cellspacing=\"0\" cellpadding=\"0\" style=\"padding:0;margin:0;line-height:1px;font-size:1px;\"><tbody><tr><td style=\"padding:0;margin:0;line-height:1px;font-size:1px;\"><table border=\"0\" cellspacing=\"0\" cellpadding=\"0\" style=\"padding:0;margin:0;line-height:1px;font-size:1px;\"><tbody><tr><td align=\"center\" bgcolor=\"#55acee\" style=\"padding:0;margin:0;line-height:1px;font-size:1px;-webkit-border-radius:4px;-moz-border-radius:4px;border-radius:4px;line-height:18px;\"><a href=\""
        mail_content += download_url  #hosts下载地址
        mail_content += "\" download=\"hosts.zip\" target=\"_blank\" class=\"bulletproof-btn-2\" style=\"text-decoration:none;border-style:none;border:0;padding:0;margin:0;font-family:'Helvetica Neue', Helvetica, Arial, sans-serif;font-size:16px;line-height:22px;font-weight:500;-webkit-font-smoothing:antialiased;-webkit-text-size-adjust:none;color:#ffffff;text-align:center;text-decoration:none;-webkit-border-radius:4px;-moz-border-radius:4px;border-radius:4px;padding:11px 40px;border:1px solid #55acee;display:inline-block;\"><strong>立即下载</strong></a></td></tr></tbody></table></td></tr></tbody></table></td></tr></tbody></table></td></tr><tr><td align=\"center\" class=\"display\" style=\"padding:0;margin:0;line-height:1px;font-size:1px;font-family:'Helvetica Neue', Helvetica, Arial, sans-serif;font-size:12px;line-height:30px;font-weight:300;-webkit-font-smoothing:antialiased;-webkit-text-size-adjust:none;text-align:center;color:#aaa;\">更新时间："
        mail_content += update_time  #更新时间
        mail_content += "</td></tr><tr><td height=\"55\" style=\"height:55px;padding:0;margin:0;line-height:1px;font-size:1px;\"></td></tr></tbody></table></td><td width=\"50\" style=\"width:50px;padding:0;margin:0;line-height:1px;font-size:1px;\" class=\"margins\"></td></tr></tbody></table>"
        mail_content += "<table class=\"collapse\" id=\"footer\" align=\"center\" width=\"500\" style=\"width:500px;background-color:#ffffff;padding:0;margin:0;line-height:1px;font-size:1px;\" cellpadding=\"0\" cellspacing=\"0\" border=\"0\"><tbody><tr><td height=\"1\" style=\"line-height:1px;display:block;height:1px;background-color:#e1e8ed;padding:0;margin:0;line-height:1px;font-size:1px;\"></td></tr><tr><td height=\"20\" style=\"height:20;padding:0;margin:0;line-height:1px;font-size:1px;\"></td></tr><tr><td align=\"center\" style=\"padding:0;margin:0;line-height:1px;font-size:1px;\"><span class=\"footer_type\" style=\"font-family:'Helvetica Neue Light', Helvetica, Arial, sans-serif;-webkit-font-smoothing:antialiased;color:#8899a6;font-size:12px;padding:0px;margin:0px;font-weight:normal;line-height:12px;\"><a href=\"https://github.com/liuker0x007/hosts/blob/master/README.md\" class=\"footer_link\" style=\"text-decoration:none;border-style:none;border:0;padding:0;margin:0;font-family:'Helvetica Neue Light', Helvetica, Arial, sans-serif;-webkit-font-smoothing:antialiased;-webkit-text-size-adjust:none;color:#55acee;font-size:12px;padding:0px;margin:0px;font-weight:600;line-height:12px;\" target=\"_blank\">需要帮助吗?</a></span><span class=\"footer_type\" style=\"font-family:'Helvetica Neue Light', Helvetica, Arial, sans-serif;-webkit-font-smoothing:antialiased;color:#8899a6;font-size:12px;padding:0px;margin:0px;font-weight:normal;line-height:12px;\"><a href=\"https://github.com/liuker0x007/hosts/issues/new\" class=\"footer_link\" style=\"text-decoration:none;border-style:none;border:0;padding:0;margin:0;font-family:'Helvetica Neue Light', Helvetica, Arial, sans-serif;-webkit-font-smoothing:antialiased;-webkit-text-size-adjust:none;color:#55acee;font-size:12px;padding:0;margin:0px;margin-left:20px;font-weight:600;line-height:12px;\" target=\"_blank\">反馈问题嘞！</a></span></td></tr><tr><td height=\"10\" style=\"height:10px;line-height:1px;font-size:1px;padding:0;margin:0;line-height:1px;font-size:1px;\"></td></tr><tr><td align=\"center\" style=\"padding:0;margin:0;line-height:1px;font-size:1px;\"> <span class=\"address\"> <a href=\"\" style=\"text-decoration:none;border-style:none;border:0;padding:0;margin:0;font-family:'Helvetica Neue Light', Helvetica, Arial, sans-serif;-webkit-font-smoothing:antialiased;color:#8899a6;font-size:12px;padding:0px;margin:0px;font-weight:normal;line-height:12px;cursor:default;\">Copyright (c) 2015 - 2016, ]Liuker Team[.</a> </span> </td></tr><tr><td height=\"26\" style=\"height:26;padding:0;margin:0;line-height:1px;font-size:1px;\"></td></tr></tbody></table>"
        mail_content += "</td></tr></tbody></table></body></html>"

        Log.WriteLog(u"邮件主题和内容创建成功！")

        return (mail_subject, mail_content)
    except Exception, e: 
        Log.WriteLog(u"错误：邮件主题和内容创建失败！文件\"SendMail.py\"，函数\"CreateMailContent(logo_url, download_url)\"，错误原因：%s" % (e))
        return (mail_subject, mail_content)


#函数名称：PushMail
#函数功能：群发邮件
#函数参数：
#  mysqlcont：数据库连接
#  logo_url：logo地址
#  download_url：下载地址
#  mail_servers：邮箱服务器信息
#返回值：
#  
def PushMail(mysqlcont, logo_url, download_url, mail_servers):
    num_total = 0
    num_success = 0
    num_fail = 0
    try:
        (mail_subject, mail_content) = CreateMailContent(logo_url, download_url) #获取邮件主题和邮件内容
        if len(mail_subject) > 0 and len(mail_content) > 0:
            where_cont = " Bool_IsSend=1 and VChar_Email <>'' "
            results = UserName_DAL.SelectAllByWhere(mysqlcont, where_cont)

            server_total = len(mail_servers) #总邮箱服务器数
            si = 0 # 用于记录服务器序号

            for row in results:

                num_total += 1 #统计总记录

                #读取收件人信息
                uname = row[1]
                mail_to = row[2]
                issend = row[3]

                #读取邮箱服务器信息
                mail_host = mail_servers[si][0]
                mail_user = mail_servers[si][1]
                mail_pass = mail_servers[si][2]
                mail_port = mail_servers[si][3]

                # 休息5秒钟
                time.sleep(5)

                if len(mail_to) > 0 and issend == 1:
                    # SendMail(mail_to, mail_subject, mail_content, mail_host, mail_user, mail_pass, mail_port)
                    if SendMail(mail_to, mail_subject, mail_content, mail_host, mail_user, mail_pass, mail_port):
                        print u"%s(%s) -> 发送成功" % (uname, mail_to)
                        Log.WriteLog(u"No.%d %s(%s) -> 发送成功" % (num_total, uname, mail_to))
                        num_success += 1
                    else:
                        print u"%s(%s) -> 发送失败" % (uname, mail_to)
                        Log.WriteLog(u"No.%d %s(%s) -> 发送失败" % (num_total, uname, mail_to))
                        num_fail += 1
                elif len(mail_to):
                    print u"%s(%s) -> 空" % (uname, mail_to)
                    Log.WriteLog(u"No.%d %s(%s) -> 空" % (num_total, uname, mail_to))
                    num_fail += 1
                elif issend == 0:
                    print u"%s(%s) -> 空" % (uname, mail_to)
                    Log.WriteLog(u"No.%d %s(%s) -> 空" % (num_total, uname, mail_to))
                    num_fail += 1
                else:
                    num_fail += 1
                    print u"网络错误！"
                    Log.WriteLog(u"网络错误！")

                si += 1
                if si >= server_total:
                	si = 0

            print u"发送成功 %d 个，发送失败 %d 个，共 %d 个。" % (num_success, num_fail, num_total)
            Log.WriteLog(u"发送成功 %d 个，发送失败 %d 个，共 %d 个。" % (num_success, num_fail, num_total))
        else:
            Log.WriteLog(u"邮件主题和邮件内容不能为空！")
    except Exception, e:
        Log.WriteLog(u"错误：群发邮件失败！文件\"SendMail.py\"，函数\"PushMail(mysqlcont, mail_host, mail_user, mail_pass, mail_postfix, logo_url, download_url)\"，错误原因：%s" % (e))