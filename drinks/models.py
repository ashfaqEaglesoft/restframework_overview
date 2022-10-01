from django.db import models

class drinks(models.Model):
    name=models.CharField(max_length=200)
    des=models.CharField(max_length=500)
    def __str__(self):
        return self.name