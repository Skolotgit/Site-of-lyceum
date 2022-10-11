from django.contrib import admin
from .models import Category, Document
from django.utils.safestring import mark_safe
# Register your models here.

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('category_name', 'get_image')
    readonly_fields = ('get_image',)
    search_fields = ('category_name',)
    
    def get_image(self, obj):
        return mark_safe(f'<img src={obj.category_img.url} width="50" height="auto"')

    get_image.short_description = 'Зображення'



@admin.register(Document)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('document_title', 'category')
    list_filter = ('category',)
    search_fields = ('document_title',)

