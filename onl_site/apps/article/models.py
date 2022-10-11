from django.db import models

# Create your models here.
 
class Article(models.Model):
    article_title = models.CharField('назва статті', max_length = 200, null=True)
    pub_date = models.DateField('дата публікації', null=True)
    article_preview = models.ImageField('картинка на прев\'ю', upload_to='preview_photos', null=True)
    article_text = models.TextField('текст статті', null=True)
 
    def __str__(self):
        return self.article_title

    class Meta:
        verbose_name = 'Стаття'
        verbose_name_plural = 'Статті'
   
 
 
class ArticleImages(models.Model):
    article = models.ForeignKey(Article, on_delete = models.CASCADE, null=True)
    img = models.ImageField('картинка', upload_to='articles_photos', height_field=None, width_field=None, max_length=100, null=True)
    save_as = True

    class Meta:
        verbose_name = 'Картинка'
        verbose_name_plural = 'Картинки'
    
 
class ArticleYtvideo(models.Model):
    article = models.ForeignKey(Article, on_delete = models.CASCADE, null=True)
    yt_video_src = models.CharField('посилання на відео', max_length = 200, null=True)
    save_as = True
 
    class Meta:
        verbose_name = 'YouTube Відео'
        verbose_name_plural = 'YouTube Відео'
