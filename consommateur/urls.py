from django.urls import path

from consommateur.views import publish

urlpatterns = [
    path('', publish, name='publish_consommateur'),
]
