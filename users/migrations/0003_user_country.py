# Generated by Django 4.2 on 2024-10-05 16:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_user_address_line_1_user_address_line_2_user_city_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='country',
            field=models.CharField(blank=True, help_text='Your current country.', max_length=100, null=True, verbose_name='Country'),
        ),
    ]