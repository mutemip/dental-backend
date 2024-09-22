# Dental Management Platform REST API
 - This is a management system api for a dental clinic.


## Setup virtual environment
 - Create a virtual environment: `pyhton -m venv <your-env-name>`
 - Activate virtual environment: `source <you-env-name>/bin/activate`

# How to set up the project.
- Clone the project repo: `git clone git@github.com:mutemip/dental-backend.git`
- Navigate into project folder using: `cd dental-backend`
- Project structure:


    ![alt text](https://github.com/mutemip/dental-backend/blob/master/screens/structure.png?raw=true)


- Install project requirement libraries: `pip install -r requirements.txt`
- Ensure you setup your postgres database and create a `.env` file. Follow `.env.example`

    ### PostgreSQL Setup

    ```
        DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': os.getenv('POSTGRESQL_DB'),
            'USER': os.getenv('POSTGRESQL_USER'),
            'PASSWORD': os.getenv('POSTGRESQL_PASSWORD'),
            'HOST': os.getenv('POSTGRESQL_HOST'),
            'PORT': os.getenv('POSTGRESQL_PORT'),
        }
        }
    ```

    ### .env example
    ```
        POSTGRESQL_DB=<db_name>
        POSTGRESQL_USER=<db_user>
        POSTGRESQL_PASSWORD=<db_password>
        POSTGRESQL_HOST=localhost
        POSTGRESQL_PORT=5432

        SECRET_KEY= "<secret_key>" Example: 'django-insecure-9k*92jdzml7h1=@1vkp_g6-reqd%8%xdcb7amgwl!kbtx^7-yd'
    ```

## Makemigrations and migrate
 - After successful db setup:
   - Makemigrations: `python manage.py makemigrations`
   - Migrate: `python manage.py migrate`
   - Create super user: `python manage.py createsuperuser`
   - Run server: `python manage.py runserver`

## Available REST API Endpoints

![alt text](https://github.com/mutemip/dental-backend/blob/master/screens/endpoints.png?raw=true)


 - All endpoints have necessary  ``HTTP Methods``
    ```
    GET,
    POST,
    PUT,
    PATCH,
    DELETE
    ```
 - Use Postman collection file for endpoints setup: <>

 # Key Features
   - Login endpoint
    - Endpoint: `http://127.0.0.1:8000/api/login/`
  - Ability to add, update, view details and delete clinic details
    - Endpoint: `http://127.0.0.1:8000/api/clinics/`
  - Ability to add, update, view details and delete doctor details
    - Endpoint: `http://127.0.0.1:8000/api/doctors/`
  - Ability to add, update, view details and delete patient details
    - Endpoint: `http://127.0.0.1:8000/api/patients/`
  - Ability to add, update, view details and delete clinic-doctor affiliation details. Enables tracking doctors affiliated to certain clinic.
    - Endpoint: `http://127.0.0.1:8000/api/affiliation/`
  - Ability to add, update, view details and delete visits details. Enables to track patients clinic visits.
    - Endpoint: `http://127.0.0.1:8000/api/visits/`
  - Ability to add, update, view details and delete appointments details. Enables tracking patients appointments with doctors.
    - Endpoint: `http://127.0.0.1:8000/api/appointments/`

 - Clinic-Doctor Affiliations: `http://127.0.0.1:8000/clinics/{clinic_id}/affiliated doctors`
 - Doctor-Clinic Affiliations: `http://127.0.0.1:8000/doctors/{doctor_id}/affiliated_clinics`
 - Doctor-patients affiliations: `http://127.0.0.1:8000/doctors/{doctor_id}/affiliated_patients`
 - Patient vists: `http://127.0.0.1:8000/patients/{patient_id}/visits`

 There is room for improvement.