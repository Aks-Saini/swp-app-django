# Generated by Django 4.2.13 on 2024-08-09 10:22

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("api_shipper", "0005_alter_package_allocation"),
    ]

    operations = [
        migrations.AddField(
            model_name="package",
            name="stock",
            field=models.IntegerField(default=2),
            preserve_default=False,
        ),
    ]
