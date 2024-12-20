# Generated by Django 5.1.1 on 2024-10-27 01:08

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hero', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('content', models.TextField()),
                ('author', models.CharField(max_length=200)),
                ('date', models.DateField()),
                ('image', models.CharField(max_length=200)),
                ('hero', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hero.superhero')),
            ],
        ),
    ]
