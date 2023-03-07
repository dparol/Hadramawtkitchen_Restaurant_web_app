from django.shortcuts import render
from django.http import HttpResponse
from .models import FoodItems
from categories.models import CategoryMain
from news.models import News
from weekly_offer.models import Offer

# Create your views here.
def homePage(request):
    products = FoodItems.objects.all()
    category = CategoryMain.objects.all()
    news = News.objects.all()
    # offerz = Offer.objects.latest('-id')

    context = {
        "food" : products,
        "categories" : category,
        "news" : news,
        # "offer" : offerz,
    }

    return render(request, 'home.html', context)

