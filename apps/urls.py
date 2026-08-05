from django.urls import path

from apps.views import students, student_delete, student_detail, student_create_or_update

# from apps.views import profiles

urlpatterns = [
    path('', students, name="students_list"),
    path('delete', student_delete, name="delete"),
    path('detail', student_detail, name="detail"),
    path('create_or_update', student_create_or_update, name="create_or_update"),
]
