from rest_framework import serializers

from .models import CartItemSubclass

class CartItemSubclassSerializer(serializers.ModelSerializer):
    product_name = serializers.CharField(max_length=200)
    product_price = serializers.FloatField()
    product_quantity = serializers.IntegerField(required=False, default=1)
    
    class Meta:
        model = CartItemSubclass
        fields = "__all__"