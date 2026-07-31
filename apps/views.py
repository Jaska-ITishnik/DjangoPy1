from django.shortcuts import render
from django.template.response import TemplateResponse


# Create your views here.

def profiles(request):
    return TemplateResponse(request, template="user_profiles.html")