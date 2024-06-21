# Blog Application

This is a blog application built with Django and Django REST Framework (DRF). It features user authentication, CRUD operations for posts and comments, search and filtering, pagination, and an admin interface. The application is containerized using Docker and deployed on Render.

## Table of Contents

- [Features](#features)
- [Setup Instructions](#setup-instructions)
  - [Local Setup](#local-setup)
  - [Docker Setup](#docker-setup)
- [API Endpoints](#api-endpoints)
- [Deployment](#deployment)
- [Links](#links)

## Features

- User Authentication (registration, login, logout, profile management)
- CRUD operations for Posts and Comments
- Search functionality by title and content
- Filtering by categories and tags
- Pagination for posts
- Admin interface for managing posts, categories, tags, comments, and profiles
- Deployment with Docker and Render

## Setup Instructions

### Local Setup

1. Clone the repository:
    ```bash
    git clone https://github.com/AbdelrahmanElsaeid/Blog-Application-DRF.git
    cd Blog-Application-DRF
    ```
2. Create a virtual environment and activate it:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```
3. Install the dependencies:
    ```bash
    pip install -r requirements.txt
    ```
4. Apply the migrations:
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

### Docker Setup

1. Build and run the Docker containers:
    ```bash
    docker-compose up --build
    ```
2. Run migrations inside the Docker container:
    ```bash
    docker-compose run web python manage.py migrate
    ```
3. Create a superuser:
    ```bash
    docker-compose run web python manage.py createsuperuser
    ```

## API Endpoints

- `/api/posts/` - List and create posts
- `/api/posts/<id>/` - Retrieve, update, and delete a post
- `/api/categories/` - List categories
- `/api/tags/` - List tags
- `/api/comments/` - List and create comments
- `/api/comments/<id>/` - Delete a comment
- `/api/user/auth/login/` - Login
- `/api/user/auth/logout/` - Logout
- `/api/user/signup//` - Signup
- `/api/user/profile/` - Profile Retrieve and update and delete

## Deployment

To deploy using Docker, run:
```bash
docker-compose up --build
```

## Links
- GitHub Repository: [Link to Repository](https://github.com/AbdelrahmanElsaeid/Blog-Application-DRF/tree/main)
- Deployed Application: [Link to Production](https://dev7-task-blog-djangoserver-tag.onrender.com)
- API Documentation: [Link to API Documentation](https://documenter.getpostman.com/view/33964071/2sA3XWbdFS)




