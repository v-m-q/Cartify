from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from .models import Category
from .serializer import CategorySerializer

@api_view(['GET'])
def Categories(request):
    try:
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)