from django.urls import path
from task2 import views


urlpatterns = [
    path("list/", views.VacancyFilterView.as_view()),
]
