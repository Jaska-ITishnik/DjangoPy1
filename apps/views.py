from django.views.generic.base import TemplateView
from django.views.generic.list import ListView

from apps.models import Student


# def students(request):
#     return TemplateResponse(request, template="students/student_list.html")
#
#
# def student_delete(request):
#     return TemplateResponse(request, template="students/student_confirm_delete.html")
#
#
# def student_detail(request):
#     return TemplateResponse(request, template="students/student_detail.html")
#
#
# def student_create_or_update(request):
#     return TemplateResponse(request, template="students/student_form.html")


# Class based views

class StudentTemplateView(ListView):
    template_name = "students/student_list.html"
    queryset = Student.objects.all()
    context_object_name = "students"


class StudentDetailTemplateView(TemplateView):
    template_name = "students/student_detail.html"


class StudentDeleteTemplateView(TemplateView):
    template_name = "students/student_confirm_delete.html"


class StudentCreateTemplateView(TemplateView):
    template_name = "students/student_form.html"
