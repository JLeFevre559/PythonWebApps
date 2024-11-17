from .models import Superhero, Article, Investigator
import json, csv
from django.http import HttpResponse

def import_heroes(file, file_type):
    if file_type == 'json':
        data = json.loads(file.read())
        for item in data:
            superhero = Superhero(
                name=item['name'],
                identity=item['identity'],
                description=item['description'],
                image=item['image'],
                strengths=item['strengths'],
                weaknesses=item['weaknesses'],
            )
            superhero.save()
    elif file_type == 'csv':
        reader = csv.reader(file)
        next(reader)  # Skip the header row
        for row in reader:
            superhero = Superhero(
                name=row[0],
                identity=row[1],
                description=row[2],
                image=row[3],
                strengths=row[4],
                weaknesses=row[5],
            )
            if Superhero.objects.get(name=row[0]):
                return HttpResponse(status=201)
            superhero.save()
    else:
        return HttpResponse(status=400)
    return HttpResponse(status=201)

def import_articles(file, file_type):
    if file_type == 'json':
        data = json.loads(file.read())
        for item in data:
            article = Article(
                title=item['title'],
                content=item['content'],
                author=item['author'],
                date=item['date'],
                image=item['image'],
                hero=Superhero.objects.get(name=item['hero']),
            )
            article.save()
    elif file_type == 'csv':
        reader = csv.reader(file)
        next(reader)  # Skip the header row
        for row in reader:
            article = Article(
                title=row[0],
                content=row[1],
                author=row[2],
                date=row[3],
                image=row[4],
                hero=Superhero.objects.get(name=row[5]),
            )
            article.save()
    else:
        return HttpResponse(status=400)
    return HttpResponse(status=201)
    