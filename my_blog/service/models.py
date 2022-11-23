from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from django.core.validators import MinLengthValidator

# Create your models here.
class Service(models.Model):
    name = models.CharField(max_length=40, null=False, blank=False)
    code_service = models.CharField(max_length=40, null=False, blank=False)
    category = models.CharField(max_length=40, null=False, blank=False)
    price = models.IntegerField(null=False, blank=False)
    numberphone = models.IntegerField(null=False, blank=False)
    email = models.EmailField(null=False, blank=False)
    description = RichTextField(null = True, blank = True)
    image = models.ImageField(upload_to='service', null=True, blank=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, null = True,)
    comments = models.ManyToManyField(
        User, through="CommentService", related_name="commentser_owned"
    )
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    
    class Meta:
        unique_together = (
            "name",
            "code_service",
        )
        ordering = ["-created_at"]
    
    def __str__(self):
        return f'Service: {self.name} | Price: {self.price} | Category: {self.category} | Email: {self.email}'
    
class CommentService(models.Model):
    text = models.TextField(
        validators=[
            MinLengthValidator(10, "El comentario debe ser mayor de 10 caracteres")
        ]
    )
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)