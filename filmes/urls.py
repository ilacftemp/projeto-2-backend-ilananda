from django.urls import path

from . import views

urlpatterns = [
    path('api/filmes/<str:titulo>/', views.api_filme),
    path('api/filmes/<str:titulo>/<str:palavra>/', views.delete_word),
]