# React-Django-Authentication-System

## Introduction
A simple authentication system built using React.js for the front end and Django for the back end. This application allows users to sign up and log in, with their credentials securely stored in a local SQLite database. It demonstrates basic user authentication, API creation, and integration between a React frontend and a Django backend.

## Description

### Frontend
The frontend of the application is built using React.js. The user interface is simple and intuitive, with two main options available on the landing page:
**Signup**: Allows new users to create an account by entering their email and password. The signup form is displayed when the "Signup" button is clicked. Upon successful registration, the user's details are stored in the backend, and a confirmation message is displayed. If the user already exists, an error message is shown.
**Login**: Allows existing users to log in by entering their registered email and password. The login form is displayed when the "Login" button is clicked. Upon successful authentication, a confirmation message is displayed. If the credentials are incorrect or the user does not exist, an error message is shown.

### Backend
The backend of the application is built using Django. It includes two main API endpoints:
**Signup API (/api/signup/)**: Handles the registration of new users. It checks if the email already exists in the database. If it doesn't, it creates a new user record with the provided email and password.
**Login API (/api/login/)**: Handles user authentication. It checks if the provided email exists and if the password matches the one stored in the database. If both are correct, the user is authenticated successfully.
The user data is stored in a simple SQLite database. The backend uses Django's ORM to interact with the database, ensuring secure and efficient data handling.

## Technologies Used
**Frontend**: React.js, CSS
**Backend**: Django, SQLite
**Other Tools**: Django CORS Headers, Git, Visual Studio Code

## Installation and Setup
To run this project locally:
1. Clone the repository:
     - git clone https://github.com/your-username/your-repository-name.git
     - cd your-repository-name
2. Setup the backend:
     - Navigate to backend directory and create a virtual environment and activate it:
         - python -m venv env
         - source .\env\Scripts\activate   #For Windows
     - Install the required dependencies:
         -  pip install django django-cors-headers
     - Run the migrations to set up the database:
         - python manage.py makemigrations
         - python manage.py migrate
     - Start the Django development server:
         - python manage.py runserver
3. Setup the frontend:
     - Navigate to the frontend directory and install the required dependencies:
         - npm install
     - Start the React development server:
         - npm start
4. Access the application:
     - Open the web browser and navigate to the localhost server on which the application has been started
  

