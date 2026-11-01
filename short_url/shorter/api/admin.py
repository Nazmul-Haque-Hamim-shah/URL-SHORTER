from django.contrib import admin
from .models import Api_Storage
# Register your models here.

@admin.register(Api_Storage)
class API_ADMIN(admin.ModelAdmin):
    list_display=("id","original_url","short_code","clicks","created_at")
