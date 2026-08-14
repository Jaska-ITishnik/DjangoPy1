from django.http.response import HttpResponse
from django.urls import reverse_lazy
from django.views.generic.base import TemplateView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView
from django.views.generic.list import ListView

from apps.forms import StudentModelForm
from apps.models import Student


class StudentListView(ListView):
    template_name = "students/student_list.html"
    queryset = Student.objects.all()
    context_object_name = "students"


class StudentDetailView(DetailView):
    template_name = "students/student_detail.html"
    queryset = Student.objects.all()
    context_object_name = "student"


class StudentDeleteTemplateView(TemplateView):
    template_name = "students/student_confirm_delete.html"


class StudentCreateTemplateView(TemplateView):
    template_name = "students/student_form.html"


class StudentUpdateView(UpdateView):
    queryset = Student.objects.all()
    form_class = StudentModelForm
    template_name = "students/student_form.html"
    context_object_name = "student"
    success_url = reverse_lazy("students_list")

    def form_invalid(self, form) -> HttpResponse:
        return super().form_invalid(form)
