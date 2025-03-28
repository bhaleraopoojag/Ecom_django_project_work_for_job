# Generated by Django 5.1.5 on 2025-02-23 08:09

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("billing", "0002_alter_billingprofilemodel_user"),
        ("orders", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="ordermodel",
            name="active",
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name="ordermodel",
            name="billing_profile",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="billing.billingprofilemodel",
            ),
        ),
    ]
