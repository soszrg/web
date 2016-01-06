#encoding:utf8

from celery import task, Celery
# from BlogPost.utils.mail import EmailThread
# from django.core.mail import send_mail
# from web.settings import EMAIL_HOST_USER as from_email
# from celery import shared_task

from celeryApp import app
# @app.task()
# def SendMail(to_mail):
#     print "<=====Send Mail=====>"
# #     emailThread = EmailThread(to_email=to_mail, from_email=None, context=None)
# #     emailThread.start()
#     try:
#         send_mail('subject','body',from_email, recipient_list=to_mail,fail_silently=False)
#     except Exception , msg:
#         print msg    
#          
#     return 0

@app.task()
# @task
def Add1(x, y):
    print "===>win:Add1<==="
    return x+y+1

# @app.task()
# def Add2(x, y):
#     print "===>win:Add2<==="
#     return x+y+2
# 
# @app.task()
# def Add3(x, y):
#     print "===>ubu:Add3<==="
#     return x+y+1
#  
# @app.task()
# def Add4(x, y):
#     print "===>ubu:Add4<==="
#     return x+y+2

