from django.shortcuts import render
from django.utils.translation import gettext as _
from .models import Project


def index(request):    
    projects = Project.objects.order_by('-created_date')
    context = {'projects': projects}

    return render(request, 'index.html', context)

def privacy(request):
    return render(request, 'privacy.html')