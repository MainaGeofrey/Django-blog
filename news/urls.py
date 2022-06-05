
from django.urls import path
from news import views
  
urlpatterns = [
   path('mynews', views.index, name ='mynews'),

]