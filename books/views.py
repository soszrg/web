# Create your views here.
from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, render_to_response
from models import Book, Author, Publisher
from django.core.mail import send_mail
from web.settings import EMAIL_HOST_USER
from books.forms import ContractForm, AuthorForm, BookForm, PubForm
from django.core.urlresolvers import reverse
from django.contrib.sessions.models import Session

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required

@login_required(login_url='auth_login')
def home_page(request):
#     print request.session.keys['']
    print request.user.is_authenticated()
    res = HttpResponse("<html><body>this is books home page..</body></html>")
    if request.session.test_cookie_worked():
        session_id = request.COOKIES['sessionid']
        print session_id
        session = Session.objects.get(session_key=session_id)
        print session.session_data
        print session.get_decoded()
#         request.session.delete_test_cookie()
        res = HttpResponse('cookie is worked.')
        return res
    else:
        request.session.set_test_cookie()
        res = HttpResponse('open cookie.')
        res.set_cookie('mykey', 'myvalue')
        return res
    return res

def register(request):
    form = None
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            return HttpResponseRedirect(reverse("home_page"))
    else:
        form = UserCreationForm()
    
    return render_to_response('registration/register.html',{'form':form})        
    
# def login(request):
    
    
# def logout(request):
#     return HttpResponse('logout')

def search(request):
    error = []
    if 'q' in request.GET:
        q = request.GET['q']
        if not q:
            error = "Plz input a search term."
        elif len(q) > 20:
            error = "Plz input most 20 characters."
        else:
            books = Book.objects.filter(title__icontains=q)
            return render_to_response('search_results.html',
                {'books': books, 'query': q})
    return render_to_response('search_form.html',
        {'error': error})
    
# def contract(request):
#     errors = []
#     from_mail = ''
#     if request.method == 'POST':
#         if not request.POST.get('title', ''):
#             errors.append('Enter a title')
#         from_mail = request.POST.get('email', '')
#         if from_mail and '@' not in request.POST['email']:
#             errors.append('Enter a valid email')
#         if not request.POST.get('message', ''):
#             errors.append('Enter the message')
#         
#         print 'email:',request.POST.get('email', 'zrg1231@126.com')
#         if not from_mail:
#             from_mail = 'zrg1231@126.com'
#         if not errors:
#             print request.POST['title'], request.POST['message'], from_mail, [EMAIL_HOST_USER]
#             send_mail(request.POST['title'], request.POST['message'], from_mail, [EMAIL_HOST_USER])
#             return HttpResponse('Thanks for your advice.')
#         
#     return render_to_response('contract_us.html', {'errors':errors, 
#                                                    'title':request.POST.get('title',''),
#                                                    'email':request.POST.get('email',''),
#                                                    'message':request.POST.get('message','')
#                                                    })

def thanks(request,str):
    return render_to_response('thanks.html', {'str':str})

def contract(request):
#     errors = []
    form = ''
    if request.method == 'POST':
        form = ContractForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            from_mail = cd.get('email', 'zrg1231@126.com')
            if not from_mail or from_mail is 'This is optional':
                from_mail = 'zrg1231@126.com'
            print request.POST['title'], request.POST['message'], from_mail, [EMAIL_HOST_USER]
            send_mail(cd['title'], cd['message'], from_mail, [EMAIL_HOST_USER])
#             return HttpResponse('Thanks for your advice.')
            return HttpResponseRedirect(reverse('thanks', args=('Thanks for your advice',)))
    else:
        form = ContractForm(initial={'title':'Enter one title', 'email':'zrg1231@126.com', 'message':'Enter one message'})
    return render_to_response('contract_us.html', {'form':form})

def form_check(func):
    def inner(req, *args, **kwargs):
        form = ''
        if req.method == 'POST':
            print 'inn post'
            form = func(req, *args, **kwargs)
        else:
            print 'inn form'
            type = kwargs.pop('form')
            form = type()
        if form.is_valid():
            return HttpResponseRedirect(reverse('thanks', args=('Adding new item',)))
        else:
            return render_to_response('add.html', {'form':form})
    return inner

@form_check    
def new_item(request, *args, **kwargs):
    errors=[]
    type = kwargs.pop('type')
    if type == 'author':
        form = AuthorForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            author = Author(first_name=cd.get('first_name'), last_name=cd['last_name'], email=cd['email'])
            author.save()
            
    elif type == 'publisher':
        form = PubForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            print cd
            pub = Publisher(name=cd['name'], address=cd['address'], city=cd['city'], state_province=cd['state_province'], country=cd['country'], website=cd['website'])
            pub.save()
        
    elif type == 'book':
        form = BookForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            print cd
            names = cd['authors'].split(',')
            pub_name = cd['publisher']
            pub = ''
            try:
                pub = Publisher.objects.get(name=pub_name.strip())
            except Exception:
                print 'Publisher[%s] not exist.' %pub_name
                
            book = Book(title=cd['title'], publisher=pub, publication_date=cd['pub_date'])
            book.save()
            for name in names:
                try:
                    author = Author.objects.get(first_name=name.strip())
                    print author
                    book.authors.add(author)
                except Exception as e:
                    print e
                    print 'Author[%s] not exist.' %name
            
#                     errors.append('%s not exist.' %name)
#             book = Book(title=cd['title'], )

    return form
        
        