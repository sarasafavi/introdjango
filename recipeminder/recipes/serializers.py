from recipes.models import Recipe
from rest_framework import serializers


class RecipeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Recipe
        fields = ('name', 'created', 'description', 'servings', 'ingredients',
                  'instructions')
