from django.urls import path
from . import views

urlpatterns = [
    path('',views.index), #our domain.com/library
    
]
