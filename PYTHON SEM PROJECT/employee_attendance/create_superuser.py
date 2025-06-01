import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'employee_attendance.settings')
django.setup()

from attendance.models import User

def create_superuser():
    if not User.objects.filter(username='admin').exists():
        User.objects.create_superuser(
            username='admin',
            email='admin@example.com',
            password='admin123',
            role='admin'
        )
        print("Superuser created successfully!")
    else:
        print("Superuser already exists.")

if __name__ == '__main__':
    create_superuser()
