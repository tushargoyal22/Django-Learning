from django.db import models
from django.core.validators import (
    EmailValidator,
    MaxValueValidator,
    MinValueValidator,
)

# Create your models here.

# every table in database is represented as a class
# every row in a database is represented by object of this class


class Student(models.Model):

    GENDERS=(
        ('f','Female'),
        ('m','Male'),
        ('u','Undisclosed')
    )

    name= models.CharField(max_length=100)
    # integer

    roll_number = models.IntegerField(unique=True)
    #Text
    
    # null=True does is that a particular attribute can be null in database
    # But it dont ensures this for ORM 
    # By default ORM does not allow blank
    # so we need blank=True

    adress = models.TextField(null=True)
    phone_number = models.CharField(max_length=15 , null=True , blank=True)
    # varchar(255)

    # email = models.EmailField(null=True) # this is fine
    # We can use validators also 
    email=models.CharField(max_length=100,null=True,validators=[EmailValidator('Email Adress is not valid dear user')])
    gender = models.CharField(max_length= 1 , choices=GENDERS,null=True)

    def __str__(self):
        return self.name
    

