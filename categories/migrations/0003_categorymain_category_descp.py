# Generated by Django 4.1.5 on 2023-01-12 15:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('categories', '0002_remove_categorymain_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='categorymain',
            name='category_descp',
            field=models.TextField(blank=True, max_length=5000),
        ),
    ]
