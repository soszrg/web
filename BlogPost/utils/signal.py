#encoding = utf8

import django.dispatch

send_mail_signal = django.dispatch.Signal(providing_args=['obj'])