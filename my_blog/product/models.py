from django.contrib.auth.models import User
from django.core.validators import MinLengthValidator
from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=40, null=False, blank=False)
    code_product = models.CharField(max_length=40, null=False, blank=False)
    category = models.CharField(max_length=40, null=False, blank=False)
    price = models.IntegerField(null=False, blank=False)
    amount = models.IntegerField(null=False, blank=False)
    description = RichTextField(null = True, blank = True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    comments = models.ManyToManyField(
        User, through="Comment", related_name="comments_owned"
    )    
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    
    class Meta:
        unique_togrther = (
            "name",
            "code_product",
        )
        ordering = ["-created_at"]
    
    def __str__(self):
        return f'Product: {self.name} | Price: {self.price} | Category: {self.category}'

class Comment(models.Model):
    text = models.TextField(
        validators=[
            MinLengthValidator(10, "El comentario debe ser mayor de 10 caracteres")
        ]
    )
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)