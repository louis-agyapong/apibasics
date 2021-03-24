from django.urls import path
from . import apiviews

urlpatterns = [
    path("author/", apiviews.AuthorListView.as_view()),
    path("author/<int:pk>/", apiviews.AuthorDetailView.as_view()),
    path("book/", apiviews.BookListView.as_view()),
    path("book/<int:pk>/", apiviews.BookDetailView.as_view()),
]
