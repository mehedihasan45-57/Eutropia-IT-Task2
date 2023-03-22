from django.db import models


# Create your models here.



class TCloths(models.Model):
    name = models.CharField(max_length=255)
    price = models.FloatField()
    image = models.ImageField(upload_to='images')
    def __str__(self):
        return f"{self.name}   ({self.price})"
    
class SCloths(models.Model):
    name = models.CharField(max_length=255)
    price = models.FloatField()
    image = models.ImageField(upload_to='images')
    def __str__(self):
        return f"{self.name}   ({self.price})"
    
class WCloths(models.Model):
    name = models.CharField(max_length=255)
    price = models.FloatField()
    image = models.ImageField(upload_to='images')
    def __str__(self):
        return f"{self.name}   ({self.price})"
    


class Mobile(models.Model):
    name = models.CharField(max_length=255)
    price = models.FloatField()
    image = models.ImageField(upload_to='images')
    def __str__(self):
        return f"{self.name}   ({self.price})"
    
class Computer(models.Model):
    name = models.CharField(max_length=255)
    price = models.FloatField()
    image = models.ImageField(upload_to='images')
    def __str__(self):
        return f"{self.name}   ({self.price})"

class Laptop(models.Model):
    name = models.CharField(max_length=255)
    price = models.FloatField()
    image = models.ImageField(upload_to='images')
    def __str__(self):
        return f"{self.name}   ({self.price})"
    


class Jumkas(models.Model):
    name = models.CharField(max_length=255)
    price = models.FloatField()
    image = models.ImageField(upload_to='images')
    def __str__(self):
        return f"{self.name}   ({self.price})"
    
class Necklaces(models.Model):
    name = models.CharField(max_length=255)
    price = models.FloatField()
    image = models.ImageField(upload_to='images')
    def __str__(self):
        return f"{self.name}   ({self.price})"
    
class Kangans(models.Model):
    name = models.CharField(max_length=255)
    price = models.FloatField()
    image = models.ImageField(upload_to='images')
    def __str__(self):
        return f"{self.name}   ({self.price})"

