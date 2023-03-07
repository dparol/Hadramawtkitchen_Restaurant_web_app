# Generated by Django 4.1.5 on 2023-01-14 15:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Offer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('offer_date', models.DateField(blank=True)),
                ('offer_title', models.CharField(max_length=500)),
                ('offer_descp', models.TextField(max_length=5000)),
                ('price', models.IntegerField()),
                ('offer_price', models.IntegerField()),
            ],
        ),
    ]