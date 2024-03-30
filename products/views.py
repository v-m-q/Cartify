from django.http import JsonResponse
from .models import Product
from .serializer import ProductSerializer

# /products 
def products(request):
  products   = Product.objects.all()
  serializer = ProductSerializer(products, many=True)
  return JsonResponse(serializer.data, safe=False)