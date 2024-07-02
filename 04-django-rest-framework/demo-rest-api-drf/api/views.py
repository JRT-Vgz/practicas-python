from django.shortcuts import get_object_or_404
from rest_framework.views import APIView 
from rest_framework.generics import GenericAPIView
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework import status
from .serializers import CartItemSerializer
from .models import CartItem

# curl -X POST -H "Content-Type: application/json" http://127.0.0.1:8000/api/cart-items/ -d "{\"product_name\":\"name\",\"product_price\":\"41\",\"product_quantity\":\"1\"}"
# curl -X GET http://127.0.0.1:8000/api/cart-items/
# curl -X PATCH http://127.0.0.1:8000/api/cart-items/1 -H 'Content-Type: application/json' -d '{"product_quantity":6}'
# curl -X "DELETE" http://127.0.0.1:8000/api/cart-items/1

# Create your views here.
# class CartItemViews(APIView):
class CartItemViews(GenericAPIView):
    serializer_class = CartItemSerializer
    pagination_class = PageNumberPagination
    
    def get_queryset(self):
        return CartItem.objects.all()
    
    def post(self, request):
        serializer = CartItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                "status": "success",
                "data": serializer.data,
                },
                status= status.HTTP_200_OK
                )
        else:
            return Response({
                "status": "error",
                "data": serializer.errors,
                },
                status= status.HTTP_400_BAD_REQUEST
            )
            
            
    def get(self, request, id=None):
        if id:
            item = get_object_or_404(CartItem, id=id)
            serializer = CartItemSerializer(item)
            return Response({
                "status": "success",
                "data": serializer.data,
            }, status=status.HTTP_200_OK
            )        
        items_count = CartItem.objects.count()
        items = CartItem.objects.all()
        serializer = CartItemSerializer(items, many=True)
        
        #return Response({"status": "success", "data": serializer.data, "count": items_count,}, status=status.HTTP_200_OK)
        
        return self.get_paginated_response({
            "status": "success", 
            "data": self.paginate_queryset(serializer.data)
        })
        
    
    def patch(self,request, id=None):
        item = get_object_or_404(CartItem, id=id)
        serializer = CartItemSerializer(item, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({
                "status": "success",
                "data": serializer.data,
                },
                status= status.HTTP_200_OK
                )
        else:
            return Response({
                "status": "error",
                "data": serializer.errors,
                },
                status= status.HTTP_400_BAD_REQUEST
            )
            
    
    def delete(self, request, id=None):
        item = get_object_or_404(CartItem, id=id)
        item.delete()
        return Response({
                "status": "success",
                "data": "Item Deleted",
                },
                status= status.HTTP_204_NO_CONTENT
                ) 