from django.contrib import admin
from .models import CategoryMain

# Register your models here.

class CategoryMain_modeladmin(admin.ModelAdmin):
    list_display  = ('category_name', 'category_image', 'category_descp', )
    list_filter   = ('category_name','category_descp')
    search_fields = ('category_name', )
    list_per_page = 25

admin.site.register(CategoryMain, CategoryMain_modeladmin)