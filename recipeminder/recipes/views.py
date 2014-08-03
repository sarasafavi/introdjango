from django.shortcuts import render, HttpResponse
from recipes.models import Recipe

def recipe_list(request):
    """Pull the current list of all recipes and return them.
    """
    recipelist = Recipe.objects.all()
    context = {'recipelist': recipelist}
    return render(request, 'recipelist.html', context)
