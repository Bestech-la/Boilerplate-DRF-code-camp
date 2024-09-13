from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from django_filters.rest_framework import DjangoFilterBackend
from apps.book.api.v1.filter import BookFilterSet, PublisherFilterSet
from apps.book.api.v1.serializers import BookSerializer, PublisherSerializer
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.parsers import MultiPartParser, FormParser

from apps.book.models import Book, Publisher

class BookListCreateAPIView(ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_class = BookFilterSet
    parser_classes = (MultiPartParser, FormParser)

class BookRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    parser_classes = (MultiPartParser, FormParser)


class PublisherListCreateAPIView(ListCreateAPIView):
    queryset = Publisher.objects.all()
    serializer_class = PublisherSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_class = PublisherFilterSet

class PublisherRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Publisher.objects.all()
    serializer_class = PublisherSerializer
