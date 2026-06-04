# Django Task Management System

A Django-based task management application with user authentication, team organization, and role-based access control.

## Features

- **User Authentication**: Registration, login, and profile management
- **Role-Based Access Control**: Manager and Employee roles with different permissions
- **Task Management**: Create, update, delete, and track tasks
- **Team Organization**: Tasks organized by team with team management
- **Task Status Tracking**: Tasks can be marked as New, In Progress, or Done
- **User Profiles**: Enhanced user profiles with role assignment and team association

## Project Structure

```
mysite/
├── manage.py                      # Django management script
├── db.sqlite3                     # SQLite database
├── DjangoApp/                     # Main application
│   ├── models.py                 # Data models (Task, Team, UserProfile)
│   ├── views.py                  # View logic and request handlers
│   ├── forms.py                  # Django forms for data input
│   ├── urls.py                   # URL routing
│   ├── admin.py                  # Django admin configuration
│   ├── migrations/               # Database migrations
│   ├── static/                   # Static files (CSS, images)
│   │   ├── css/                 # Stylesheets
│   │   └── images/              # Images
│   └── templates/                # HTML templates
│       ├── auth/                # Authentication templates
│       ├── djApp/               # App templates
│       └── task/                # Task management templates
├── mysite/                        # Project settings
│   ├── settings.py              # Django settings
│   ├── urls.py                  # Main URL configuration
│   ├── wsgi.py                  # WSGI configuration
│   └── asgi.py                  # ASGI configuration
└── Screenshots/                  # Project screenshots
```

## Models

### Task
- **id**: Auto-incrementing primary key
- **name**: Task name (max 50 characters)
- **desc**: Task description (max 1000 characters)
- **destDate**: Task destination/due date
- **status**: Current status (New, In Progress, Done)
- **performer**: Assigned user (optional, foreign key to User)
- **team**: Associated team (required, foreign key to Team)

### Team
- **name**: Team name (unique, max 100 characters)

### UserProfile
- **user**: One-to-one relationship with Django User
- **role**: User role (Manager or Employee)
- **team**: Associated team (optional)

## Installation

### Prerequisites
- Python 3.8 or higher
- pip package manager

### Setup Instructions

1. **Clone/Navigate to the project directory**
   ```bash
   cd path/to/project
   ```

2. **Create and activate virtual environment**
   ```bash
   # Windows
   python -m venv .venv
   .venv\Scripts\activate
   
   # macOS/Linux
   python3 -m venv .venv
   source .venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install django
   ```

4. **Apply database migrations**
   ```bash
   python manage.py migrate
   ```

5. **Create a superuser (admin account)**
   ```bash
   python manage.py createsuperuser
   ```

6. **Run the development server**
   ```bash
   python manage.py runserver
   ```

7. **Access the application**
   - Main app: http://127.0.0.1:8000/
   - Admin panel: http://127.0.0.1:8000/admin/

## Usage

### Authentication
- Users can register for new accounts
- Login with credentials to access the application
- Complete user profile setup with role and team assignment

### Task Management (Manager Only)
- **Create Task**: Add new tasks with description, due date, and assignment
- **Update Task**: Modify existing task details
- **Delete Task**: Remove tasks with confirmation
- **View All Tasks**: See all tasks in your team

### Employee Features
- **View My Tasks**: See tasks assigned to you
- **Update Task Status**: Change task status to track progress

## Django Admin

Access the Django admin panel at `/admin/` with your superuser credentials to:
- Manage users and their profiles
- Create and manage teams
- View and modify tasks
- Manage user roles and permissions

## Technologies Used

- **Backend**: Django 5.2.8
- **Database**: SQLite
- **Frontend**: HTML, CSS
- **Authentication**: Django built-in authentication system

## File Descriptions

- **models.py**: Defines data structures for Task, Team, and UserProfile
- **views.py**: Contains business logic and request handling
- **forms.py**: Defines HTML forms for user input
- **urls.py**: Maps URLs to views
- **settings.py**: Project configuration and settings
- **admin.py**: Django admin interface configuration
- **templates/**: HTML templates for different pages
- **static/**: CSS stylesheets and images

## Development Notes

- Debug mode is currently enabled (DEBUG = True) - disable for production
- Secret key should be changed and kept secure in production
- SQLite database is suitable for development; use PostgreSQL for production

## Future Enhancements

- Task filtering and search functionality
- Task priority levels
- Task comments and activity history
- Email notifications for task updates
- Dashboard with statistics and metrics
