BE Capstone Project: e-commerce store API 

e-commerce store API using Django REST Framework.

The API will allow users to manage their orders and carts by creating, updating and deleting their orders and tasks.

The API will allow admins the ability to add products, customers, collections 

Register and log in -Endpoints
Registering
endpoint-auth/users/
"id": 2,
    "username": "abo_nkunku",
    "password": "ILoveDjango"
    "email": "kb1.satekge@gmail.com",
    "first_name": "Abo",
    "last_name": "nkunku"

LoginIn
auth/jwt/create
"username": "abo_nkunku",
    "password": "ILoveDjango"
    "email": "kb1.satekge@gmail.com",

then move to ModHeader 
use Authorization and JWT [Token]


2. API Endpoints
API Root
store/
{
    "products": "http://127.0.0.1:8000/store/products/",
    "collections": "http://127.0.0.1:8000/store/collections/",
    "carts": "http://127.0.0.1:8000/store/carts/",
    "customers": "http://127.0.0.1:8000/store/customers/",
    "orders": "http://127.0.0.1:8000/store/orders/"
}
Product list
store/products/
[List of all products]

Product ID(DELETE,UPDATE)
store/products/<id>
[Will show product matching ID]

[SAME APPLIES TO
CUSTOMER
COLLECTION
CART
ORDER
]

for the admin side 
we use the superuser
endpoint
admin/


username: admin
email: kb2.satekge@gmail.com
Password: 123123

3. Technology Stack


Back-End: Django (Django Rest Framework)


Database: MySQL

https://chromewebstore.google.com/detail/modheader-modify-http-hea/idgpnmonknjnojddfkpgkljpfnnfcklj 
# CapstoneFinal