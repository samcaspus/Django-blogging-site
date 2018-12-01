from django.db import models

class blogs(models.Model):
    user = models.CharField(max_length=100)
    heading = models.CharField(max_length=100)
    content = models.CharField(max_length=400)
