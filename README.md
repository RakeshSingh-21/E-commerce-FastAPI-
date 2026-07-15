# E-commerce-FastAPI-

# FastAPI E-commerce Project

## Overview

This is a **FastAPI backend project** for an E-commerce platform with:

- JWT-based authentication
- Role-based access control (Admin & User)
- Product management (CRUD)
- MySQL database integration via SQLAlchemy

---

## Features

1. **Authentication**
   - User registration (`/auth/register`)
   - User login (`/auth/login`)
   - JWT token for secure endpoints

2. **Role-Based Access**
   - Admin can create, update, delete products
   - Users can view products only

3. **Product Management**
   - List all products
   - Admin CRUD for products

4. **Database**
   - SQLAlchemy ORM
   - Models: `User` and `Product`

---

## Requirements

- Python 3.10+
- FastAPI
- Uvicorn
- SQLAlchemy
- Pydantic
- bcrypt
- JWT (PyJWT)
- MySQL or SQLite

---

## Installation


# Create virtual environment
python -m venv myenv
myenv\Scripts\activate   # Windows
source myenv/bin/activate  # Linux/macOS

# Install dependencies
pip install -r requirements.txt
