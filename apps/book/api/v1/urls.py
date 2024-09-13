from django.urls import path
from .views import (
    BookListCreateAPIView,
    BookRetrieveUpdateDestroyAPIView,
    PublisherListCreateAPIView,PublisherRetrieveUpdateDestroyAPIView
)

urlpatterns = [
    path( "api/v1/book", BookListCreateAPIView.as_view(), name="book", ),
    path( "api/v1/book/<int:pk>", BookRetrieveUpdateDestroyAPIView.as_view(), name="book", ),
    path( "api/v1/publisher", PublisherListCreateAPIView.as_view(), name="publisher", ),
    path( "api/v1/publisher/<int:pk>", PublisherRetrieveUpdateDestroyAPIView.as_view(), name="publisher", ),
]
