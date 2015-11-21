# -*- coding: utf-8 -*-
import smtplib  
from email.mime.text import MIMEText  
mailto_list_my=["ncuadmin@163.com"] 
mailto_list=["2529450174@qq.com","1506785369@qq.com","953861612@qq.com","1192966961@qq.com"] 
mail_host="smtp.163.com"  #设置服务器
mail_user="ncuadmin"    #用户名
mail_pass="ncu2009"   #口令 
mail_postfix="163.com"  #发件箱的后缀
  
def send_mail(sub,content,to_self=False):  #to_list：收件人；sub：主题；content：邮件内容
    if to_self:
    	global mailto_list
    	global mailto_list_my
        mailto_list=mailto_list_my
    me=mail_user+"@"+mail_postfix+">"   #这里的hello可以任意设置，收到信后，将按照设置显示
    msg = MIMEText(content,_subtype='html',_charset='utf-8')    #创建一个实例，这里设置为html格式邮件
    msg['Subject'] = sub    #设置主题
    msg['From'] = me  
    msg['To'] = ";".join(mailto_list)  
    try:  
        s = smtplib.SMTP()  
        s.connect(mail_host)  #连接smtp服务器
        s.login(mail_user,mail_pass)  #登陆服务器
        s.sendmail(me, mailto_list, msg.as_string())  #发送邮件
        s.close()  
        return True  
    except Exception, e:  
        print str(e)  
        return False  

