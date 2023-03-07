from django.db import models

# Create your models here.
class News(models.Model):
    
    news_title = models.CharField(max_length=1500)
    news_posted_by = models.CharField(max_length=1500)
    news_date = models.DateTimeField(auto_now_add=True)
    news_about = models.CharField(max_length=1500)
    news_image = models.ImageField(upload_to='news_images/', blank=True)
    news_comments_count = models.IntegerField()

    def __str__(self):
        return self.news_title