from django.db import models

from core.models import BaseModel


# Create your models here.
class Note(BaseModel):
    name = models.CharField(max_length=255)
    type = models.CharField(max_length=255)
    content = models.TextField()

    def __str__(self):
        return self.name
