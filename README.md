# Finance Tracker Backend

## Overview
This is a Django REST API for managing financial transactions.

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
