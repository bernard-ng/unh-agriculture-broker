from django.urls import path

from market.views import publish

urlpatterns = [
    path('', publish, name='publish_market'),
]
