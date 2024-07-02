from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListCreateAPIView
from rest_framework.pagination import PageNumberPagination
from .serializers import CartItemSubclassSerializer

from .models import CartItemSubclass

# curl -X PATCH http://127.0.0.1:8000/apisubclass/cart-items/1/ -H 'Content-Type: application/json' -d '{"product_quantity":10}'

# Create your views here.
class CartItemSubclassListViews(ListCreateAPIView):
    serializer_class = CartItemSubclassSerializer
    pagination_class = PageNumberPagination
    
    def get_queryset(self):
        return CartItemSubclass.objects.all()
    
    
class CartItemSubclassDetailViews(RetrieveUpdateDestroyAPIView):
    serializer_class = CartItemSubclassSerializer
    pagination_class = PageNumberPagination
    
    def get_queryset(self):
        return CartItemSubclass.objects.all()
