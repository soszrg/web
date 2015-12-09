#encoding:utf8

from celery import task
from BlogPost.utils.mail import EmailThread
from django.core.mail import send_mail
from web.settings import EMAIL_HOST_USER as from_email

@task()
def SendMail(to_mail):
    print "<=====Send Mail=====>"
#     emailThread = EmailThread(to_email=to_mail, from_email=None, context=None)
#     emailThread.start()
    try:
        send_mail('subject','body',from_email, recipient_list=to_mail,fail_silently=False)
    except Exception , msg:
        print msg    
        
    return 0