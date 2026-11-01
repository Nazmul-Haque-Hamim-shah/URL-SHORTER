from django.db import models

# Create your models here.
class Api_Storage(models.Model):
    original_url = models.CharField(max_length = 300)
    short_code = models.CharField(max_length = 150,unique=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    clicks = models.IntegerField(default=0)
    
    
    

