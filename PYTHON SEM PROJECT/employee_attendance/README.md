# Employee Attendance Management System

A web-based attendance management system built with Django, allowing employees to mark attendance, request leaves, and managers to monitor attendance and handle leave requests.

## Features

- User roles (Employee, Manager, Admin)
- Daily attendance tracking (Check-in/Check-out)
- Leave request management
- Real-time notifications
- Attendance history
- Admin dashboard
- Responsive design

## Prerequisites

- Python 3.8 or higher
- Django 4.2.1 or higher
- Other dependencies listed in requirements.txt

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd employee_attendance
```

2. Create a virtual environment and activate it:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Apply database migrations:
```bash
python manage.py migrate
```

5. Create a superuser:
```bash
python create_superuser.py
```

## Running the Application

1. Start the development server:
```bash
python manage.py runserver
```

2. Access the application:
- Main site: http://localhost:8000
- Admin interface: http://localhost:8000/admin

## Default Admin Credentials

- Username: admin
- Password: admin123
- Email: admin@example.com

## Usage

1. Login with the admin credentials
2. Create additional users through the admin interface or register page
3. Employees can:
   - Mark daily attendance
   - Submit leave requests
   - View attendance history
4. Managers can:
   - Approve/reject leave requests
   - View team attendance
5. Admins can:
   - Manage all users
   - View all attendance records
   - Handle system settings

## Project Structure

```
employee_attendance/
├── attendance/              # Main application
│   ├── migrations/         # Database migrations
│   ├── templates/         # HTML templates
│   ├── admin.py          # Admin interface configuration
│   ├── forms.py          # Form definitions
│   ├── models.py         # Database models
│   ├── urls.py           # URL routing
│   └── views.py          # View logic
├── employee_attendance/    # Project settings
├── manage.py              # Django management script
├── requirements.txt       # Project dependencies
└── README.md             # Project documentation
```
