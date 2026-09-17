from django.urls import path
from .views import student_list, student_create, student_update, student_delete

urlpatterns = [
    path("", student_list, name="student-list"),
    path("create/", student_create, name="student-create"),
    path("<int:id>/", student_update, name="student-update"),
    path("<int:id>/delete/", student_delete, name="student-delete"),
]