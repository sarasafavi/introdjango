from django.conf.urls import url
from recipes import views

urlpatterns = [
    url(r'^$', views.recipe_list, name='recipelist')
]
