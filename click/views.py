from django.http import HttpResponse
from django.shortcuts import render
from .models import Click


def index(request):
    context = {
        'listener_join':Click.listener_join
    }
    return render(request, 'click/index.html', context)
