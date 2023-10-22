# BEGIN: 8f7d6e2b7c3a
#!/bin/bash

# Wait for the database to be available
until nc -z db 5432; do
    echo "Waiting for database to be available..."
    sleep 1
done

# Run Django migrations
python manage.py migrate

# Try to create superuser
echo "Creating superuser..."
python manage.py createsuperuser --noinput --email admin@admin.com

# Start the Django development server
python manage.py runserver 0.0.0.0:8000
