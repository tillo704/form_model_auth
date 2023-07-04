from django.db import models
from phonenumber_field.modelfields import PhoneNumberField



# Create your models here.
class User(models.Model):
    user_id =  models.BigIntegerField()
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200,null=True,blank=True)
    username = models.CharField(max_length=100,null=True,blank=True)    
    email = models.EmailField()
    about = models.TextField(null=True,blank=True)
    is_married = models.BooleanField(default=False)
    birthday = models.DateField()  

class School_Years(models.Model):
    year = models.IntegerField()

    def __str__(self):
        return f"{self.year}"



class Students(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200,null=True,blank=True)
    age = models.IntegerField(null=True,blank=True)
    contact = PhoneNumberField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Subject(models.Model):
    name = models.CharField(max_length=200)
    descriptions = models.TextField(null=True,blank=True)

    def __str__(self):
        return f"{self.name}"


class Registration(models.Model):
    std = models.ForeignKey(Students, on_delete=models.CASCADE, related_name='students')
    subject = models.ManyToManyField(Subject, "subjects")
    school_year = models.ForeignKey(School_Years, on_delete=models.CASCADE, related_name='years')
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.std} {self.subject} {self.school_year} {self.date}"





 
    


