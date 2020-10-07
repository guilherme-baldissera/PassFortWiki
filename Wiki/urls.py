from django.urls import path
from .views import get_all_documents, get_all_reviews_or_add_review, get_document_by_timestamp, get_the_latest_document

urlpatterns = [
    path('documents', get_all_documents),
    path('documents/<str:title>', get_all_reviews_or_add_review),
    path('documents/<str:title>/<int:timestamp>', get_document_by_timestamp),
    path('documents/<str:title>/latest', get_the_latest_document),
]
