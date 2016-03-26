from django import forms
import datetime


class RecipeForm(forms.Form):
    name = forms.CharField(label='name')
    created = forms.DateField(initial=datetime.date.today)
    servings = forms.IntegerField(label='servings')
    description = forms.CharField(label='description', widget=forms.Textarea)
    ingredients = forms.CharField(label='ingredients', widget=forms.Textarea)
    instructions = forms.CharField(label='instructions', widget=forms.Textarea)
