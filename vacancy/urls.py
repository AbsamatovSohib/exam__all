from django.urls import path
from vacancy import views


urlpatterns = [
    path("list/", views.VacancyListApiView.as_view()),
    path("statistic/", views.VacancyStatisticView.as_view()),

    path("category/", views.CategoryListView.as_view()),
]
