from django.template.response import TemplateResponse


# Create your views here.

def profiles(request):
    people = {
        "1": {
            "fullname": "Botirjon Aliyev",
            "profession": "Developer"
        },
        "2": {
            "fullname": "Botirjon Aliyev",
            "profession": "Developer"
        },
        "3": {
            "fullname": "Botirjon Aliyev",
            "profession": "Developer"
        }
    }
    context = {
        "people": people
    }
    return TemplateResponse(request, template="user_profiles.html", context=context)
