from django.db import models
# Create your models here.

class Product(models.Model):
    id = models.AutoField(primary_key=True)
    product_ref = models.TextField(unique=True)
    product_title= models.TextField()
    product_slug = models.TextField()
    product_category = models.TextField()
    created_at = models.DateTimeField(auto_now=True)