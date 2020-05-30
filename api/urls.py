from django.urls import path
from api import views

urlpatterns = [
    path("students/",views.StudentListView.as_view()),
    path("students/<int:pk>",views.StudentDetailsView.as_view()),
    path("deletestudent/<int:pk>",views.StudentDeleteView.as_view()),
]
