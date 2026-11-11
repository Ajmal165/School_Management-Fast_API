# School Management FastAPI

A FastAPI-based backend for managing school users, competitions, and student submissions. This project is designed to support role-based access for students and teachers, making it suitable for a small academic management system or competition portal.

## Overview

This repository provides a REST API for a school management system with the following features:

- User registration and login
- JWT authentication and token generation
- Role-based access control for students, teachers, and admin users
- Competition creation and management
- Student entry submissions for competitions
- SQLAlchemy database models and schemas

## Features

- FastAPI REST API
- SQLAlchemy ORM
- Password hashing using Passlib and bcrypt
- JWT-based authorization
- Pydantic request validation
- Modular project structure
- Competition and entry tracking

## Tech Stack

- Python
- FastAPI
- SQLAlchemy
- PostgreSQL / SQLite compatible setup
- JWT Authentication
- Passlib + bcrypt
- Pydantic

## Project Structure

```bash
School-management-FastApi/
├── .gitignore
├── README.md
├── alembic
├── database.py
├── main.py
├── requirements.txt
├── seessiolocal.py
├── src/
│   ├── competition/
│   │   ├── api.py
│   │   ├── model.py
│   │   ├── permission.py
│   │   └── schemas.py
│   ├── entry/
│   │   ├── api.py
│   │   ├── model.py
│   │   └── schemas.py
│   └── user/
│       ├── api.py
│       ├── deps.py
│       ├── model.py
│       ├── schemas.py
│       ├── token.py
│       └── __init__.py
└── .idea/
```

## Installation

1. Clone the repository:

```bash
git clone https://github.com/Ajmal165/School_Management-Fast_API.git
cd School_Management-Fast_API
```

2. Create a virtual environment:

```bash
python -m venv venv
source venv/bin/activate   # macOS/Linux
# venv\Scripts\activate   # Windows
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

## Database Configuration

The project uses SQLAlchemy with a PostgreSQL-compatible database URL configured in `database.py`.

Example:

```python
DATABASE_URL = "postgresql://username:password@localhost:5432/school_db"
```

Update this value according to your local or production database settings.

## Run the Application

```bash
uvicorn main:app --reload
```

Then open:

- Swagger UI: `http://127.0.0.1:8000/docs`
- ReDoc: `http://127.0.0.1:8000/redoc`

## API Modules

### User APIs

- `POST /register` - Register a new user
- `POST /login` - Login a user and get tokens
- `GET /show/{id}` - Fetch user details by ID

### Competition APIs

- `POST /competition/` - Add a competition
- `GET /competition/` - Get all competitions
- `GET /competition/{id}` - Get one competition
- `PUT /competition/{id}` - Update competition details
- `DELETE /competition/{id}` - Delete a competition

### Entry APIs

- `POST /entry/` - Submit a competition entry
- `GET /entry/` - Get all entries
- `GET /entry/{id}` - Get specific entry
- `PUT /entry/{id}` - Update entry
- `DELETE /entry/{id}` - Delete entry

## Role-Based Access

The project includes permission checks for different user roles:

- `student`
- `teacher`
- `admin`

These checks restrict actions so only authorized users can access specific routes.

## Example Workflow

1. Register a new user
2. Login to get JWT tokens
3. Create a competition as a teacher/admin
4. Students submit entries
5. View or manage data through REST endpoints

## Future Improvements

- Admin dashboard management
- Attendance tracking
- Course and classroom modules
- Better validation and error handling
- Frontend integration
- Pagination and search filters

## License

This project is intended for learning and educational use. Review security and deployment settings before using it in production.

## Contributing

Contributions are welcome. To contribute:

1. Fork the repository
2. Create your feature branch
3. Commit your changes
4. Open a pull request

## Repository

- GitHub: https://github.com/Ajmal165/School_Management-Fast_API
