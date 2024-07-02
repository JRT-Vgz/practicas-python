from rest_framework import serializers

from .models import CartItemSubclass2

class CartItemSubclass2Serializer(serializers.ModelSerializer):
    product_name = serializers.CharField(max_length=200)
    product_price = serializers.FloatField()
    product_quantity = serializers.IntegerField(required=False, default=1)
    
    class Meta:
        model = CartItemSubclass2
        fields = "__all__"