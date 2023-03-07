from django.db import models
from categories.models import CategoryMain

# Create your models here.

class FoodItems(models.Model):
    item_name      = models.CharField(max_length=500)
    slug           = models.SlugField(max_length=100, unique=True)
    item_category  = models.ForeignKey(CategoryMain, on_delete=models.CASCADE)
    item_decsp     = models.TextField(max_length=5000)
    item_price     = models.CharField(max_length=500)
    item_cover_pic = models.ImageField(upload_to='Food_Products/images', blank=True) 

    def __str__(self):
        return self.item_name








