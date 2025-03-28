# Generated by Django 5.1.5 on 2025-02-13 07:19

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("products", "0017_alter_productmodel_slug"),
    ]

    operations = [
        migrations.AddField(
            model_name="productmodel",
            name="timestamp",
            field=models.DateTimeField(
                auto_now_add=True, default=django.utils.timezone.now
            ),
            preserve_default=False,
        ),
    ]
