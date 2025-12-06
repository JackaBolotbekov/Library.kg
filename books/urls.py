from django.urls import path
from . import views

urlpatterns = [
    path('books/all/', views.book_list_view, name='book_list'),
    path('books/detail/<int:id>/', views.book_detail_view, name='book_detail'),
]