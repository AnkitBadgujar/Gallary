from django.db import models

# Create your models here.

class Category(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=150, null=False, blank=False)

class Photo(models.Model):
    id = models.AutoField(primary_key=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)
    image = models.ImageField(null=False,blank=False)
    description = models.TextField()

