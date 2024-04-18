from django.contrib import admin
from .models import Product
import requests
import environ
import os
from dotenv import load_dotenv

env = environ.Env()
environ.Env.read_env()
load_dotenv()

class ProductAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        # Call the parent save_model method to save the object
        
        client_id = env('Client_id')   
        
        image_file =  obj.thumbnail # Access the uploaded image file from the model instance

        headers = {'Authorization': f'Client-ID {client_id}'}
        files = {'image': image_file}

        response = requests.post('https://api.imgur.com/3/upload', headers=headers, files=files)
        data = response.json()

        # if response.status_code == 200:
        obj.thumbnail = data['data']['link']
            
        super().save_model(request, obj, form, change)

admin.site.register(Product, ProductAdmin)
