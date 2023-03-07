from django.contrib import admin
from .models import FoodItems

# Register your models here.

class FoodItems_modeladmin(admin.ModelAdmin):
    list_display  = ('item_name',  'item_category',  'item_price', 'item_cover_pic'  )
    list_filter   = ('item_name', 'item_cover_pic', 'item_category', 'item_price', )
    search_fields = ('item_name',  'item_category',  'item_price', 'item_cover_pic' )
    list_per_page = 25

admin.site.register(FoodItems, FoodItems_modeladmin)