from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name = 'home_page'),
    path('Вступ/', views.admission, name = 'admission_page'),
    path('Публічна_інформація/', views.public_information, name = 'public_information_page'),
    path('Публічна_інформація/<int:document_id>/', views.document_reader, name = 'document_reader_page'),
    path('Новини/', views.new_catalog_of_articles, name = 'new_catalog_of_articles_page'),
    path('Новини/<int:article_id>/', views.article, name = 'new_article_page'),
    path('Історія_закладу/', views.history, name = 'history_page'),
    path('Історія_закладу/Фотографії_з_90-тих/', views.photos_of_90s, name = 'photos_of_90s_page'),
    path('Історія_закладу/Фотографії_з_важливих_подій/', views.old_catalog_of_articles, name = 'old_catalog_of_articles_page'),
    path('Історія_закладу/Фотографії_з_важливих_подій/<int:article_id>/', views.article, name = 'old_article_page'),
    path('Історія_закладу/Відеоматеріали_та_згадки_на_телебаченні/', views.videoteka_on_yt, name = 'videoteka_on_yt_page'),
]