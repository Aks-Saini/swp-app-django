# Generated by Django 4.2.13 on 2024-08-06 09:41

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_shipper', '0002_truck_delete_trailer_remove_package_priority_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='package',
            name='deliver_date',
            field=models.DateField(default=datetime.datetime(2024, 8, 6, 9, 40, 53, 958761, tzinfo=datetime.timezone.utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='package',
            name='destination',
            field=models.CharField(default=datetime.datetime(2024, 8, 6, 9, 41, 1, 293959, tzinfo=datetime.timezone.utc), max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='truck',
            name='destination',
            field=models.CharField(default='chandigarh', max_length=50),
            preserve_default=False,
        ),
    ]