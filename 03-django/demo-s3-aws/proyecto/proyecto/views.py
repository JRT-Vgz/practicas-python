from django.shortcuts import render
# from storages.backends.s3boto3 import S3Boto3Storage

# from .storage import PublicMediaStorage
from images.models import Image

def index(request):
    
    if request.method == "POST" and request.FILES.get("imagen"):
        image = request.FILES("imagen")
        
        # Las siguientes tres lineas no son necesarias una vez gestionamos la subida de archivo mediante un modelo que hereda
        # de S3Boto3Storage
        # storage = S3Boto3Storage()
        # image_path = f"{image.name}"
        # storage.save(image_path, image)
        
        aws_image = Image.objects.create(
            name=image.name,
            image=image
        )        
        
        image_url = aws_image.image.url
        
    return render(request, "index.html", {
        "image_url": image_url,
    })