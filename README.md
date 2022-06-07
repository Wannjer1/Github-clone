# INSTA-CLONE

A clone of the website for the popular photo app instagram

## Getting Started

To get a copy of the project up and running on your local machine for development and testing purposes;

1. Clone the repository
   > git clone https://github.com/Wannjer1/Github-clone.git
2. Create a virtual environment
   > virtual3 -m venv venv
   > source venv/bin/activate
3. Install the project dependencies
   > (venv) $ pip install -r requirements.txt
4. Create a postgress db
5. Apply all migrations
   > (venv) $ python manage.py migrate
6. Create admin account
   > (venv) $ python manage.py createsuperuser
7. Make migrations to your database
   > (venv) $ python manage.py makemigrations (appname)
   > (venv) $ python manage.py migrate
8. Start development server
   > (venv) $ python3 manage.py runserver

## Running Tests

Run automated tests for this system

> (venv) $ python3 manage.py test (appname)

## Deployment

With all environment variables changed to suit your local copy of this repository, deploy the application to Heroku to see it live

## Behaviour Driven Development

## Built with

- Django 4.0.1-web framework
- Python3.9- backend logic
- PostgreSQL- database system
- Heroku- deployment platform

## Author

Ann Wanjeri

## License

MIT License
