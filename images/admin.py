from django.contrib import admin
from images.models import Images
import requests

class ImagesAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        # Call the parent save_model method to save the object
        
        client_id = 'acc328def3e5178'  
        image_file =  obj.image # Access the uploaded image file from the model instance

        headers = {'Authorization': f'Client-ID {client_id}'}
        files = {'image': image_file}

        response = requests.post('https://api.imgur.com/3/upload', headers=headers, files=files)
        data = response.json()

        # if response.status_code == 200:
        obj.image = data['data']['link']
            
        super().save_model(request, obj, form, change)

admin.site.register(Images, ImagesAdmin)
