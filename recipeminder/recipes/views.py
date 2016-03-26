from django.shortcuts import HttpResponse


def recipe_list(request):
    return HttpResponse("This will be a list of all recipes.")
