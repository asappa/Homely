# homely
homely home rent repository

To execute:
Create python virtual environment 

Install dependecies
$> pip install -r requirements.txt
$> python manage.py createsuperuser

1. Create User

 Note: input type owner/renter if owner create owner account, if renter it creates renter account

url : http://127.0.0.1:8000/users/create-user/

type: POST

input data: 

{"first_name":"test", "last_name":"user", "username":"testuser", "password":"admin123", "email":"something@gmail.com","type":"owner","phone":"1112223333","address":"someethingg"}

output:

{
    "status": "1",
    "msg": "Created Succesfully"
}

 2. Retrieve, Update and Delete of user profile

id of the user is passed


API: http://127.0.0.1:8000/users/get-user/1/

3. Create home details

API : http://127.0.0.1:8000/users/create-home/


4. Retrieve, update and delete home details

API: http://127.0.0.1:8000/users/get-home/1/


5. create Home Rent details

API: http://127.0.0.1:8000/users/create-rent/

6. Get, Update, Delete Rent
API: http://127.0.0.1:8000/users/get-rent/1/



