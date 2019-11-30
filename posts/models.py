from django.db import models

# Create your models here.

class Post(models.Model):
    text = models.TextField()
    cover = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.text