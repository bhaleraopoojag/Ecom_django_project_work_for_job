# Generated by Django 5.1.5 on 2025-02-07 09:49

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("products", "0009_alter_productmodel_slug"),
    ]

    operations = [
        migrations.AlterField(
            model_name="productmodel",
            name="slug",
            field=models.SlugField(blank=True, unique=True),
        ),
    ]
