from django.urls import path

from apps.views import StudentListView, \
    StudentDetailView, StudentDeleteTemplateView, StudentCreateTemplateView, StudentUpdateView

# from apps.views import profiles

urlpatterns = [
    # path('', students, name="students_list"),
    # path('delete', student_delete, name="delete"),
    # path('detail', student_detail, name="detail"),
    # path('create_or_update', student_create_or_update, name="create_or_update"),

    path('', StudentListView.as_view(), name="students_list"),
    path('delete', StudentDeleteTemplateView.as_view(), name="delete"),
    path('detail/<int:pk>', StudentDetailView.as_view(), name="detail"),
    path('create_or_update', StudentCreateTemplateView.as_view(), name="create_or_update"),
    path('update/<int:pk>', StudentUpdateView.as_view(), name="student_update"),
]
