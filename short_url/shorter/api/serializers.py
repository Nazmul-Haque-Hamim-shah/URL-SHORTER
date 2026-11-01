from rest_framework import serializers
from .models import Api_Storage

class APi_Storage_Serializer(serializers.ModelSerializer):
    class Meta:
        model=Api_Storage
        exclude=['clicks','short_code']
        
        
        
