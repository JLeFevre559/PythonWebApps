from django import forms
from .models import Article, Superhero

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'content', 'date', 'image', 'hero']  # Only list needed fields

    # Customize the hero field
    hero = forms.ModelChoiceField(
        queryset=Superhero.objects.all(),
        empty_label="Select a Superhero",
        label="Hero",
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    # Customize the date field with a DateInput widget
    date = forms.DateField(
        widget=forms.DateInput(
            attrs={
                'type': 'date',  # HTML5 date input type
                'class': 'form-control'  # Optionally add Bootstrap styling
            }
        ),
        label="Date"
    )
