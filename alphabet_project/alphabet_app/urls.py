from django.urls import path
from . import views

urlpatterns = [
    path('alphabet/<str:letter>/', views.get_letter_detail, name='get_letter_detail'),
]
