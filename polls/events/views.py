from django.shortcuts import render, redirect
from django.http import request
# Create your views here.


def index(request):
    events = []
 
    if request.method == 'POST':
        event = request.POST.get('events')
        events.append(event)
    return render(request, 'index.html', {'events': events})
    