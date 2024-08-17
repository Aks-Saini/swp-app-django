# Generated by Django 4.2.13 on 2024-08-09 13:43

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("api_shipper", "0010_alter_approval_link"),
    ]

    operations = [
        migrations.AddField(
            model_name="approval",
            name="status",
            field=models.CharField(
                choices=[("pending", "Pending Admin Approval"), ("approved", "Approved"), ("rejected", "Rejected")],
                default="pending",
                editable=False,
                max_length=20,
            ),
        ),
        migrations.AlterField(
            model_name="approval",
            name="link",
            field=models.URLField(default="http://localhost:8081/visualization/warn/"),
        ),
    ]
