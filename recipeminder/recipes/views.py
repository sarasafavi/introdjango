from django.shortcuts import render
from recipes.models import Recipe


def recipe_list(request):
    recipelist = Recipe.objects.all()
    context = {'recipelist': recipelist}
    return render(request, 'recipelist.html', context)
