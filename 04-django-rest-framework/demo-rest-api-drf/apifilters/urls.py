from django.urls import path
from .views import QuestionsAPIView

urlpatterns = [
    path('questions/', QuestionsAPIView.as_view())
]