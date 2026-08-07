from django.urls import path

from apps.views import StudentTemplateView, \
    StudentDetailTemplateView, StudentDeleteTemplateView, StudentCreateTemplateView

# from apps.views import profiles

urlpatterns = [
    # path('', students, name="students_list"),
    # path('delete', student_delete, name="delete"),
    # path('detail', student_detail, name="detail"),
    # path('create_or_update', student_create_or_update, name="create_or_update"),

    path('', StudentTemplateView.as_view(), name="students_list"),
    path('delete', StudentDeleteTemplateView.as_view(), name="delete"),
    path('detail', StudentDetailTemplateView.as_view(), name="detail"),
    path('create_or_update', StudentCreateTemplateView.as_view(), name="create_or_update"),
]
