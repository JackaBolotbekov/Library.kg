from django.urls import path
from . import views

urlpatterns = [
    path('writers/', views.writers_view, name='writers'),
    path('quotes/', views.quotes_view, name='quotes'),
    path('time/', views.current_time_view, name='time'),
]