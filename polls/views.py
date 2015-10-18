# Create your views here.
from django.http import HttpResponse
from polls.models import Poll
from django.template import Context
from django.shortcuts import render, get_object_or_404
from django.http.response import Http404

def index(request):
    latest_poll_list = Poll.objects.order_by('-pub_date')
#     output = ','.join([p.question for p in latest_poll_list])
#     template = loader.get_template('polls/index.html')
    context = Context({
                       "latest_poll_list":latest_poll_list
                       })
#     return HttpResponse(template.render(context))
    return render(request, 'polls/index.html', context)

def detail(request, poll_id):
#     try:
#         poll = Poll.objects.get(pk=poll_id)
#     except Poll.DoesNotExist:
#         raise Http404
    poll = get_object_or_404(Poll, pk=poll_id)
    return render(request, 'polls/detail.html', {'poll':poll})
#     return HttpResponse("this poll id is :%s" %poll_id)

# def result

def Page_Not_Found(request):
    return HttpResponse(r"Oh, you is visiting unexist page..")