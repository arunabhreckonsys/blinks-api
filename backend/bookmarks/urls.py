from django.urls import path

from backend.bookmarks.views import GetBookmarksAPI, CreateBookmarksAPI

urlpatterns = [
    path("bookmarks", GetBookmarksAPI.as_view(), name="get_bookmarks"),
    path("bookmarks/create", CreateBookmarksAPI.as_view(), name="create_bookmarks")
]