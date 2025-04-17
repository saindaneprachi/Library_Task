 
from django.urls import path
from .views import AdminSignupView,BookListCreateView, BookDetailView, student_book_list

urlpatterns = [
    path('signup/', AdminSignupView.as_view(), name='admin_signup'),
    path('books/', BookListCreateView.as_view(), name='book_list_create'),
    path('books/<int:pk>/', BookDetailView.as_view(), name='book_detail'),
    path('student/books/', student_book_list, name='student_book_list'),
]

