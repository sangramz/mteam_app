from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(
        request,
        'mt/index.html',
        {
            'title' : 'Manny\'s team, One stop Point to LEARN & EARN'
        }
    )