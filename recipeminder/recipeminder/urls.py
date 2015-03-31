from django.conf.urls import patterns, include, url
from django.contrib import admin
from recipes import views
from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'recipeminder.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^recipes/', include('recipes.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
# API urls
urlpatterns += format_suffix_patterns(
    [
        url(r'^api/recipes/$', views.api_recipe_list, name='api-recipe-list'),
    ]
)
