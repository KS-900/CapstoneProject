Store Back-End Project Documentation(Capstone Part 2)


Project Overview


This project is a back-end system for an online store, designed with two apps:


1. stor - Manages products, collections, customers, carts, and orders.

2. Tag - Manages product tagging with a tagging system.
3. core - Managers the users








1. Features of the Project


store App


Products: Create, update, delete, and list products.


Collections: Organize products into categories.


Customers: Manage customer information.


Cart: add/remove products before checkout.


Orders: Track customer purchases and order history.




Tag App


Tags: Labels that can be assigned to products.


TaggedItems: Links between tags and products.






2. API Endpoints
API Root
store/
Product list
store/products/
Product ID(DELETE,UPDATE)
store/products/<id>

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

auth/jwt/create
superuser
admin
kb2.satekge@gmail.com
123123
3. Technology Stack


Back-End: Django (Django Rest Framework)


Database: MySQL


Tools: draw.io for ERD




6. ERD image
	[Store ERD]

[Tags ERD]

7. Relationships
Tag will have a many to one relationship with TaggedItem.
Product and cart will have a many to many relationship and uses cartItem to function efficiently.
Collection will have a many to one relationship with products.
Collection will have a many to one relationship with customers.
Customers have a one to many relationship with orders.
Product and order will need OrderItem to function efficiently.

