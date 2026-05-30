# SupportFlow API

SupportFlow API is a Django REST Framework SaaS-style backend for managing customer support workflows.

It provides authenticated APIs for users, organizations, and support tickets, with ownership-based access control and a clean backend structure designed for future SaaS features.

---

## Overview

SupportFlow API is a learning-focused and portfolio-ready backend project that simulates the foundation of a customer support SaaS platform.

The project focuses on:

- User authentication
- Organization management
- Support ticket management
- Protected API endpoints
- Ownership-based data access
- Clean Django REST Framework architecture
- API documentation
- Future SaaS-ready structure

---

## Tech Stack

- Python
- Django
- Django REST Framework
- Simple JWT
- SQLite
- django-filter
- drf-spectacular
- Git & GitHub

---

## Main Features

### Authentication

- User registration
- User login
- JWT access and refresh tokens
- Protected current-user endpoint
- Role field for users

### Organizations

- Create organizations
- List organizations owned by the authenticated user
- Retrieve organization details
- Update organization details
- Ownership-based access control

### Tickets

- Create support tickets
- List tickets for the authenticated user
- Retrieve ticket details
- Update ticket status and details
- Delete tickets
- Connect tickets to organizations
- Ownership-based access control

### API Documentation

- Swagger API documentation
- OpenAPI schema generation

---

## Project Structure

```bash
supportflow-api/
├── config/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── core/
│
├── organizations/
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   └── urls.py
│
├── tickets/
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   └── urls.py
│
├── users/
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   └── urls.py
│
├── manage.py
├── requirements.txt
└── .gitignore
```

---

## API Endpoints

### Authentication

| Method | Endpoint | Description |
|---|---|---|
| POST | `/api/auth/register/` | Register a new user |
| POST | `/api/auth/login/` | Log in and receive JWT tokens |
| POST | `/api/auth/refresh/` | Refresh access token |
| GET | `/api/auth/me/` | Get authenticated user details |

### Organizations

| Method | Endpoint | Description |
|---|---|---|
| GET | `/api/organizations/` | List user organizations |
| POST | `/api/organizations/` | Create a new organization |
| GET | `/api/organizations/<id>/` | Retrieve organization details |
| PATCH | `/api/organizations/<id>/` | Update organization |
| DELETE | `/api/organizations/<id>/` | Delete organization |

### Tickets

| Method | Endpoint | Description |
|---|---|---|
| GET | `/api/tickets/` | List user tickets |
| POST | `/api/tickets/` | Create a new ticket |
| GET | `/api/tickets/<id>/` | Retrieve ticket details |
| PATCH | `/api/tickets/<id>/` | Update ticket |
| DELETE | `/api/tickets/<id>/` | Delete ticket |

### Documentation

| Method | Endpoint | Description |
|---|---|---|
| GET | `/api/docs/` | Swagger API documentation |
| GET | `/api/schema/` | OpenAPI schema |

---

## Example Ticket Object

```json
{
  "id": 1,
  "title": "Customer cannot access account",
  "description": "The customer says they cannot log in after resetting their password.",
  "status": "open",
  "priority": "medium",
  "organization": 1,
  "owner": 1,
  "created_at": "2026-05-30T10:00:00Z"
}
```

---

## Example Organization Object

```json
{
  "id": 1,
  "name": "Acme Support",
  "description": "Customer support team for Acme.",
  "owner": 1,
  "created_at": "2026-05-30T10:00:00Z"
}
```

---

## Local Setup

### 1. Clone the repository

```bash
git clone https://github.com/adrianatortja/supportflow-api.git
cd supportflow-api
```

### 2. Create and activate a virtual environment

On Windows:

```bash
python -m venv venv
venv\Scripts\activate
```

On macOS/Linux:

```bash
python -m venv venv
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run migrations

```bash
python manage.py migrate
```

### 5. Create a superuser

```bash
python manage.py createsuperuser
```

### 6. Start the development server

```bash
python manage.py runserver
```

The API will run at:

```text
http://127.0.0.1:8000/
```

Swagger documentation will be available at:

```text
http://127.0.0.1:8000/api/docs/
```

---

## Authentication Flow

1. Register a user:

```text
POST /api/auth/register/
```

2. Log in:

```text
POST /api/auth/login/
```

3. Copy the access token from the response.

4. Use the token in protected requests:

```text
Authorization: Bearer your_access_token_here
```

5. Refresh the access token when needed:

```text
POST /api/auth/refresh/
```

---

## Example Login Response

```json
{
  "refresh": "your_refresh_token",
  "access": "your_access_token"
}
```

---

## Access Control

SupportFlow API uses ownership-based access control.

This means:

- Users can only see their own organizations.
- Users can only manage tickets connected to their own data.
- Protected endpoints require authentication.
- Unauthorized users cannot access private resources.

This structure is important for SaaS-style applications where each user or organization must only access their own data.

---

## Current Status

The project currently includes:

- Django project setup
- Django REST Framework configuration
- JWT authentication
- Custom user model
- Organization management
- Ticket management
- Protected endpoints
- Ownership-based access control
- API documentation setup

---

## Planned Improvements

Future improvements may include:

- Ticket filtering, search, and ordering
- Ticket analytics endpoint
- Suggested reply endpoint
- Automated tests
- GitHub Actions CI
- PostgreSQL configuration
- Docker setup
- Frontend dashboard
- Role-based permissions for admin and support agents
- SaaS billing and subscription logic

---

## Learning Goals

This project was built to practice backend development concepts used in real SaaS applications, including:

- API design
- Authentication
- Authorization
- Data ownership
- Model relationships
- Serializer validation
- Clean project structure
- Postman testing
- API documentation
- Git and GitHub workflow

---

## Portfolio Value

SupportFlow API demonstrates the backend foundation of a customer support SaaS platform.

It shows how to build authenticated, protected, and organized APIs for real-world business workflows.

The project can be extended into a full SaaS application with:

- A React frontend
- Team-based organizations
- Ticket assignment
- Analytics dashboard
- AI-assisted support replies
- Subscription billing

---

## Author

Built by Adriana Tortja.

GitHub: [@adrianatortja](https://github.com/adrianatortja)

---

## Repository

[SupportFlow API](https://github.com/adrianatortja/supportflow-api)