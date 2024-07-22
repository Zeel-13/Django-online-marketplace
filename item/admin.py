from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Category)

class ItemAdmin(admin.ModelAdmin):
    list_display=['name','category']
admin.site.register(Item,ItemAdmin)
