from typing import Iterable, Optional
from django.utils.text import slugify
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

class Customer(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200,null=True,blank=True)
    contact = models.OneToOneField(to="Contact", on_delete=models.CASCADE)
    address = models.ForeignKey(to="Address",on_delete=models.CASCADE)


    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"
    


class Order(models.Model):
    customer = models.ForeignKey(to=Customer,on_delete=models.CASCADE,related_name="orders")
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    created = models.DateTimeField(auto_now_add=True)
    products = models.ManyToManyField(to="Product")


    def __str__(self) -> str:
        return f"{self.customer.first_name} - {self.total_price}"
    

class Contact(models.Model):
    email = models.EmailField(max_length=100)
    phone = PhoneNumberField(unique = True)

    def __str__(self) -> str:
        return f"{self.email} {self.phone}"



class Address(models.Model):
    UZB ="uzb"
    RUS ="rus"
    TRK = "trk"
    QZK= "qzk"
    TJK ="tjk"
    COUNTRIES = (
        (UZB,"Uzbekistan"),
        (RUS,"Russia"),
        (TRK,"Turkmaniston"),
        (QZK,"Kazaqiston"),
        (TJK, "Tojikiston")
    )


    street= models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    zipcode = models.CharField(max_length=15)
    country = models.CharField(max_length=20, choices=COUNTRIES,default=UZB)


    def __str__(self) -> str:
        return f"{self.street},{self.city},{self.country}"
    

class Category(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200,unique=True,blank=True)

    def save(self, *args,**kwargs):
        self.slug = slugify(self.title)
        super(Category,self).save(*args,**kwargs)
        

    def __str__(self) -> str:
        return self.title



class Product(models.Model):
    title = models.CharField(max_length=100)
    descriptions = models.TextField(max_length=400,null=True,blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE,null=True)
    price = models.DecimalField(max_digits=10,decimal_places=2)
    image = models.ImageField(upload_to="products/",null=True)
    in_stock = models.BooleanField(default=True)


    def __str__(self) -> str:
        return f"{self.title} - {self.price}"
    
    class Meta:
        ordering = ['-id']