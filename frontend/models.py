from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class AlkibiadesUser(AbstractUser):
    email = models.EmailField(unique=True)
    biography = models.TextField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email
    
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField(max_length=500)
    author = models.ForeignKey(AlkibiadesUser, on_delete=models.CASCADE, related_name='posts')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
