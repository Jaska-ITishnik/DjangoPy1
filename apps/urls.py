from django.urls import path

from apps.views import profiles

urlpatterns = [
    path('profiles', profiles, name="profiles"),
]
