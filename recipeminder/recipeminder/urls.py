from django.conf.urls import include, url

urlpatterns = [
    url(r'^recipes/', include('recipes.urls')),
        ]
