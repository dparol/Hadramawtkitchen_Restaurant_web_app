from django.db import models

# Create your models here.
class CategoryMain(models.Model):
    category_name = models.CharField(max_length=50, unique=True)
    category_descp = models.TextField(max_length=5000, blank=True)
    category_image = models.ImageField(upload_to='Category_images/', blank=True)
    
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
        ordering = ['category_name']

    def get_url(self):
            return reverse('products_by_category', args=[self.slug])

    def __str__(self):
        return self.category_name