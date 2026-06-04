# SupportFlow API

![Django CI](https://github.com/adrianatortja/supportflow-api/actions/workflows/django.yml/badge.svg)

SupportFlow API is a Django REST Framework SaaS-style backend for managing customer support workflows.

It provides authenticated APIs for users, organizations, support tickets, ticket analytics, suggested replies, and internal ticket comments, with ownership-based access control and a clean backend structure designed for future SaaS features.

---

## Overview

SupportFlow API is a learning-focused and portfolio-ready backend project that simulates the foundation of a customer support SaaS platform.

The project focuses on:

- User authentication
- Organization management
- Support ticket management
- Ticket filtering, search, and ordering
- Ticket analytics
- Suggested customer support replies
- Ticket comments and internal notes
- Protected API endpoints
- Ownership-based data access
- Automated testing
- GitHub Actions CI
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
- GitHub Actions

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
- Delete organizations
- Ownership-based access control

### Tickets

- Create support tickets
- List tickets for the authenticated user
- Retrieve ticket details
- Update ticket status and details
- Delete tickets
- Connect tickets to organizations
- Filter tickets by status, priority, and organization
- Search tickets by title and description
- Order tickets by created date, updated date, priority, and status
- Ownership-based access control

### Ticket Analytics

- View total ticket count
- View ticket counts by status
- View ticket counts by priority
- Analytics are scoped to the authenticated user

### Suggested Replies

- Generate a rule-based suggested support reply for a ticket
- Suggested replies are based on the ticket title and description
- Access is restricted to the ticket owner

### Ticket Comments / Internal Notes

- Create comments for a ticket
- List comments for a ticket
- Support internal notes with `is_internal`
- Comments are tied to both the ticket and authenticated user
- Access is restricted to the ticket owner

### API Documentation

- Swagger API documentation
- OpenAPI schema generation

### Testing and CI

- Automated Django tests
- GitHub Actions workflow for running tests on push and pull request

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
| GET | `/api/tickets/analytics/` | Get ticket analytics |
| GET | `/api/tickets/<id>/suggested-reply/` | Get a suggested support reply |
| GET | `/api/tickets/<id>/comments/` | List comments for a ticket |
| POST | `/api/tickets/<id>/comments/` | Create a comment for a ticket |

### Ticket Filtering, Search, and Ordering

The ticket list endpoint supports filtering, search, and ordering.

```text
GET /api/tickets/?status=open
GET /api/tickets/?priority=high
GET /api/tickets/?organization=1
GET /api/tickets/?search=login
GET /api/tickets/?ordering=-created_at
```

### Documentation

| Method | Endpoint | Description |
|---|---|---|
| GET | `/api/docs/` | Swagger API documentation |
| GET | `/api/schema/` | OpenAPI schema |

---

## Example Analytics Response

```json
{
  "total_tickets": 1,
  "status_counts": {
    "open": 1
  },
  "priority_counts": {
    "high": 1
  }
}
```

---

## Example Suggested Reply Response

```json
{
  "ticket_id": 2,
  "suggested_reply": "Hi, thank you for reaching out. I’m sorry you’re having trouble accessing your account. Please try resetting your password again, and if the issue continues, we’ll investigate further."
}
```

---

## Example Ticket Comment Object

```json
{
  "id": 1,
  "ticket": 2,
  "owner": 1,
  "body": "Customer already tried resetting the password. Need to check account status.",
  "is_internal": true,
  "created_at": "2026-05-30T15:59:14.034483Z"
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

## Running Tests

Run the test suite locally with:

```bash
python manage.py test
```

Current test coverage includes:

- Suggested reply endpoint access
- Ticket comments list/create behavior
- Ownership protection
- Unauthenticated access protection

---

## Continuous Integration

This project uses GitHub Actions for CI.

The workflow runs automatically on:

- Pushes to `main`
- Pull requests targeting `main`

The CI workflow checks migrations and runs the Django test suite.

Workflow file:

```text
.github/workflows/django.yml
```

---

## Access Control

SupportFlow API uses ownership-based access control.

This means:

- Users can only see their own organizations.
- Users can only manage their own tickets.
- Users can only access suggested replies for their own tickets.
- Users can only create and list comments for their own tickets.
- Protected endpoints require authentication.
- Unauthorized users cannot access private resources.

---

## Current Status

The project currently includes:

- Django project setup
- Django REST Framework configuration
- JWT authentication
- Custom user model
- Organization management
- Ticket management
- Ticket filtering, search, and ordering
- Ticket analytics
- Suggested replies
- Ticket comments and internal notes
- Protected endpoints
- Ownership-based access control
- Automated tests
- GitHub Actions CI
- API documentation setup

---

## Planned Improvements

Future improvements may include:

- PostgreSQL configuration
- Docker setup
- Frontend dashboard
- Team-based organizations
- Ticket assignment
- Role-based permissions for admin and support agents
- SaaS billing and subscription logic
- AI-assisted support replies using an external AI service

---

## Portfolio Value

SupportFlow API demonstrates the backend foundation of a customer support SaaS platform.

It shows how to build authenticated, protected, tested, and organized APIs for real-world business workflows.

---

## Author

Built by Adriana Tortja.

GitHub: [@adrianatortja](https://github.com/adrianatortja)

---

## Repository

[SupportFlow API](https://github.com/adrianatortja/supportflow-api)