from django.shortcuts import render
from .models import matchez
# Create your views here.


def index(request):

    matchs=matchez.objects.all()
    return render(request, 'matches/index.html', {'matchs': matchs})