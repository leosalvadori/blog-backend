# Blog Backend

This is the backend for a blog application built with Django and Django Rest Framework.

## Features

- User authentication with JWT
- CRUD operations for blog posts
- Commenting on blog posts

## URLs

This project includes the following URLs:

1. Authentication - [authentication/urls.py](authentication/urls.py)

- *`api/v1/authentication/token/`*: Obtain a pair of JWT tokens (access and refresh).
- *`api/v1/authentication/token/refresh/`*: Refresh the JWT token.
- *`api/v1/authentication/token/verify/`*: Verify the JWT token.
- *`api/v1/authentication/register/`*: Register a new user.

2. Posts - [posts/urls.py](posts/urls.py)

- *`api/v1/posts/`*: List all posts.
- *`api/v1/posts/create/`*: Create a new post.
- *`api/v1/posts/<int:pk>/update/`*: Update a post.
- *`api/v1/posts/<int:pk>/delete/`*: Delete a post with the given pk (primary key).

3. Comments - [comments/urls.py](comments/urls.py)

- *`api/v1/posts/<int:pk>/add_comment/`*: Add a comment to the post with the given pk.
- *`api/v1/posts/<int:pk>/comments/`*: List all comments for the post with the given pk.

## Setup

### Requirements

- Python 3.8+
- Docker and Docker Compose

### Installation

1. Clone the repository:

```sh
git clone https://github.com/leosalvadori/blog-backend.git
cd blog-backend
```

2. Create a *`.env`* at the same level of manage.py

3. Copy *`.env_example`* data to *`.env`* file

4. Build the Docker image:

```sh
docker-compose build
```

5. Run the Docker containers:

```sh
docker-compose up
```

The application will be available at `http://localhost:8000`.

### Database

This application uses PostgreSQL as its database. The default database name, user, and password are all 'postgres'. You can change these in the `DATABASES` setting in `.env` file.

## Migrate the DB

```sh
docker-compose run web python manage.py migrate
```

## Create a Django admin superuser

```sh
docker-compose run web python manage.py createsuperuser
```

## Testing

To run the tests, use the following command:

```sh
docker-compose run web python manage.py test
```
