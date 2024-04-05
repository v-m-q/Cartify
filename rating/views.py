from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from products.models import Product
from .serializer import RatingSerializer

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def rate_product(request, product_id):
    try:
        product = Product.objects.get(product_id=product_id)

        serializer = RatingSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user, product=product)
            
            product.avg_rate = product.calculate_avg_rating()
            product.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
    except Exception as e:
        return Response(str(e), status=status.HTTP_500_INTERNAL_SERVER_ERROR)
