from django.urls import path

from transporteur.views import publish

urlpatterns = [
    path('', publish, name='publish_transporteur'),
]
