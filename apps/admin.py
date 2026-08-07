from django.contrib import admin
from django.contrib.admin.options import ModelAdmin

from apps.models import Student


# Register your models here.

@admin.register(Student)
class StudentModelAdmin(ModelAdmin):
    list_display = "id", "fullname", "email", "grade", "status"
