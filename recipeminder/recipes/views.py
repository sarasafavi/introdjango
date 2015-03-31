from django.shortcuts import render, HttpResponse, redirect
from recipes.models import Recipe
from django.http import Http404
from recipes.forms import RecipeForm
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from recipes.serializers import RecipeSerializer

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


def addrecipe(request):
    """Create a form that can be used to add a new recipe.
    Save data submitted through the form to the database as a new recipe.
    """

    if request.method == 'POST':
        form = RecipeForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            r = Recipe()
            r.name = data['name']
            r.servings = data['servings']
            r.description = data['description']
            r.ingredients = data['ingredients']
            r.instructions = data['instructions']
            r.save()
            return redirect(recipe_list)
    else:
        form = RecipeForm()
    return render(request, 'addrecipe.html', { 'form': form})


@api_view(['GET', 'POST'])
def api_recipe_list(request):
    """
    API view that allows a list of recipes to be viewed or a new recipe to be
    created
    """
    if request.method == 'GET':
        recipes = Recipe.objects.all()
        serializer = RecipeSerializer(recipes, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = RecipeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(('GET',))
def api_recipe_detail(request, id):
    """
    API view that returns a recipe by ID
    """

    try:
        recipe = Recipe.objects.get(id=id)
    except Recipe.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = RecipeSerializer(recipe)
        return Response(serializer.data)
