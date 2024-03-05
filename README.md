# AI Tools API

This is a Django-based API for AI tools.

## Unique Features

- **Hyperlinked Model Serializers**: This project uses Django Rest Framework's HyperlinkedModelSerializer, which uses hyperlinks to represent relationships, rather than primary keys. This makes the API more navigable.

- **Image Optimization with PIL and BytesIO**: The project uses the Python Imaging Library (PIL) and BytesIO to optimize images before saving them to the database. This reduces the storage space required for images and improves the performance of the API.

- **RESTful API**: The API supports all the standard HTTP methods (GET, POST, PUT, DELETE) for interacting with resources. This makes it easy to integrate with other systems and services.

- **Model ViewSets**: The project uses Django Rest Framework's ModelViewSet, which is a class-based view that provides default `list()`, `create()`, `retrieve()`, `update()`, and `destroy()` actions. This reduces the amount of code needed to create the API.

## Project Structure
'''bash
|   db.sqlite3
|   manage.py
|   README.md
|   requirements.txt
|
+---Api_app
|   |   admin.py
|   |   apps.py
|   |   models.py
|   |   serializers.py
|   |   tests.py
|   |   urls.py
|   |   views.py
|   |   __init__.py
|   |
|   +---migrations
|   |   |   0001_initial.py
|   |   |   0002_mainai_keywords_mainai_version_alter_mainai_id.py
|   |   |   __init__.py
|   |   |
|   |   \---__pycache__
|   |           0001_initial.cpython-312.pyc
|   |           0002_mainai_keywords_mainai_version_alter_mainai_id.cpython-312.pyc
|   |           __init__.cpython-312.pyc
|   |
|   \---__pycache__
|           admin.cpython-312.pyc
|           apps.cpython-312.pyc
|           models.cpython-312.pyc
|           serializers.cpython-312.pyc
|           urls.cpython-312.pyc
|           views.cpython-312.pyc
|           __init__.cpython-312.pyc
|
+---Api_main
|   |   asgi.py
|   |   settings.py
|   |   urls.py
|   |   wsgi.py
|   |   __init__.py
|   |
|   \---__pycache__
|           settings.cpython-312.pyc
|           urls.cpython-312.pyc
|           wsgi.cpython-312.pyc
|           __init__.cpython-312.pyc
|
\---images
        bg.png
        bg_f6ZEghe.png


'''

## Built With

- [Python](https://www.python.org/) - The programming language used.
- [Django](https://www.djangoproject.com/) - The web framework used.
- [Django REST Framework](https://www.django-rest-framework.org/) - The toolkit used to build the API.
* [![python][python.com]][python-url]


## Setup

1. Clone the repository:

    ```sh
    git clone https://github.com/vidhyasagargslv
    ```

2. Navigate to the project directory:

    ```sh
    cd Api_main
    ```

3. Install the required packages:

    ```sh
    pip install -r requirements.txt
    ```

4. Run the migrations:

    ```sh
    python manage.py migrate
    ```

5. Start the server:

    ```sh
    python manage.py runserver
    ```

## Usage

You can interact with the API using HTTP requests. For example, to get a list of all `Mainai` instances, you can send a GET request to `http://localhost:8000/api/mainai/`.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.