from django.urls import path
from .views import ClientAPI, ClientDetailAPI, BlogAPI, BlogDetailAPI, SponsorAPI, SponsorDetailAPI

urlpatterns = [
    path('client/', ClientAPI.as_view()),
    path('client/<int:pk>/', ClientDetailAPI.as_view()),
    path('blog/<int:pk>/', BlogDetailAPI.as_view()),
    path('blog/', BlogAPI.as_view()),
    path('sponsor/', SponsorAPI.as_view()),
    path('sponsor/<int:pk>/', SponsorDetailAPI.as_view())
]