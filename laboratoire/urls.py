from django.urls import path

from laboratoire.views import publish

urlpatterns = [
    path('', publish, name='publish_laboratoire'),
]
