from django.db import models

from core.models import BaseModel


# Create your models here.
class Folder(BaseModel):
    name = models.CharField(max_length=150)
    description = models.TextField(blank=True, null=True)
    type = models.CharField(max_length=150)
    icon = models.CharField(max_length=120, blank=True, null=True)
    cover_image = models.FileField(upload_to="/cover-images", blank=True, null=True)
    # user = models.ForeignKey(Use)
    color = models.CharField(max_length=7)
    parent_folder = models.ForeignKey(
        "self",
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name="sub_folders",
    )
