from django.db import models
import datetime


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True 

class Category(BaseModel): 
    name = models.CharField(max_length=50)

    def __str__(self): 
        return self.name

    class Meta: 
        verbose_name_plural = 'categories'


class Customer(BaseModel): 
    first_name =models.CharField(max_length=50)
    last_name =models.CharField(max_length=50)
    phone = models.CharField(max_length=10)
    email = models.EmailField(max_length=100)
    password =models.CharField(max_length=100)

    def __str__(self): 
        return(f"{self.first_name} {self.last_name}")

class Product(BaseModel): 
    name = models.CharField(max_length=100)
    price = models.DecimalField(default=0, decimal_places=2, max_digits=6)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)
    description = models.CharField(max_length=250, default='', blank=True, null=True)
    image = models.ImageField(upload_to='uploads/products/')
    #Sale
    is_sale = models.BooleanField(default=False)
    sale_price = models.DecimalField(default=0, decimal_places=2, max_digits=6)

    def __str__(self): 
        return self.name


class Order(BaseModel):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    address = models.CharField(max_length=100, default='',blank=True)
    phone = models.CharField(max_length=12, default='', blank=True)
    date = models.DateField(default=datetime.datetime.today)
    status = models.BooleanField(default=False) 

    def __str__(self): 
        return(f"{self.product}")
    
# class Checkout(BaseModel)
#     item = models.ForeignKey(Inventory)
#     user = models.ForeignKey(User)
#     checked_out = models.DateTimeField()
#     checked_in = models.DateTimeField(null=True)