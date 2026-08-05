from django.template.response import TemplateResponse


#
# def profiles(request):
#     people = [
#         {
#             "fullname": "Jasurbek Bekmirzayev",
#             "profession": "Developer"
#         },
#         {
#             "fullname": "Alijon Valiyev",
#             "profession": "Teacher"
#         },
#         {
#             "fullname": "Anvar Jabborov",
#             "profession": "Software Engineer"
#         },
#         {
#             "fullname": "Abdujappor Teshayev",
#             "profession": "Builder"
#         }
#     ]
#     context = {
#         "people": people
#     }
#     return TemplateResponse(request, template="user_profiles.html", context=context)


def students(request):
    return TemplateResponse(request, template="students/student_list.html")


def student_delete(request):
    return TemplateResponse(request, template="students/student_confirm_delete.html")


def student_detail(request):
    return TemplateResponse(request, template="students/student_detail.html")


def student_create_or_update(request):
    return TemplateResponse(request, template="students/student_form.html")
