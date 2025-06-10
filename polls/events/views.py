from django.shortcuts import render, redirect
from django.http import request
from .models import Question, Choice
from django.contrib import messages
from django.core.cache import cache 
from django.conf import settings
from django.core.cache.backends.base import DEFAULT_TIMEOUT
CACHE_TTL = getattr(settings, 'CACHE_TTL', DEFAULT_TIMEOUT)

def index(request):
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    if cache.get('data'):
        d = cache.get('data')
        pl = cache.get('per')
    else:
        d = None
        pl = None
    return render(request, "index.html", {'questions': latest_question_list, 'votes':d, 'percentages':pl})
    
    

def vote(request, question_id):
    total = 100
    c = Question.objects.get(pk=question_id).choice_set.all()
    if request.method == 'POST':
        choice = request.POST.get('vote')
        cc = Choice.objects.get(choice_text=choice)
        cc.votes = cc.votes + 1
        cc.save()
        q = Question.objects.get(pk=question_id)
        ts = q.choice_set.values_list('choice_text')
        vs = q.choice_set.values_list('votes')
        pl = []
        for i in vs:
            p = (i[0] / total)* 100
            
            pl.append(p)
        d = []
        
        for i, j in zip(ts, vs):
            e = f"{i[0]}:   {j[0]}"
            d.append(e)
        cache.set('data', d, CACHE_TTL)
        cache.set('per', pl, CACHE_TTL)
            
        messages.success(request, "You have Voted!")
        return redirect('index')
    else:
        choice= ''
        d = None
        pl = None
    return render(request, 'vote.html', {'choices': c, 'ccc':choice, 'votes':d, 'percentages':pl })
    