from django.urls import path
from . import views

urlpatterns = [
    # Admin Routes
    path('admin/signup/', views.admin_signup, name='admin_signup'),
    path('admin/login/', views.admin_login, name='admin_login'),
    path('admin/logout/', views.admin_logout, name='admin_logout'),
    path('admin/books/', views.book_list, name='book_list'),
    path('admin/books/add/', views.add_book, name='add_book'),
    path('admin/books/<int:pk>/update/', views.update_book, name='update_book'),
    path('admin/books/<int:pk>/delete/', views.delete_book, name='delete_book'),

    # Student View
    path('student/books/', views.student_view_books, name='student_books'),
]
