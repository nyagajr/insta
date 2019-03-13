from django.shortcuts import render
from django.http  import HttpResponse
import datetime as dt
from .models import Profile,Comments,Image

# Create your views here.
def welcome(request):
    return render(request, 'welcome.html')


def index(request):
    return render(request, 'all-pages/index.html')
