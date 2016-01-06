from django.core.mail import EmailMessage, send_mail
from django.template import loader
import threading
from web.settings import EMAIL_HOST_USER as from_email

def Signal_Send_Mail(sender, **kwargs):
    print "from:", from_email, "to:", self.to_email
    try:
        send_mail('subject','body',from_email, recipient_list=self.to_email,fail_silently=False)
    except Exception , msg:
        print msg

class EmailThread(threading.Thread):
    def __init__(self, to_email, from_email, context):
        threading.Thread.__init__(self)
        self.to_email = to_email
        self.from_email = from_email
        self.context = context
        
    def run(self):
        print "from:", from_email, "to:", self.to_email
        try:
            send_mail('subject','body',from_email, recipient_list=self.to_email,fail_silently=False)
        except Exception , msg:
            print msg
#         headers = {}
#         msg = EmailMessage(r"Register->blog", "You have registered [zrg] blog..", 
#                            from_email=from_email, to=self.to_email, headers=headers)
#         
# #         msg.content_subtype="html"
#         msg.send()