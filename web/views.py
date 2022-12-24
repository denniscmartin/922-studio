from django.shortcuts import render
from .models import Project


def index(request):
    projects = Project.objects.order_by('-created_date')
    context = {'projects': projects}

    return render(request, 'index.html', context)
