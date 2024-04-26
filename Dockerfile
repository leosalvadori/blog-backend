# Use an official Python runtime as a parent image
FROM python:3.12.3

# prevents pyc files
ENV PYTHONDONTWRITEBYTECODE 1

# unbuffered mode
ENV PYTHONUNBUFFERED 1

# Set work directory
WORKDIR /backend

# Install dependencies
COPY requirements.txt /backend/
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# Copy project
COPY . /backend/

# Collect static files
RUN python manage.py collectstatic --noinput

CMD ["gunicorn", "--bind", "0.0.0.0:8000", "--workers", "2", "blog.wsgi"]