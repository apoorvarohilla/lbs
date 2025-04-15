# 📚 Library Management System

A Django-based web application to manage library books, admin authentication, and student access.

## 🚀 Features
- Admin login/logout
- Add, edit, delete book records
- View all books
- Student view to browse books
- MySQL database integration

## 🛠 Tech Stack
- Django
- MySQL
- HTML/CSS (Bootstrap)

## ⚙️ Setup Instructions

```bash
# Clone the repo
git clone https://github.com/your-username/library-management-system.git
cd library-management-system

# Install dependencies
pip install -r requirements.txt

# Configure your database in settings.py

# Run migrations
python manage.py makemigrations
python manage.py migrate

# Start the server
python manage.py runserver
