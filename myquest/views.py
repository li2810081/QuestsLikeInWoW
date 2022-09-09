from django.shortcuts import render

from django.core import serializers
# Create your views here.

from .models import Quest

def index(request):
    quests = Quest.objects.all()
    # 转化为json并序列化
    data = list(quests.values())
    context = {'quests': quests,"jsondata":data}
    return render(request, 'index.html', context)
    