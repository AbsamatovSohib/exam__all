from django.urls import path
from task3 import views

urlpatterns = [
    path('plain/', views.ProductListPlainView.as_view()),
    path('encrypted/', views.ProductListEncryptedView.as_view()),
    path('decrypt/', views.DecryptProductList.as_view()),
]
