# REST-API
Employee REST api

Create a Virtual Environment 'Env'

```
virtualenv Env
source Env/bin/activate
```



# Configuring MySQL

1. configure MySQL Server on the local machine,
2. Update the credentials under 'tutorial/settings.py'

```
DATABASES = {
    'default': {
        'ENGINE'    : 'django.db.backends.mysql',
        'NAME'      : 'employees',
        'USER'      : 'USERNAME',
        'PASSWORD'  : 'PASSWORD',
        'HOST'      : 'localhost',
        'PORT'      : ''
    }
```    

```
pip install -r Requirements.txt
```

## Launch Server

```
./tutorial/manage.py runserver
```

Endpoints you can try:

# CREATE AN EMPLOYEE RECORD

http POST http://localhost:8000/employees firstname="Jagadeesh" lastname="Rampam" email="jagadeesh@wilderhood.com" phoneno="+919986507298" role=1

Sample output would be 
```
{
    "email": "jagadeesh@wilderhood.com",
    "firstname": "Jagadeesh",
    "lastname": "Rampam",
    "phoneno": "9986507298",
    "pk": 1,
    "role": true
}
```
# LIST ALL EMPLOYEES

http GET http://localhost:8000/employees/

# UPDATE AN EXISTING EMPLOYEE
http PUT http://localhost:8000/employees/1/ phoneno="+919986507475"

Sample output would be 
```
{
    "email": "jagadeesh@wilderhood.com",
    "firstname": "Jagadeesh",
    "lastname": "Rampam",
    "phoneno": "+919986507475",
    "pk": 1,
    "role": true
}
```

# DELETE AN EMPLOYEE
http DELETE http://localhost:8000/1/

