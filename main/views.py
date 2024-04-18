import requests
from django.http import JsonResponse
from rest_framework.response import Response
from django.shortcuts import render, redirect
from rest_framework import status, generics, filters
from rest_framework.decorators import api_view
from products.models import Product
from products.serializer import ProductSerializer

@api_view(['GET'])
def getHomeData(request):
    try:
        highest_rated_products = Product.objects.order_by('-avg_rate')[:3]
        latest_products = Product.objects.order_by('-id')[:8]
        
        highest_serializer = ProductSerializer(highest_rated_products, many=True)
        latest_serializer = ProductSerializer(latest_products, many=True)
        
        result = {
            'highest_rated_products': highest_serializer.data,
            'latest_products': latest_serializer.data
        }
        
        return Response(result, status=status.HTTP_200_OK)
    
    except Exception as e:
        error_message = str(e)
        return Response({'error': error_message}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

# # Upload image to Imgur
# client_id = 'YOUR_CLIENT_ID'
# image_path = 'path/to/your/image.jpg'
# headers = {'Authorization': f'Client-ID {client_id}'}
# files = {'image': open(image_path, 'rb')}
# response = requests.post('https://api.imgur.com/3/upload', headers=headers, files=files)
# data = response.json()

# # Get URL to access the uploaded image
# image_url = data['data']['link']
# print(image_url)

# views.py
import requests
from django.http import JsonResponse

def upload_to_imgur(request):
    if request.method == 'POST' and request.FILES.get('image'):
        client_id = 'your_key'  # Replace with your Imgur client ID
        image_file = request.FILES['image']

        headers = {'Authorization': f'Client-ID {client_id}'}
        files = {'image': image_file}

        response = requests.post('https://api.imgur.com/3/upload', headers=headers, files=files)
        data = response.json()

        if response.status_code == 200:
            image_url = data['data']['link']
            return JsonResponse({'image_url': image_url})
        else:
            return JsonResponse({'error': 'Failed to upload image to Imgur'}, status=response.status_code)
    else:
        return JsonResponse({'error': 'Please send a POST request with an image file.'}, status=400)

def upload_view(request):
	return render(request, 'general/upload_view.html')