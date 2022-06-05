from django.urls import path
from . import views

urlpatterns = [
    path('api', views.ApiOverview, name='api_overview'),
    path('create/', views.add_items, name='add-items'),
]