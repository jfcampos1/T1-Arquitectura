from django.db import models

# Create your models here.

class Comment(models.Model):
    text = models.CharField(max_length=200)
    ip_address = models.GenericIPAddressField()
    created_date = models.DateTimeField()

    def __str__(self):
        return self.text
