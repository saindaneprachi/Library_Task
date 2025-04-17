from django.shortcuts import render, redirect
from rest_framework import generics, permissions
from .models import Book
from .serializers import BookSerializer, AdminSignupSerializer
from django.contrib.auth.models import User

"""API View for Admin Signup using DRF
Allows creation of admin users (is_staff=True)"""

class AdminSignupView(generics.CreateAPIView):
    queryset = User.objects.filter(is_staff=True) # Only filters admin users
    serializer_class = AdminSignupSerializer      # Uses custom serializer to create admin



""" API View for listing and creating books
Accessible only by authenticated users (dmins)"""

class BookListCreateView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]


"""API View to retrieve, update, or delete a specific book by ID
Only accessible by authenticated users (i.e., admins)"""

class BookDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()       # Query all books
    serializer_class = BookSerializer    # Serializer to handle Book model
    permission_classes = [permissions.IsAuthenticated]  # JWT authentication required


"""UI view to show book list to students using HTML template
No authentication required – publicly accessible"""

from django.shortcuts import render

def student_book_list(request):
    books = Book.objects.all()
    return render(request, 'Management/book_list.html', {'books': books})   # Render to template