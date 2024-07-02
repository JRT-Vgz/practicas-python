from rest_framework.viewsets import ModelViewSet
from rest_framework.pagination import PageNumberPagination
from .serializers import CartItemSubclass2Serializer

from .models import CartItemSubclass2

# curl -X PATCH http://127.0.0.1:8000/apisubclass/cart-items/1/ -H 'Content-Type: application/json' -d '{"product_quantity":10}'

# Create your views here.
class CartItemSubclass2Views(ModelViewSet):
    serializer_class = CartItemSubclass2Serializer
    pagination_class = PageNumberPagination
    
    def get_queryset(self):
        return CartItemSubclass2.objects.all()
    

