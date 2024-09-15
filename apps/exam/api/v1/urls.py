from django.urls import path
from .views import (
    ExamListCreateAPIView,
    ExamRetrieveUpdateDestroyAPIView,
    SubjectListCreateAPIView,SubjectRetrieveUpdateDestroyAPIView
)

urlpatterns = [
    path( "api/v1/exam", ExamListCreateAPIView.as_view(), name="exam", ),
    path( "api/v1/exam/<int:pk>", ExamRetrieveUpdateDestroyAPIView.as_view(), name="exam", ),
    path( "api/v1/subject", SubjectListCreateAPIView.as_view(), name="subject", ),
    path( "api/v1/subject/<int:pk>", SubjectRetrieveUpdateDestroyAPIView.as_view(), name="subject", ),
]
