from django.conf.urls import patterns, include, url
from django.contrib import admin
import recipes

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'recipeminder.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^recipes/', include('recipes.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
