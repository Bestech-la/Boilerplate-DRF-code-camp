# Workhub Link for RAD Backend API

This application enables Django powered API via PostgreSQL, Django Rest Framework with authentication and access control.

    # Create a new database
    CREATE DATABASE 'boilerplate_drf_codecamp'

## Basic Settings for Development

Activate environment

    python3 -m venv venv
    source venv/bin/activate

### Install dependencies

    python -m pip install Pillow
    export CFLAGS="-I/usr/local/opt/openssl/include"Difference between one-to-one and one-to-many relationship in a database
    export LDFLAGS="-L/usr/local/opt/openssl/lib"
    pip install cryptography
    pip install -r requirements/dev.txt
    pip install -r requirements/freeze.txt

### Create .env File

To set up the environment variables for this project, create a `.env` file from the `.env.example` file by running the following command in your terminal:

    cp .env.example .env

### Basic Settings

You’ll have to make the following creations to your .env file
and Django Secret Key

    DB_NAME=your_database_name
    DB_USR=your_user_name
    DB_PWD=your_password

    SECRET_KEY='your_secret_key'

### Make migrations and Apply to database # create migrations files (every new django app)

    python manage.py makemigrations
    python manage.py makemigrations user product profile brand district category
    python manage.py migrate

### Setup Initial User as Admin

    # create first user
    python manage.py createsuperuser
    python manage.py runserver

### Navigate to

    # for Swagger API
    localhost:8000/swagger/
    # or CRUD admin pandel
    localhost:8000/admin/


## For User Group Creation for API Access

API Endpoint
The API endpoint for creating a user group is:
POST http://127.0.0.1:8000/api/v1/group
Send a POST request to the above endpoint with the following JSON body:

    ### Request Body
    application/json
    ```json

    {
        "name": "staff"
    }

## Further Development

### Create a new app

    cd apps
    python ../manage.py startapp "folder name"

### For Checking before deploy

#### API/ Unit Test

    python manage.py test

#### Deploy checklist

    python manage.py check --deploy

#### Check Style

    pip install flake8
    flake8 apps/
    flake8 commmon/

#### Check Pylint

    pylint --rcfile=.pylintrc apps --ignore=migrations,tests --django-settings-module=core.settings
    pylint --rcfile=.pylintrc common --ignore=migrations,tests  --django-settings-module=core.settings

### Django Rest Framework Integration Testing

add doc to view function as below,

    class ListUserView(ListAPIView):

| """                                                 |
| --------------------------------------------------- |
| # Testing Notes                                     |
| - Passes ListUserView API tests: {api_tests_passed} |
| - Test Coverage: {test_coverage}%                   |
| ---                                                 |
| """                                                 |
| queryset = User.objects.all()                       |
| serializer_class = UserSerializer                   |

then write testcases for the views, then add mapping to common/test/view_test_mapping.py

    views_to_update = [
        (ListUserView, UserAPITestCase),
    ]

#### To run Test

    python manage.py test

#### To Run Test Coverage

    coverage run manage.py test -v 2 && coverage report && coverage html
