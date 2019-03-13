from django.contrib.auth.decorators import login_required
from .forms import NewsLetterForm
from django.shortcuts import render
from django.http  import HttpResponse
import datetime as dt
from .models import Profile,Comments,Image

# Create your views here.
@login_required(login_url='/accounts/login/')
def welcome(request):
    query_img = Image.objects.all()
    return render(request, 'welcome.html', {"query_img":query_img})


def index(request):
    return render(request, 'all-pages/index.html')

# def logout(request):
#     return render(request, 'registration/registration_form.html')

def search_results(request):

    if 'article' in request.GET and request.GET["article"]:
        search_term = request.GET.get("article")
        searched_articles = Article.search_by_title(search_term)
        message = f"{search_term}"

        return render(request, 'all-pages/search.html',{"message":message,"articles": searched_articles})

    else:
        message = "You haven't searched for any term"
        return render(request, 'all-pages/search.html',{"message":message})

    if request.method == 'POST':
        form = NewsLetterForm(request.POST)
        if form.is_valid():
            print('valid')
    else:
        form = NewsLetterForm()
    return render(request, 'templates/welcome.html', {"letterForm":form})
