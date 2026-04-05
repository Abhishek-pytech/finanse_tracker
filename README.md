# Finance Tracker Backend

## 📌 Project Overview
The Python Finance System Backend is a Django and Django REST Framework (DRF) powered application for managing personal financial transactions. It allows users to create, read, update, and delete financial records, view summaries of incomes, expenses, balances, and category-wise breakdowns, and implement role-based access control for different types of users. This project demonstrates core backend concepts such as Django ORM and models, RESTful API development, serializers and views, role-based access control, validation and error handling. It is designed for practical learning and real-world backend application logic.

## Features
- Create, Read, Update, Delete transactions
- Summary API (income, expense, balance)
- Filtering by type, category, date
- Input validation
- Basic role-based access

## Tech Stack
- Python
- Django
- Django REST Framework
- SQLite

## Setup Instructions
1. Clone repository
2. Install dependencies:
   pip install -r requirements.txt
3. Run server:
   python manage.py runserver

## API Endpoints
- /transactions/
- /summary/
- /transactions/?type=income
- /transactions/?category=food

## Assumptions
- Type must be either 'income' or 'expense'
- Amount must be positive

## Author
Abhishek Patel
