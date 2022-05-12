from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=255)
    resume = models.CharField(max_length=255)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.PROTECT)
    create_at = models.DateField(auto_now_add=True)