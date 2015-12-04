# Create your views here.
from models import BlogPost
from django.shortcuts import render
from django.template.context import Context

def home_page(request):
    blogs = BlogPost.objects.all()
    context = Context({'blogs':blogs})
    return render(request, "blogpost/index.html", context)
    
def new_blog(request):
    return render(request, "blogpost/new_blog.html", None)

def detail(request, blog_id):
    blog = BlogPost.objects.get(pk=blog_id)
    context = Context({"blog":blog})
    return render(request,"blogpost/detail.html", context)
    