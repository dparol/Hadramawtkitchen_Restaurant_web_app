# Generated by Django 4.1.5 on 2023-01-12 15:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('categories', '0003_categorymain_category_descp'),
    ]

    operations = [
        migrations.AddField(
            model_name='categorymain',
            name='category_image',
            field=models.ImageField(blank=True, upload_to='Category_images/'),
        ),
    ]