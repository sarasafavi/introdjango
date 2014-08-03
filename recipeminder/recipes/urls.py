from django.conf.urls import patterns, url
from recipes import views

urlpatterns = patterns('',
        url(r'^$', views.recipe_list, name = 'recipelist'),
        url(r'^(?P<recipe_id>\d+)/$', views.recipe, name='recipe'),
        url(r'^addrecipe/', views.addrecipe, name='addrecipe')
                        )
