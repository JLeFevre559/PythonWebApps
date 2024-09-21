from django.shortcuts import render
from pathlib import Path
from django.views.generic import TemplateView

class PhotoView(TemplateView):
    template_name = 'photo.html'

    def get_context_data(self, **kwargs):
        p = kwargs['name']
        p = f'/static/images/{p}'
        return dict(photo=p)
    
def photo_list():
    photos = Path('static/images').iterdir()
    photos = [f for i, f in enumerate(photos)]
    return photos

class PhotosView(TemplateView):
    template_name = 'photos.html'

    def get_context_data(self, **kwargs):
        return dict(photos=photo_list())
        