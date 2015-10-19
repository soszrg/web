# Create your views here.
from django.http import HttpResponse
from polls.models import Poll, Choice
from django.template import Context
from django.shortcuts import render, get_object_or_404
from django.http.response import HttpResponseRedirect
from django.core.urlresolvers import reverse

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

def results(request, poll_id):
    poll = get_object_or_404(Poll, pk=poll_id)
    return render(request, 'polls/results.html', {'poll': poll})

def Page_Not_Found(request):
    return HttpResponse(r"Oh, you is visiting unexist page..")

def vote(request, poll_id):
    p = get_object_or_404(Poll, pk=poll_id)
    try:
        selected_choice = p.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the poll voting form.
        return render(request, 'polls/detail.html', {
            'poll': p,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(p.id,)))