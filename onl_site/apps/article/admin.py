from django.contrib import admin
from .models import Article, ArticleImages, ArticleYtvideo
from django.utils.safestring import mark_safe
# Register your models here.

class ArticleImageInline(admin.TabularInline):
    model = ArticleImages

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    inlines = [ArticleImageInline,]
    list_display = ('article_title', 'id')
    search_fields = ('article_title',)

@admin.register(ArticleImages)
class ArticleImagesAdmin(admin.ModelAdmin):
    list_filter = ('article',)
    list_display = ('article', 'get_image')
    readonly_fields = ('get_image',)

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.img.url} width="60px" height="auto"')

    get_image.short_description = 'Зображення'

@admin.register(ArticleYtvideo)
class ArticleYtvideoAdmin(admin.ModelAdmin):
    list_filter = ('article',)
    list_display = ('article',)