import datetime
from django.utils import timezone
from unicodedata import category
from django.shortcuts import render
from django.core.paginator import Paginator
from django.utils.safestring import mark_safe
from documents.models import Category, Document
from article.models import Article, ArticleImages, ArticleYtvideo
from django.http import Http404
# Create your views here.

def page_not_found_view(request, exception):
    return render(request, 'error404.html', status=404)

def home(request):
    articles = Article.objects.order_by('-pub_date')[:3]
    slider = Article.objects.get(id = 22)
    images = ArticleImages.objects.order_by()
    return render(request, 'home.html', {'articles' : articles, 'slider' : slider, 'images' : images})

def admission(request):
    return render(request, 'admission.html')

def public_information(request):
    categories = Category.objects.order_by()[:6]
    documents = Document.objects.order_by()
    return render(request, 'public_information.html', {'categories' : categories, 'documents' : documents})

def document_reader(request, document_id):
    try:
        doc = Document.objects.get( id = document_id)
    except:
        raise Http404("Документ не знайдений!")
    return render(request, 'document_reader.html', {'document' : doc})

def new_catalog_of_articles(request):
    articles = Article.objects.order_by('-pub_date')
    new_articles = articles.filter(pub_date__gte = timezone.now() - datetime.timedelta(days = 365), pub_date__year__gt = 1980)
    paginator = Paginator(new_articles, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'new_catalog_of_articles.html', {'page_obj' : page_obj, 'paginator' : paginator})    

def history(request):
    return render(request, 'history.html')

def photos_of_90s(request):
    article = Article.objects.get(id = 18)
    title = mark_safe(article.article_title)
    images = ArticleImages.objects.filter(article=article)
    return render(request, 'photos_of_90s.html', {'article' : article, 'images' : images, 'title' : title})

def old_catalog_of_articles(request):
    articles = Article.objects.order_by('-pub_date')
    old_articles = articles.filter(pub_date__lt = timezone.now() - datetime.timedelta(days = 365), pub_date__year__gt = 1980)
    paginator = Paginator(old_articles, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'old_catalog_of_articles.html', {'page_obj' : page_obj, 'paginator' : paginator})

def videoteka_on_yt(request):
    video_article = Article.objects.get(id = 19)
    title = mark_safe(video_article.article_title)
    videos = ArticleYtvideo.objects.filter(article = video_article)
    paginator = Paginator(videos, 3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'video_yt.html', {'page_obj' : page_obj, 'paginator' : paginator, 'title' : title})

def article(request, article_id):
    try:
        article = Article.objects.get(id = article_id)
        text = mark_safe(article.article_text)
    except:
        raise Http404("Статті не знайдено!")
    images = ArticleImages.objects.filter(article=article)
    videos = ArticleYtvideo.objects.filter(article=article)
    return render(request, 'article.html', {'article' : article, 'text' : text, 'images' : images, 'videos' : videos})
