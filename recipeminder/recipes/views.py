from django.shortcuts import render, HttpResponse
from recipes.models import Recipe

def recipe_list(request):
    """Pull the current list of all recipes and return them.
    """
    recipelist = Recipe.objects.all()
    names = '<li>'.join([r.name for r in recipelist])
    output = '<ul><li>{0}</ul>'.format(names)
    return HttpResponse(output)
