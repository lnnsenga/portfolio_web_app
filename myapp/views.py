from django.shortcuts import render

from django.http import HttpResponse
from .models import Project



# Create your views here.

def index(request):
    projects = Project.objects
    return render(request, 'myapp/index.html', {'projects':projects})

