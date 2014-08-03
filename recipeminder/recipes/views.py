from django.shortcuts import render, HttpResponse
from recipes.models import Recipe
from django.http import Http404

def recipe_list(request):
    """Pull the current list of all recipes and return them.
    """

    recipelist = Recipe.objects.all()
    context = {'recipelist': recipelist}
    return render(request, 'recipelist.html', context)


def recipe(request, recipe_id):
    """Render a specific recipe, selected by ID, in a standalone page
    """

    try:
        recipe = Recipe.objects.get(id = recipe_id)
    except Recipe.DoesNotExist:
            raise Http404
    context = {'recipe' : recipe}
    return render(request, 'recipe.html', context)
