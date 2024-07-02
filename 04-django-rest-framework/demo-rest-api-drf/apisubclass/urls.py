from django.urls import path
from .views import CartItemSubclassDetailViews, CartItemSubclassListViews

urlpatterns = [
    path("cart-items/", CartItemSubclassListViews.as_view()),
    path('cart-items/<int:pk>/', CartItemSubclassDetailViews.as_view()),
]