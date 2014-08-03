from django.shortcuts import render, HttpResponse, redirect
from recipes.models import Recipe
from django.http import Http404
from recipes.forms import RecipeForm

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
