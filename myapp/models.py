# from django.db import models

# # Create your models here.

# class Address(models.Model):
#     street_address = models.CharField(max_length=300,null=True, blank= True)
#     apartment_address = models.CharField(max_length=300,null=True, blank= True)
#     country = models.CountryField(multiple=False)
#     zip = models.CharField(max_length=100,null=True, blank= True)
#     address_type = models.CharField(max_length=300,null=True, blank= True)
#     default = models.BooleanField(default=False)


# class Customer(models.Model):
#     first_name = models.CharField(max_length=50,null=True, blank= True)
#     last_name =  models.CharField(max_length=30,null=True, blank= True)
#     address = models.CharField(max_length=500,null=True, blank= True)
#     city = models.CharField(max_length=30,null=True, blank= True)
#     state = models.CharField(max_length=30,null=True, blank= True)
#     postalcode = models.IntegerField()
#     country = models.CharField(max_length=30,null=True, blank= True)
#     email = models.EmailField()
#     phone_no = models.BigAutoField(primary_key=True) #primary key
#     customer_address = models.ForeignKey(Address, on_delete=models.CASCADE)

#     def __str__(self):
#         return self.first_name

    
# class Product(models.Model):
#     name = models.CharField(max_length=100,null=True, blank= True)
#     product_price = models.FloatField()
#     image = models.ImageField()
#     quantity = models.IntegerField()
#     tax_rate = models.FloatField()
    
#     def __str__(self):
#         return self.name

# class Order(models.Model):
#     order_date = models.DateTimeField()
#     quantity = models.IntegerField()
#     ship_address = models.TextField()
#     ship_date = models.DateTimeField()
#     product_name = models.ForeignKey(Product, on_delete=models.CASCADE)
#     order_address = models.ForeignKey(Address, on_delete=models.CASCADE)
#     customer_order = models.ForeignKey(Customer, on_delete=models.CASCADE)
    


# class OrderDetails(models.Model):
#     total_price = models.FloatField()
#     quantity = models.IntegerField()
#     discount = models.IntegerField()
#     ship_date = models.DateTimeField()
#     order = models.ForeignKey(Order, on_delete=models.CASCADE)
#     product = models.ForeignKey(Product, on_delete=models.CASCADE)
#     address = models.ForeignKey(Address, on_delete=models.CASCADE)


# class Cart(models.Model):
#     image = models.ImageField()
#     no_of_days = models.IntegerField()
#     is_remove = models.BooleanField()
#     customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
#     product = models.ForeignKey(Product, on_delete=models.CASCADE)



# class Payment(models.Model):
#     payment_type = models.CharField(max_length=100,null=True, blank= True)
#     payment_amount = models.FloatField()
#     payment_status = models.CharField(max_length=50,null=True, blank= True)
#     payment_date = models.DateField()
#     order = models.ForeignKey(Order, on_delete=models.CASCADE)
#     customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
#     payment_address = models.ForeignKey(Address, on_delete=models.CASCADE)


# class Coupon(models.Model):
#     coupon_code = models.CharField(max_length=30,null=True, blank= True)
#     coupon_amount = models.FloatField()
#     discount_amount = models.FloatField()
#     usage_limit = models.FloatField()        #number of times the coupon can be used before it expires)
#     expiration_date = models.DateField()
#     is_active = models.BooleanField()
#     orderdetails = models.ForeignKey(OrderDetails, on_delete=models.CASCADE)
#     cart = models.ForeignKey(Cart, on_delete=models.CASCADE)


#     def __str__(self):
#         return self.code
    
    