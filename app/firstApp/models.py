from django.db import models
from django.utils import timezone

# Create your models here.

class AppVariety(models.Model):
    APP_TYPE_CHOICE =[
        ('ML', 'MACHINE_LEARNING'),
        ('FT', 'FINTECH'),
        ('SI', 'SOFTWARE_INDUSTRY'),
    ]
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to = 'applications/')
    date_added = models.DateTimeField(default=timezone.now)
    type = models.CharField(max_length=2, choices=APP_TYPE_CHOICE)
