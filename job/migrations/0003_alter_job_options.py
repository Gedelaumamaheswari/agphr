# Generated by Django 4.2 on 2024-10-05 09:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0002_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='job',
            options={'ordering': ['-id'], 'verbose_name': 'Job Post', 'verbose_name_plural': 'Job Posts'},
        ),
    ]