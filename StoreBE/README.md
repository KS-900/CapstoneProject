# CapstoneProject
This is a e-commerce project.
Creating data modles in the shop and tag app.
Next week will be talking views and users.
class Promotion(models.Model):
    description = models.CharField(max_length=200)
    discount = models.FloatField()
    start_date = models.DateTimeField(auto_now_add=True)
    end_date = models.DateTimeField()

class Collecction(models.Model):
    title = models.CharField(max_length=200)
    featured_product = models.ForeignKey('Product', on_delete==models.SET_NULL, null=True, related_name='+')

class Product(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=7, decimal_places=2)
    iventory = models.PositiveIntegerField()
    last_update = models.DateTimeField(auto_now=True)
    Collecction = models.ForeignKey(Collecction, on_delete=models.PROTECT)
    promotions = models.ManyToManyField(Promotion,)

class Customer(models.Model):
    first_name = models.CharField(max_length=200)
    lasst_name = models.CharField(max_length=200)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=200)
    birth_date = models.DateTimeField(null=True) 

class Order(models.Model):
    placed_at = models.DateTimeField(auto_now=True)
    PENDING =  'P'
    COMPLETE = 'C'
    FAILED = 'F'
    payment_status_choices =[
        (PENDING, 'Pending'),
        (COMPLETE, 'Complete'),
        (FAILED, 'Failed'),
    ]
    payment_status = models.CharField(max_length=1, default=PENDING)
    customer = models.ForeignKey(Customer, on_delete=models.PROTECT)

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.PROTECT)
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    quantity = models.PositiveSmallIntegerField()
    base_price = models.DecimalField(max_digits=7, decimal_places=2)

class Address(models.Model):
    street = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    Customer = models.ForeignKey(Customer,on_delete=models.CASCADE)

class Cart(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveSmallIntegerField()