from django.db import models


class NoteType(models.TextChoices):
    USER = ("USER", "User Note")
    BOOKMARK = ("BOOKMARK", "Bookmark Note")