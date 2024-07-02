from django.urls import path
from .views import CartItemSubclass2Views

urlpatterns = [
    path("cart-items/", CartItemSubclass2Views.as_view({
        "get": "list", 
        "post": "create", 
        #"put": "update", 
        #"patch": "partial_update",
        #"delete": "destroy",
        })
    ),
    #path('cart-items/<int:pk>/', CartItemSubclass2DetailViews.as_view()),
]