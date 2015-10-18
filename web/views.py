from django.http import HttpResponse

def home(request):
    return HttpResponse("This is the home page...")

def Page_Not_Found(request):
    return HttpResponse(r"Oh, you is visiting unexist page..")