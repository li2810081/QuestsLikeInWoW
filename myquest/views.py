from django.shortcuts import render

# Create your views here.

from .models import Quest

def index(request):
    quests = Quest.objects.all()
    context = {'quests': quests}
    return render(request, 'index.html', context)
    