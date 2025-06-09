from django.shortcuts import render, redirect
from django.http import request
# Create your views here.
from .models import Question, Choice
from .forms import choices
from django.contrib import messages

    

def index(request):
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    
    return render(request, "index.html", {'questions': latest_question_list})
    
    
"""def detail(request, question_id):
    
    instance = Question.objects.get(id=question_id).choice_set.values_list("id", "choice_text")
    
    if request.method == 'POST':
        form = choices(request.POST or None, initial={'result': instance})
        if form.is_valid():
            vote = form.cleaned_data.get('choice')
            c = Choice.objects.get(choice_text=vote)
            c.votes = c.votes+1
            messages.success(request, "You have Voted!")
            #redirect('index')
            
    else:
        form= choices()
    #return render(request, "question.html", {'form': form})
"""
def vote(request, question_id):
    c = Question.objects.get(pk=question_id).choice_set.all()
    if request.method == 'POST':
        choice = request.POST.get('vote')
        cc = Choice.objects.get(choice_text=choice)
        cc.votes = cc.votes + 1
        cc.save()
        messages.success(request, "You have Voted!")
        #return redirect('index')
    else:
        choice= ''
    return render(request, 'vote.html', {'choices': c, 'ccc':choice})