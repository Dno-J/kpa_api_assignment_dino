# Backend Assignment for Sarva Suvidhan Pvt. Ltd. — KPA API (by Dino)

This project involves building a RESTful API to manage wheel specification form data using **FastAPI** and **PostgreSQL**. The goal is to demonstrate proficiency in API development, data validation, and modular backend architecture.

---

## 🚀 Features

- ✅ Two API endpoints:
  - `POST /api/forms/wheel-specifications` — Submit wheel specification form
  - `GET /api/forms/wheel-specifications` — Retrieve filtered forms
- ✅ Input validation for required fields and data types
- ✅ Duplicate form number check
- ✅ Structured JSON responses with `success`, `message`, and `data`
- ✅ Swagger UI for API documentation (`/docs`)
- ✅ Postman collection with working API responses
- ✅ Modular codebase with SQLAlchemy models and CRUD operations
- ✅ Environment-based configuration using `.env`

---

## 🛠️ Tech Stack

- FastAPI
- PostgreSQL
- SQLAlchemy
- Pydantic
- Uvicorn
- dotenv

---

## 📦 Setup Instructions

1. Clone the repo:
   ```bash
   git clone https://github.com/Dno-J/kpa_api_assignment_dino.git
   cd kpa_api_assignment_dino
   ```

2. Create a virtual environment and install dependencies:
   ```bash
   python -m venv .venv
   .venv\Scripts\activate  # or source .venv/bin/activate on Linux/Mac
   pip install -r requirements.txt
   ```

3. Create a `.env` file in the root directory:
   ```env
   DATABASE_URL=postgresql://postgres:admin123@localhost:5432/kpa_db
   ```

4. Run the app:
   ```bash
   uvicorn app.main:app --reload
   ```

5. Access Swagger UI:
   ```
   http://127.0.0.1:8000/docs
   ```

---

## 📁 Postman Collection

Included in the repo as `dino_postman_collection.json`, containing:
- POST request with valid form data
- GET request with query parameters to retrieve saved forms

---

## ⚠️ Assumptions & Limitations

- Assumes PostgreSQL is running locally on port 5432
- `.env` file must be created manually with correct DB credentials
- No authentication or user roles implemented (not required for this assignment)
