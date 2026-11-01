import random
import string

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Api_Storage
from .serializers import APi_Storage_Serializer
from django.shortcuts import redirect

class Home(APIView):
    def get(self,request):
        return Response({"msg":"Hello world!"},status=status.HTTP_200_OK) 
    
    
    
    
class Shorten(APIView):
    
    def post(self,request):
        data=APi_Storage_Serializer(data=request.data)
        
        if data.is_valid():
            characters=string.ascii_letters+string.digits
            
            short_code=''.join(
                random.choices(characters,k=6)
            )
            
            data.save(short_code=short_code)
            
            return Response(
                {
                     "message": "URL Shortened Successfully",
                     "URL":f"http://127.0.0.1:8000/shorty/s/{short_code}/"
                }
            )
        
        return Response(data.errors)
            
            
      
      

class Custoom(APIView):
    
    def post(self,request):
        
        text=request.data.get("text")
        original_url=request.data.get("original_url")
        
        Api_Storage.objects.create(original_url=original_url,short_code=text)
        
        return Response(
            {
                "message":"Url short done.",
                "URL":f"http://127.0.0.1:8000/shorty/s/{text}"
            }
        )      

    
class URL_Redirect(APIView):
    
    def get(self,request,short_code):
        
        try:
            url=Api_Storage.objects.get(short_code=short_code)
        
            url.clicks+=1
            url.save()
        
            return redirect(url.original_url)
        
        except Api_Storage.DoesNotExist:
            return Response({'msg':"Url not found"})
        
        

class URL_Display(APIView):
    
    def get(self,request):
        
        urls=Api_Storage.objects.all()
        
        URLS={}
        i=1
        for u in urls:
            URLS[f"Url{i}"]=f"http://127.0.0.1:8000/shorty/s/{u.short_code}"
            i+=1
            
            
        return Response({
            "msg":"All urls Display",
            "URLS":URLS
        })
            
        
        
        