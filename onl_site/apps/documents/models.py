from django.db import models

# Create your models here.

class Category(models.Model):
    category_name = models.CharField('назва категорії', max_length = 200, null=True)
    category_img = models.ImageField('картинка', upload_to='document_gradient', height_field=None, width_field=None, max_length=100, null=True)
    def __str__(self):
        return self.category_name

    class Meta:
        verbose_name = 'Категорія'
        verbose_name_plural = 'Категорії'


class Document(models.Model):
    category = models.ForeignKey(Category, on_delete = models.CASCADE, null=True)
    document_title = models.CharField('назва документа', max_length = 200, null=True)
    document_url = models.CharField('посилання на google document', max_length = 400, null=True)


    def __str__(self):
        return self.document_title

    class Meta:
        verbose_name = 'Документ'
        verbose_name_plural = 'Документи'