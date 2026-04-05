**#Python Based Finance System Backend 
<br>
Overview
This project is a Python-powered finance tracking system backend built with Django and Django REST Framework (DRF). It allows users to manage financial records, view summaries, and perform role-based actions. The system is designed to be clean, maintainable, and easy to understand, demonstrating backend best practices, proper data handling, and structured code.
<br>
Features
Financial Records Management: Create, read, update, delete, and filter financial transactions.
Transaction Fields: Amount, Type (Income/Expense), Category, Date, Notes/Description.
Summary and Analytics: Total income, total expenses, balance, category-wise breakdown, monthly totals, and recent activity.
<br>
User Roles:
Viewer: Can view records and summaries.
Analyst: Can view, filter, and access detailed insights.
Admin: Full access to create, update, delete records, and manage users.
API Endpoints: RESTful API with clear and structured routes.
Validation & Error Handling: Input validation, meaningful error messages, and proper status codes.
Database: Uses SQLite with Django ORM for persistent data storage.

Technology Stack
Backend Framework: Django 4.x, Django REST Framework
Database: SQLite
Python Version: 3.10+
Project Structure
Plain text
finance_tracker/
├── finance_tracker/        # Project configuration
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── transactions/           # App for financial records
│   ├── models.py           # Transaction and user role models
│   ├── serializers.py      # DRF serializers
│   ├── views.py            # API views
│   ├── urls.py             # App routes
│   └── admin.py            # Admin panel configuration
├── manage.py
└── README.md
API Endpoints
Transactions
GET /api/transactions/ – List all transactions (with filtering options)
POST /api/transactions/ – Create a new transaction
GET /api/transactions/<id>/ – Retrieve a single transaction
PUT /api/transactions/<id>/ – Update a transaction
DELETE /api/transactions/<id>/ – Delete a transaction
Summaries
GET /api/summary/ – View total income, expenses, balance, category breakdown, and recent activity
Users & Roles
Role-based access is enforced: Viewer, Analyst, Admin
Users can be managed via Django Admin panel
Setup & Installation
Clone the repository
Bash
git clone https://github.com/Abhishek-pytech/finanse_tracker.git
cd finanse_tracker
Install Django and DRF globally (no virtual environment)
Bash
pip install django djangorestframework
Apply migrations
Bash
python manage.py migrate
Create superuser (for admin access)
Bash
python manage.py createsuperuser
Run the development server
Bash
python manage.py runserver
Access the API
API endpoints: http://127.0.0.1:8000/api/
Admin panel: http://127.0.0.1:8000/admin/
Assumptions
Role-based behavior is simplified for demonstration.
Authentication uses Django's default user model.
Optional features like pagination or CSV import/export can be added as enhancements.
Validation & Error Handling
Invalid requests return proper HTTP status codes (400, 404, 403).
API responses include descriptive error messages.
Backend ensures predictable behavior for invalid or incomplete inputs.
Optional Enhancements Implemented
API documentation via DRF browsable API
Admin panel for managing transactions and users
Filtering transactions by date, type, and category
Evaluation Notes
Code is structured with separation of concerns (models, views, serializers, urls).
Demonstrates Python proficiency and backend logic.
Summaries and filters implemented for meaningful financial insights.
Clean error handling and validation ensure reliability.
Author
******
