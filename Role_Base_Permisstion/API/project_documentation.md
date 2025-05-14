# Role-Based Access Control System Documentation

## Project Overview
This project implements a Role-Based Access Control (RBAC) system using Django and Django REST Framework. It provides a secure way to manage user permissions, roles, and access control for a music management system.

## Technology Stack
- Django 5.0.7
- Django REST Framework 3.15.2
- Django REST Framework Simple JWT 5.3.1
- Python JWT (PyJWT) 2.8.0

## Project Structure
```
.
├── API/                  # Main Django project directory
├── RBAC_API/            # Main application directory
│   ├── models.py        # Data models
│   ├── views.py         # API views
│   ├── urls.py          # URL routing
│   └── permissions.py   # Custom permissions
```

## Models

### User Model
- Custom user model extending AbstractBaseUser
- Fields:
  - email (unique identifier)
  - role (choices: admin, manager, and normal)
  - is_staff
  - is_active
  - is_superuser

### Singer Model
- Represents music artists
- Fields:
  - name
  - age
  - email
  - date_of_birth
  - address

### Song Model
- Represents music tracks
- Fields:
  - title
  - singer (ForeignKey to Singer)

### Role Model
- Defines user roles
- Fields:
  - name
  - description

### UserPermission Model
- Maps users to permissions
- Fields:
  - user (ForeignKey)
  - permission (ForeignKey)

## API Endpoints

### Authentication Endpoints
1. **Register** (`/api/register/`)
   - Method: POST
   - Creates new user accounts

2. **Login** (`/api/login/`)
   - Method: POST
   - Authenticates users and provides JWT tokens

### Resource Endpoints
1. **Songs** 
   - CRUD operations for songs
   - Different permissions based on user roles

2. **Singers**
   - CRUD operations for singers
   - Different permissions based on user roles

3. **Groups**
   - Create and manage user groups
   - Admin-only access

4. **User Permissions**
   - Manage user-specific permissions
   - Admin-only access

## Permission Classes

### IsAdminOrReadOnly
- Full access for admin users
- Read-only access for other users

### IsManagerOrReadOnly
- Full access for managers
- Read-only access for other users

### IsExtraReadOnly
- Provides read-only access with specific conditions

## Authentication
The system uses JWT (JSON Web Tokens) for authentication:
- Access tokens for API requests
- Refresh tokens for obtaining new access tokens

## Role-Based Access Levels

1. **Admin**
   - Full system access
   - Can manage users, roles, and permissions
   - Complete CRUD access to all resources

2. **Manager**
   - Can create and modify resources
   - Limited administrative capabilities
   - Cannot modify system settings

3. **Normal User**
   - Read-only access to most resources
   - Limited creation rights
   - No administrative access

## Setup Instructions

1. Clone the repository
2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Apply migrations:
   ```bash
   python manage.py migrate
   ```
5. Create a superuser:
   ```bash
   python manage.py createsuperuser
   ```
6. Run the development server:
   ```bash
   python manage.py runserver
   ```

## Security Considerations
- JWT tokens must be included in request headers
- Passwords are securely hashed
- Role-based permissions are strictly enforced
- Input validation on all endpoints

## API Usage Examples

### User Registration
```http
POST /api/register/
{
    "email": "user@example.com",
    "password": "secure_password",
    "role": "normal"
}
```

### User Login
```http
POST /api/login/
{
    "email": "user@example.com",
    "password": "secure_password"
}
```

### Creating a Singer (Manager/Admin only)
```http
POST /api/singers/
{
    "name": "Artist Name",
    "age": 30,
    "email": "artist@example.com",
    "date_of_birth": "1993-01-01",
    "address": "123 Music Street"
}
```