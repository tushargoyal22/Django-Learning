
from django.shortcuts import render
from main import models

# Create your views here.

def index(request):

    # latest_articles=models.Article.objects.all()[:10]
    # to fetch artciles in order of time
    latest_articles=models.Article.objects\
    .all()\
    .order_by('-createdAt')[:10]


    context={
        'articles':latest_articles
    }
    return render(request, 'main/index.html',context)


def article(request,pk):
    article=models.Article.objects.get(pk=pk)

    context={
        'articel':article
    }

    return render(request,'main/article.html',context)