# Generated by Django 4.1.5 on 2023-01-14 15:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('weekly_offer', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='offer',
            name='offer_banner',
            field=models.ImageField(blank=True, upload_to='Offer_weekly/images'),
        ),
        migrations.AddField(
            model_name='offer',
            name='offer_percentage',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='offer',
            name='offer_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='offer',
            name='offer_descp',
            field=models.TextField(blank=True, max_length=5000, null=True),
        ),
        migrations.AlterField(
            model_name='offer',
            name='offer_price',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='offer',
            name='offer_title',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='offer',
            name='price',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]