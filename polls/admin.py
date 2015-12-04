#encoding=utf-8

from django.contrib import admin
from polls.models import Poll, Choice
from BlogPost.models import BlogPost

class ChoiceInline(admin.TabularInline):
    model=Choice
    extra=1

class PollAdmin(admin.ModelAdmin):
#     fields=['pub_date', 'question']
    fieldsets=[
              ('Question', {'fields':['question']}),
              ('Date information', {'fields':['pub_date']}),
            ]
    inlines = [ChoiceInline]
    
admin.site.register(Poll, PollAdmin)
admin.site.register(BlogPost)
# admin.site.register(Choice)
