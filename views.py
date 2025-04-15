from django.shortcuts import render, redirect, get_object_or_404
from .forms import AdminSignupForm, AdminLoginForm, BookForm
from .models import Admin, Book
from django.contrib import messages

# Admin Signup
def admin_signup(request):
    if request.method == 'POST':
        form = AdminSignupForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Admin registered successfully.')
            return redirect('admin_login')
    else:
        form = AdminSignupForm()
    return render(request, 'admin_signup.html', {'form': form})


# Admin Login
def admin_login(request):
    if request.method == 'POST':
        form = AdminLoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            try:
                admin = Admin.objects.get(email=email, password=password)
                request.session['admin_id'] = admin.id  # Login using session
                return redirect('book_list')
            except Admin.DoesNotExist:
                messages.error(request, 'Invalid login credentials.')
    else:
        form = AdminLoginForm()
    return render(request, 'admin_login.html', {'form': form})


# Admin Logout
def admin_logout(request):
    request.session.flush()
    return redirect('admin_login')


# Book Create
def add_book(request):
    if 'admin_id' not in request.session:
        return redirect('admin_login')
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Book added successfully.')
            return redirect('book_list')
    else:
        form = BookForm()
    return render(request, 'add_book.html', {'form': form})


# Book List (Admin View)
def book_list(request):
    if 'admin_id' not in request.session:
        return redirect('admin_login')
    books = Book.objects.all()
    return render(request, 'book_list.html', {'books': books})


# Update Book
def update_book(request, pk):
    if 'admin_id' not in request.session:
        return redirect('admin_login')
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            messages.success(request, 'Book updated successfully.')
            return redirect('book_list')
    else:
        form = BookForm(instance=book)
    return render(request, 'update_book.html', {'form': form})


# Delete Book
def delete_book(request, pk):
    if 'admin_id' not in request.session:
        return redirect('admin_login')
    book = get_object_or_404(Book, pk=pk)
    book.delete()
    messages.success(request, 'Book deleted successfully.')
    return redirect('book_list')


# Student View (All Books)
def student_view_books(request):
    books = Book.objects.all()
    return render(request, 'student_books.html', {'books': books})
