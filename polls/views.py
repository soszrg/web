# Create your views here.
from django.http import HttpResponse
from django.core.context_processors import request

def index(request):
    return HttpResponse("Hello, world. You're at the poll index.")

def detail(request, poll_id):
    return HttpResponse("this poll id is :%s" %poll_id)

# def result
