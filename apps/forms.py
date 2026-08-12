from django.forms.models import ModelForm

from apps.models import Student


class StudentModelForm(ModelForm):
    class Meta:
        model = Student
        fields = "fullname", "email", "grade", "status"
