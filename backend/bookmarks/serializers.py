from rest_framework import serializers

from backend.bookmarks.models import Bookmark


class BookmarkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bookmark
        fields = ["id", "name", "description", "url", "website"]
