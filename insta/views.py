from django.shortcuts import render
from django.http  import HttpResponse

# Create your views here.
def welcome(request):
    return render(request, 'welcome.html')


def index(request):
    return render(request, 'all-pages/index.html')
