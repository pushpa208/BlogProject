# Django Blog Application

## Introduction
This is a simple blog application built using Django and Django REST Framework. The application provides APIs for managing blog posts and comments with basic CRUD functionalities and token-based authentication.

## Features
- Create, read, update, and delete blog posts.
- Add comments to posts.
- Token-based authentication for secure access.
- Pagination for listing posts.
- Functionality to like/unlike a post and view the number of likes.

## Prerequisites
- Python 3.8+
- Django 4.x
- Django REST Framework
- A virtual environment (recommended)

## Setup Instructions

1. **Clone the Repository:**
   ```bash
   git clone <repository_url>
   cd django_blog_application
   ```

2. **Set Up Virtual Environment:**
   ```bash
   python -m venv env
   source env/bin/activate  # On Windows: env\Scripts\activate
   ```

3. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run Migrations:**
   ```bash
   python manage.py migrate
   ```

5. **Create a Superuser:**
   ```bash
   python manage.py createsuperuser
   ```

6. **Run the Development Server:**
   ```bash
   python manage.py runserver
   ```

7. **Access the Application:**
   Open your browser and navigate to `http://127.0.0.1:8000/admin` to access the Django admin panel or interact with the APIs at `http://127.0.0.1:8000/api/`.

## API Documentation

### Authentication

#### Obtain Token
**Endpoint:** `POST /api/token/`

**Request:**
```json
{
  "username": "your_username",
  "password": "your_password"
}
```

**Response:**
```json
{
  "access": "<access_token>",
  "refresh": "<refresh_token>"
}
```

#### Refresh Token
**Endpoint:** `POST /api/token/refresh/`

**Request:**
```json
{
  "refresh": "<refresh_token>"
}
```

**Response:**
```json
{
  "access": "<new_access_token>"
}
```

### Posts

#### List Posts
**Endpoint:** `GET /api/posts/`

**Response:**
```json
[
  {
    "id": 1,
    "title": "First Post",
    "content": "This is the content of the first post.",
    "author": "admin",
    "published_date": "2024-12-01T10:00:00Z",
    "likes_count": 5,
    "comments": []
  }
]
```

#### Create a Post
**Endpoint:** `POST /api/posts/`
**Headers:** `Authorization: Bearer <access_token>`

**Request:**
```json
{
  "title": "New Post",
  "content": "This is a new post."
}
```

**Response:**
```json
{
  "id": 2,
  "title": "New Post",
  "content": "This is a new post.",
  "author": "admin",
  "published_date": "2024-12-01T11:00:00Z",
  "likes_count": 0,
  "comments": []
}
```

#### Like a Post
**Endpoint:** `POST /api/posts/<post_id>/like/`
**Headers:** `Authorization: Bearer <access_token>`

**Response:**
```json
{
  "likes_count": 6
}
```

### Comments

#### List Comments for a Post
**Endpoint:** `GET /api/posts/<post_id>/comments/`

**Response:**
```json
[
  {
    "id": 1,
    "post": 1,
    "author": "John",
    "text": "Great post!",
    "created_date": "2024-12-01T10:15:00Z"
  }
]
```

#### Create a Comment
**Endpoint:** `POST /api/posts/<post_id>/comments/`
**Headers:** `Authorization: Bearer <access_token>`

**Request:**
```json
{
  "author": "John",
  "text": "Nice article!"
}
```

**Response:**
```json
{
  "id": 2,
  "post": 1,
  "author": "John",
  "text": "Nice article!",
  "created_date": "2024-12-01T11:20:00Z"
}
```

## Testing
To run tests, use the following command:
```bash
python manage.py test
```

## Additional Notes
- Ensure that the `requirements.txt` file includes all dependencies.
- Use environment variables for sensitive information like database credentials in a production environment.

## License
This project is licensed under the MIT License. See the LICENSE file for details.
