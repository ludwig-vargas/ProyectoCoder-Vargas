from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=40)
    code_product = models.IntegerField()
    category = models.CharField(max_length=40)
    price = models.IntegerField()
    amount = models.IntegerField()
    description = RichTextField(null = True, blank = True)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    
    def __str__(self):
        return f'Product: {self.name} | Price: {self.price} | Category: {self.category}'
