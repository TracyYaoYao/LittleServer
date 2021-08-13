from django.db import models

# Create your models here.

class ClientInfo(models.Model):
    id = models.CharField(max_length=30, primary_key=True)
    key = models.CharField(max_length=30)

    def __str__(self):
        return self.id