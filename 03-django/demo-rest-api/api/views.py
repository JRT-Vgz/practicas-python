import json
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.shortcuts import render
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.core.exceptions import ObjectDoesNotExist

from .models import CartItem

# curls para importar y testear las peticiones HTTP.
# curl -X POST -H "Content-Type: application/json" http://127.0.0.1:8000/cart-items/ -d "{\"product_name\":\"name\",\"product_price\":\"41\",\"product_quantity\":\"1\"}"
# curl -X GET http://127.0.0.1:8000/cart-items/
# curl -X PATCH http://127.0.0.1:8000/update-item/1 -H "Content-Type: application/json" -d "{\"product_quantity\":\"3\"}"
# curl -X "DELETE" http://127.0.0.1:8000/update-item/1


# Create your views here.
@method_decorator(csrf_exempt, name="dispatch")
class ShoppingCart(View):
    def post(self, request):
        data = json.loads(request.body.decode("utf-8"))
        
        p_name = data.get("product_name") 
        p_price = data.get("product_price")
        p_quantity = data.get("product_quantity")
        
        product_data = {
            "product_name": p_name,
            "product_price": p_price,
            "product_quantity": p_quantity,
        }
        
        cart_item = CartItem.objects.create(**product_data)
        
        data = {
            "message": f"New item added to Cart with id: {cart_item.id}"
        }        
        return JsonResponse(data, status=201)
    
    
    def get(self, request):
        items_count = CartItem.objects.count()
        items = CartItem.objects.all()
        
        items_data = []
        
        for item in items:
            items_data.append({
                "product_name": item.product_name,
                "product_price": item.product_price,
                "product_quantity": item.product_quantity,
            })
        
        data = {
            "items": items_data,
            "count": items_count,
        }    
        return JsonResponse(data)
    
    
@method_decorator(csrf_exempt, name="dispatch")    
class ShoppingCartUpdate(View):
    def patch(self, request, item_id):
        data = json.loads(request.body.decode("utf-8"))
        try:
            item = CartItem.objects.get(id = item_id)
        except ObjectDoesNotExist:
            data = {
                "message": "Item not found."
            }
            return JsonResponse(data, status=404)
            
        item.product_quantity = data["product_quantity"]
        item.save()
        
        data = {
            "message": f"Item {item_id} has been updated."
        }       
        return JsonResponse(data)
    
    def delete(self, request, item_id):
        item = CartItem.objects.get(id = item_id)
        item.delete()
        
        data = {
            "message": f"Item {item_id} has been deleted."
        }        
        return JsonResponse(data, status=204)