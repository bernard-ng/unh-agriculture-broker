from django.urls import path

from agriculteur.views import publish, receive

urlpatterns = [
    path('', publish, name='publish_agriculteur'),
    path('recevoir', receive, name='receive_agriculteur')
]
