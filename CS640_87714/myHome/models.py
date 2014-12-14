from django.db import models

# Create your models here.

class DEVELOPMENT(models.Model):
    name=models.CharField(max_length=30, primary_key=True)
    content=models.TextField(blank=True)

class PRODUCTION(models.Model):
    name=models.CharField(max_length=30, primary_key=True)
    content=models.TextField(blank=True)

