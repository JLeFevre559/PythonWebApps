from django import forms
from .models import Article, Superhero, Investigator
from django.contrib.auth.models import User

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'content', 'date', 'image', 'hero', 'investigator']  # Only list needed fields

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

    # Customize the investigator field
    investigator = forms.ModelChoiceField(
        queryset=Investigator.objects.all(),
        empty_label="Select an Investigator",
        label="Investigator",
        widget=forms.Select(attrs={'class': 'form-control'})
    )

class InvestigatorForm(forms.ModelForm):
    class Meta:
        model = Investigator
        fields = ['user','name']

    user = forms.ModelChoiceField(
        queryset=User.objects.all(),
        empty_label="Select a User",
        label="User",
        widget=forms.Select(attrs={'class': 'form-control'})
    )