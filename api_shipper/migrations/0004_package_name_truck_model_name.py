# Generated by Django 4.2.13 on 2024-08-06 16:25

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("api_shipper", "0003_package_deliver_date_package_destination_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="package",
            name="name",
            field=models.CharField(default="abc", max_length=20, unique=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="truck",
            name="model_name",
            field=models.CharField(default="bcd", max_length=20, unique=True),
            preserve_default=False,
        ),
    ]
