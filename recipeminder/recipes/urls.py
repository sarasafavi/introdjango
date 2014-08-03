from django.conf.urls import patterns, url
from recipes import views

urlpatterns = patterns('',
        url(r'^$', views.recipe_list, name = 'recipelist')
                        )
