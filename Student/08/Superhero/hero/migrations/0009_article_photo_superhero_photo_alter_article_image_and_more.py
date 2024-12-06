# Generated by Django 5.1.1 on 2024-11-24 11:01

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hero', '0006_photo'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='photo',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='hero.photo'),
        ),
        migrations.AddField(
            model_name='superhero',
            name='photo',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='hero.photo'),
        ),
        migrations.AlterField(
            model_name='article',
            name='image',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='superhero',
            name='image',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]