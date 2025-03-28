# Generated by Django 5.1.5 on 2025-02-15 08:56

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("products", "0018_productmodel_timestamp"),
    ]

    operations = [
        migrations.CreateModel(
            name="TagModel",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=120)),
                ("slug", models.SlugField()),
                ("timestamp", models.DateTimeField(auto_now_add=True)),
                ("active", models.BooleanField(default=True)),
                (
                    "products",
                    models.ManyToManyField(blank=True, to="products.productmodel"),
                ),
            ],
        ),
    ]
