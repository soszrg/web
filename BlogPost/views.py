# Create your views here.
from models import BlogPost, User
from django.shortcuts import render
from django.template.context import Context
from django.http.response import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.utils.timezone import now
from httplib import HTTPResponse
from utils import EmailThread

def home_page(request):
    blogs = BlogPost.objects.all()
    context = Context({'blogs':blogs})
    return render(request, "blogpost/index.html", context)
    
def new_blog(request):
    return render(request, "blogpost/new_blog.html", None)

def add_blog(request):
    if request.method != "GET":
        return HTTPResponse("this request is error!") 
    
    title = request.GET['title']
    body = request.GET['body']
    print title,"   ", body, "  ", now()
    new_blog = BlogPost.objects.model(title=title, body=body, timestamp=now())
    new_blog.save()
    return HttpResponseRedirect(reverse("detail", args=(new_blog.id,)))

def detail(request, blog_id):
    blog = BlogPost.objects.get(pk=blog_id)
    context = Context({"blog":blog})
    return render(request,"blogpost/detail.html", context)
    
def register(request):
    return render(request, "blogpost/register.html", None)

def add_user(request):
    user_name = request.GET['user']
    email = request.GET['email']
    
    user = User.objects.model(name=user_name, email=email)
    user.save()
    
    emailThread = EmailThread(to_email=[email], from_email=None, context=None)
    emailThread.start()
    
    return render(request, "blogpost/register_result.html", None)
    
    
    