from django.urls import path
from . import views

urlpatterns = [
    path('', views.see_reviews, name='see_reviews'),
]
