from django.db import models

from backend.websites.models import Website
from core.models import BaseModel


# Create your models here.
class Bookmark(BaseModel):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    url = models.URLField(max_length=1000)
    website = models.ForeignKey(Website, related_name="bookmarks", on_delete=models.CASCADE)


class BookmarkSummary(BaseModel):
    bookmark = models.ForeignKey(Bookmark, related_name="summaries", on_delete=models.CASCADE)
    type = models.CharField(max_length=128)
    summary = models.TextField()