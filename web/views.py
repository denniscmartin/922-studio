import json

from django.shortcuts import render
from django.conf import settings
from django.http import Http404

from .models import Project


def index(request, lang='es'):    
    if f'{lang.lower()}.json' not in settings.SUPPORTED_LOCALES:
        raise Http404("Localization not found")

    with open(f'{settings.STATIC_ROOT}/localization/{lang}.json') as f:
        context = json.load(f)

    projects = Project.objects.order_by('-created_date')
    context['projects'] = projects

    return render(request, 'index.html', context)