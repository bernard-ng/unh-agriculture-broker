"""
URL configuration for agricole project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

import agricole.views as agricole_views
import consommateur.views as consommateur_views
import agriculteur.views as agriculteur_views
import laboratoire.views as laboratoire_views
import market.views as market_views
import transporteur.views as transporteur_views


urlpatterns = [
    path('', agricole_views.connection, name='connection'),
    path('admin/', admin.site.urls),
    path('agriculteur/', agriculteur_views.publish, name='publish_agriculteur'),
    path('consommateur/', consommateur_views.publish, name='publish_consommateur'),
    path('laboratoire/', laboratoire_views.publish, name='publish_laboratoire'),
    path('market/', market_views.publish, name='publish_market'),
    path('transporteur/', transporteur_views.publish, name='publish_transporteur'),

    path('agriculteur/recevoir', agriculteur_views.receive, name='receive_agriculteur'),
    path('consommateur/recevoir', consommateur_views.receive, name='receive_consommateur'),
    path('laboratoire/recevoir', laboratoire_views.receive, name='receive_laboratoire'),
    path('market/recevoir', market_views.receive, name='receive_market'),
    path('transporteur/recevoir', transporteur_views.receive, name='receive_transporteur'),

]
