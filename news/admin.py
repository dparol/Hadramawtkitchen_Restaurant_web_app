from django.contrib import admin
from .models import News

# Register your models here.

class News_modeladmin(admin.ModelAdmin):
    list_display  = ('news_title',  'news_posted_by',  'news_date', 'news_about',  'news_about', 'news_comments_count', 'news_image'  )
    list_filter   = ('news_title', 'news_posted_by', 'news_date', 'news_about', 'news_about', 'news_comments_count', 'news_image' )
    search_fields = ('news_title',  'news_posted_by',  'news_date', 'news_about',  'news_about', 'news_comments_count', 'news_image' )
    list_per_page = 25

admin.site.register(News, News_modeladmin)