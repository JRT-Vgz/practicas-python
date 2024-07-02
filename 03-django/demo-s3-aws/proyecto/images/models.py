from django.db import models

# Create your models here.
class Image(models.Model):
    name = models.CharField(max_length=255, null=False, blank=False)
    image = models.ImageField(upload_to="images")
    created_at = models.DateTimeField(auto_now_add=True)