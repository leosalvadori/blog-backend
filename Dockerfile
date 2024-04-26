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
RUN pip install -r requirements.txt

# Copy project
COPY . /backend/