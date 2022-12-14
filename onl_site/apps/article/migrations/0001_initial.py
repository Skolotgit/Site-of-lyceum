# Generated by Django 4.0.5 on 2022-07-26 20:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('article_title', models.CharField(max_length=200, null=True, verbose_name='назва статті')),
                ('pub_date', models.DateField(null=True, verbose_name='дата публікації')),
                ('article_preview', models.ImageField(null=True, upload_to='preview_photos', verbose_name="картинка на прев'ю")),
                ('article_text', models.TextField(null=True, verbose_name='текст статті')),
            ],
            options={
                'verbose_name': 'Стаття',
                'verbose_name_plural': 'Статті',
            },
        ),
        migrations.CreateModel(
            name='ArticleYtvideo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('yt_video_src', models.CharField(max_length=200, null=True, verbose_name='посилання на відео')),
                ('article', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='article.article')),
            ],
            options={
                'verbose_name': 'YouTube Відео',
                'verbose_name_plural': 'YouTube Відео',
            },
        ),
        migrations.CreateModel(
            name='ArticleImages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(null=True, upload_to='articles_photos', verbose_name='картинка')),
                ('article', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='article.article')),
            ],
            options={
                'verbose_name': 'Картинка',
                'verbose_name_plural': 'Картинки',
            },
        ),
    ]
