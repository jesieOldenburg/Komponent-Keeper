# # Komponent Keeper
An app for designers and developers to track design assets and their associated code. Created with the intent on solving the problem of design handoff between UI/UX designers and developers.

## Installation

To run this app locally on your machine, follow these steps:

1. Clone this repo into your machine.
2. Run the following command to create a virtual environment, and install the project dependencies:

```shell
cd Komponent-Keeper
python -m venv KomponentKeeperEnv
source ./KomponentKeeperEnv/bin/activate
pip install django Pillow django-bootstrap4
pip freeze > requirements.txt
```

### Creating Database Tables

1. Run the following commands to apply the models to your database tables:

```shell
python manage.py makemigrations 
python manage.py migrate
```

### Create Superuser and User Accounts

1. Create your user account by running `python manage.py createsuperuser` and remember your credentials, you’ll need them soon!
2. Start the development server by running `python manage.py run server` then navigate to http://localhost:8000/admin/ to enter the application’s administrative application.  
3. Login to the application using your superuser credential, then click the add button next to users.
4. Create a new user in the application and save them. This will save the user to the database. **THIS STEP IS CRUCIAL FOR LOADING THE TEST DATA TO THE DATABASE!!**.

### Populate the database with test data

The following steps are crucial to see the true functionality of the application.  

1. Run the following command to load all of the fixtures to the database:

   `python3 manage.py loaddata komponentkeeperapp/fixtures/*.json`

2. Navigate to http://localhost:8000/ and login to your account.


## Built With

* [Django](https://www.djangoproject.com/) - The Python web framework for perfectionists with deadlines
* [Django Bootstrap](https://github.com/zostera/django-bootstrap4) - Bootstrap 4 integrated with Django

## Authors
* **Jesie Oldenburg**
