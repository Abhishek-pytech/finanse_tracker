# Finance Tracker Backend

## 📌 Project Overview
The Python Finance System Backend is a Django and Django REST Framework (DRF) powered application for managing personal financial transactions. It allows users to create, read, update, and delete financial records, view summaries of incomes, expenses, balances, and category-wise breakdowns, and implement role-based access control for different types of users. This project demonstrates core backend concepts such as Django ORM and models, RESTful API development, serializers and views, role-based access control, validation and error handling. It is designed for practical learning and real-world backend application logic.

## 🚀 Features
✔️ Manage Transactions: Create, Read, Update, Delete  
✔️ Transaction Fields: Amount, Type (Income/Expense), Category, Date, Notes  
✔️ Summaries & Analytics: Total income, expenses, balance, category breakdown, monthly totals  
✔️ Role-based Access: Viewer (view records and summaries), Analyst (filter and access detailed insights), Admin (full access to manage records and users)  
✔️ RESTful API Endpoints  
✔️ Proper Validation & Error Handling 

## 🛠️ Technologies Used
- Python 3.10+  
- Django 4.x  
- Django REST Framework (DRF)  
- SQLite (default Django database)  
- Command Line / API Interface

## 📂 Project Structure
finance_tracker/ <br>

├── finance_tracker/ # Project configuration <br>
│ ├── settings.py  <br>
│ ├── urls.py  <br>
│ └── wsgi.py  <br>
├── transactions/ # App for financial records  <br>
│ ├── models.py # Transaction and user role models  <br>
│ ├── serializers.py # DRF serializers  <br>
│ ├── views.py # API views  <br>
│ ├── urls.py # App routes  <br>
│ └── admin.py # Admin panel configuration  <br>
├── manage.py  <br>
└── README.md  <br>

## ⚙️ How to Run the Project
1. Clone Repository:  <br>
git clone https://github.com/Abhishek-pytech/finanse_tracker.git  <br>
cd finanse_tracker

## Install Dependencies:
pip install django djangorestframework

## Apply Migrations:
python manage.py migrate

## Create Superuser (Admin Access):
python manage.py createsuperuser

## Run Development Server:
python manage.py runserver

Access the System: API: http://127.0.0.1:8000/api/ ,Admin Panel: http://127.0.0.1:8000/admin/

## API Endpoints  <br>
GET /api/transactions/ – List all transactions  <br>
POST /api/transactions/ – Create transaction  <br>
GET /api/transactions/<id>/ – Retrieve transaction  <br>
PUT /api/transactions/<id>/ – Update transaction  <br>
DELETE /api/transactions/<id>/ – Delete transaction  <br>
GET /api/summary/ – View totals, balances, and category breakdown  <br>


## Assumptions
- Type must be either 'income' or 'expense'
- Amount must be positive

📚 Learning Outcomes <br>
Structuring Django REST APIs  <br>
Managing user roles and permissions  <br>
Creating CRUD operations with validation  <br>
Implementing summaries and analytics  <br>
Handling errors and proper HTTP responses  <br>

🎯 Future Improvements <br>
Add authentication using JWT or OAuth  <br>
Add pagination and filtering for large datasets  <br>
Export/import transactions (CSV/Excel)  <br>
Connect to PostgreSQL or MySQL for production  <br>
Add automated tests for API endpoints  <br>

👨‍💻 Author <br>
Abhishek Patel  <br>
Python Developer | Backend Enthusiast | Data Analytics Learner  <br>
Email: itsabhishek.patel29@gmail.com

