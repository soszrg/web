# Create your views here.
from models import BlogPost, User
from django.shortcuts import render, render_to_response
from django.template.context import Context
from django.http.response import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.utils.timezone import now
from django.http import HttpResponse
from BlogPost.utils.tasks import SendMail
from models import BlogInfo
from django.core.context_processors import csrf 

def home_page(request):
    blogs = BlogPost.objects.all()
    context = Context({'blogs':blogs})
    return render(request, "blogpost/index.html", context)
    
def new_blog(request):
    context = {}
    context.update(csrf(request))
    return render_to_response("blogpost/new_blog.html", context)
#     return render(request, "blogpost/new_blog.html", None)

def add_blog(request):
    if request.method != "POST":
        context = Context({"str":"this request is error!"})
        return render(request, "blogpost/error.html", context) 
    
    title = request.POST['title']
    body = request.POST['body']
    print title,"   ", body, "  ", now()
    new_blog = BlogPost.objects.model(title=title, body=body, timestamp=now())
    new_blog.save()
    print "new:",new_blog.id
    return HttpResponseRedirect(reverse("detail", args=(new_blog.id,)))

def detail(request, blog_id):
    blog = BlogPost.objects.get(pk=blog_id)
    tags = []
    blog_info = None
    try:
        blog_info = BlogInfo.objects.get(blog_id=int(blog_id))
        tags = blog_info.tags.names()
    except Exception as e:
        print "blog[%s] no tag:" %blog_id, e
    
    context = Context({
                       "blog":blog,
                       "tags":tags
                    })
    return render(request,"blogpost/detail.html", context)
    
def register(request):
    return render(request, "blogpost/register.html", None)

def add_user(request):
    user_name = request.GET['user']
    email = request.GET['email']
    pwd = request.GET['pwd']
    obj = None
    try:
        obj = User.objects.get(email=email)
    except Exception as e:
        print e
    if obj is not None:
        return render(request, 'blogpost/error.html', Context({'str':"This email has registered!!"})) 
    user = User.objects.model(name=user_name, email=email, pwd=pwd)
    user.save()
    print "send mail--start"
    SendMail.delay([email])
    print "send mail--stop"
    return render(request, "blogpost/register_result.html", None)

def tag(request, blog_id):
    context = Context({"blog_id":blog_id})
    return render(request, "blogpost/tag.html", context)

def add_tags(request, blog_id):
    tags = request.GET["tags"]
    blog_info, created = BlogInfo.objects.get_or_create(blog_id=blog_id)
    blog_info.tags.clear()
    
    blog = BlogPost.objects.get(id=int(blog_id))
    save_tags = []
    blog_info.tags.add(tags)
    for tag in tags.split(','):
#         blog_info.tags.add(tag)
        save_tags.append(tag)
        
    context = Context({
                       "blog":blog,
                       "tags":save_tags
                    })
    return render(request, 'blogpost/detail.html', context)

def login(request):
    context = {}
    context.update(csrf(request))
    print "login"
    return render(request, "blogpost/login.html", context)
#     return HttpResponse('this is login')

def login_check(request):
        email = request.POST['email']
        pwd = request.POST['pwd']
        obj = None
        try:
            obj = User.objects.get(email=email)
        except Exception as e:
            print e
            print 'error1'
            return render(request, "blogpost/error.html", Context({'str':'This user hasn\'t been registered..'}))
        
        if pwd != obj.pwd:
            return render(request, "blogpost/error.html", Context({'str':'Password is error'}))
#         return HttpResponseRedirect(reverse("BlogPost.views.home_page"))
        return HttpResponseRedirect(reverse("home"))
        
    
def login_usr(request, usr):
    blogs = BlogPost.objects.get(usr=usr)
    
    