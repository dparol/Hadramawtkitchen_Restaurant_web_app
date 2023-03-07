from django.contrib import admin
from .models import Offer

# Register your models here.

class Offermodeladmin(admin.ModelAdmin):
    list_display  = ('offer_date', 'offer_title', 'offer_descp', 'price', 'offer_price', 'offer_percentage' )
    list_filter   = ('offer_date', 'offer_title', 'offer_descp', 'price', 'offer_price', 'offer_percentage' )
    search_fields = ('offer_date', 'offer_title', 'offer_descp', 'price', 'offer_price', 'offer_percentage' )
    list_per_page = 25

admin.site.register(Offer, Offermodeladmin)