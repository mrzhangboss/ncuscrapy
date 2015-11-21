# -*- coding: utf-8 -*-
import db_helper
if __name__ == '__main__':  
    if db_helper.send_art_email():  
        print "发送成功"  
        db_helper.send_art_email(to_self=True)
    else:  
        print "发送失败" 
        db_helper.send_art_email(to_self=True)

