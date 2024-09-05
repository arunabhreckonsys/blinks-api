from django.db import models

from core.models import BaseModel


# Create your models here.
class Website(BaseModel):
    name = models.CharField(max_length=256, unique=True)
    description = models.TextField(blank=True, null=True)
    icon = models.CharField(max_length=120, blank=True, null=True)
    url = models.URLField(max_length=300, unique=True)