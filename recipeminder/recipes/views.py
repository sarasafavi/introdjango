from django.shortcuts import render
from django.http import Http404
from recipes.models import Recipe


def recipe_list(request):
    recipelist = Recipe.objects.all()
    context = {'recipelist': recipelist}
    return render(request, 'recipelist.html', context)


def recipe(request, recipe_id):
    try:
        recipe = Recipe.objects.get(id=recipe_id)
    except Recipe.DoesNotExist:
        raise Http404
    context = {'recipe': recipe}
    return render(request, 'recipe.html', context)
