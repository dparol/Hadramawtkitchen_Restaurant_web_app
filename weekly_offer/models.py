from django.db import models

# Create your models here.
class Offer(models.Model):
    offer_date = models.DateField(blank=True, null=True)
    offer_title = models.CharField(max_length=500, blank=True, null=True)
    offer_descp = models.TextField(max_length=5000, blank=True, null=True)
    price = models.IntegerField(blank=True, null=True)
    offer_price = models.IntegerField(blank=True, null=True)
    offer_percentage = models.IntegerField(blank=True, null=True)
    offer_banner = models.ImageField(upload_to='Offer_weekly/images', blank=True) 
    def __str__(self):
        return self.offer_title

