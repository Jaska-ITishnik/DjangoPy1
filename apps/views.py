from typing import Any

from django.urls import reverse_lazy
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
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


class StudentDeleteView(DeleteView):
    template_name = "students/student_confirm_delete.html"
    queryset = Student.objects.all()
    context_object_name = "student"
    success_url = reverse_lazy("students_list")


class StudentCreateView(CreateView):
    template_name = "students/student_form.html"
    queryset = Student.objects.all()
    success_url = reverse_lazy("students_list")
    form_class = StudentModelForm

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        ctx = super().get_context_data(**kwargs)
        ctx["grades"] = {choice[0]: choice[-1] for choice in Student.Grade.choices}
        return ctx


class StudentUpdateView(UpdateView):
    queryset = Student.objects.all()
    form_class = StudentModelForm
    template_name = "students/student_form.html"
    context_object_name = "student"
    success_url = reverse_lazy("students_list")
