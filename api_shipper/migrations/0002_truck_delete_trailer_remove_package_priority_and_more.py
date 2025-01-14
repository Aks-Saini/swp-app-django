# Generated by Django 4.2.13 on 2024-08-06 08:42

import uuid

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("api_shipper", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Truck",
            fields=[
                ("id", models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ("length", models.DecimalField(decimal_places=2, max_digits=6)),
                ("breadth", models.DecimalField(decimal_places=2, max_digits=6)),
                ("height", models.DecimalField(decimal_places=2, max_digits=6)),
                ("tare_weight", models.DecimalField(decimal_places=2, max_digits=10)),
                ("gvwr", models.DecimalField(decimal_places=2, max_digits=10)),
                ("axle_weight_ratings", models.JSONField()),
                ("axle_group_weight_ratings", models.JSONField()),
                ("wheel_load_capacity", models.DecimalField(decimal_places=2, max_digits=10)),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("entered", "Entered the Inventory"),
                            ("loaded", "Allocated Packages"),
                            ("dispatched", "Dispatched"),
                        ],
                        default="inventory",
                        editable=False,
                        max_length=20,
                    ),
                ),
            ],
        ),
        migrations.DeleteModel(
            name="Trailer",
        ),
        migrations.RemoveField(
            model_name="package",
            name="priority",
        ),
        migrations.AddField(
            model_name="package",
            name="status",
            field=models.CharField(
                choices=[("inventory", "Inventory"), ("allocated", "Allocated to Truck"), ("dispatched", "Dispatched")],
                default="inventory",
                editable=False,
                max_length=20,
            ),
        ),
        migrations.AlterField(
            model_name="package",
            name="breadth",
            field=models.DecimalField(decimal_places=2, max_digits=5),
        ),
        migrations.AlterField(
            model_name="package",
            name="height",
            field=models.DecimalField(decimal_places=2, max_digits=5),
        ),
        migrations.AlterField(
            model_name="package",
            name="length",
            field=models.DecimalField(decimal_places=2, max_digits=5),
        ),
        migrations.AlterField(
            model_name="package",
            name="weight",
            field=models.DecimalField(decimal_places=2, max_digits=6),
        ),
        migrations.AddField(
            model_name="package",
            name="allocation",
            field=models.ForeignKey(
                blank=True,
                default=None,
                editable=False,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="api_shipper.truck",
            ),
        ),
    ]
