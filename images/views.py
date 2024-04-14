from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from .models import Images
from .serializer import ImagesSerializer


@api_view(['GET'])
def productImages(request, ProductId):
    try:
        product_images = Images.objects.filter(product_id=ProductId)
        serializer = ImagesSerializer(product_images,  many=True)
        print(product_images)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except Exception as e:
        return Response(status=status.HTTP_404_NOT_FOUND)