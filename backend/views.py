from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from backend.models import Article

def home_view(request):
    return HttpResponse("Hello! Aici gasesti raspunsurile pentru tema :))")

def all_object_view(request, articles = None):
    return render(request, articles.html)

def article_list_view(request):
    articles = Article.objects.all()
    context = {}
    context['articles'] = articles
    return render(request, "articles.html", context)

