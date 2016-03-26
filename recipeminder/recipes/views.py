from django.shortcuts import HttpResponse
from recipes.models import Recipe


def recipe_list(request):
    recipelist = Recipe.objects.all()
    names = '<li>'.join([r.name for r in recipelist])
    output = '<ul><li>{}</ul>'.format(names)
    return HttpResponse(output)
