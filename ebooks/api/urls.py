from django.urls import path
from ebooks.api.views import EbookListCreateAPIView, ReviewCreateAPIView, ReviewDetailAPIView ,EbookListCreateAPIView

urlpatterns = [
    path("ebooks/", EbookListCreateAPIView.as_view(), name="ebook-list"),
    path("ebooks/<int:pk>/", EbookListCreateAPIView.as_view(), name="ebook-detail"),
    path("ebooks/<int:ebook_pk>/", ReviewCreateAPIView.as_view(), name="ebook-review"),
    path("reviews/<int:pk>/", ReviewDetailAPIView.as_view(), name="review-detail"),

]

