# Generated by Django 5.1.1 on 2024-12-06 03:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hero', '0011_remove_article_image_remove_superhero_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Note',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('notes', models.TextField()),
            ],
        ),
    ]
