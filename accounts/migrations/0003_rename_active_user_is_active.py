# Generated by Django 5.1.5 on 2025-03-25 08:40

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("accounts", "0002_user_full_name"),
    ]

    operations = [
        migrations.RenameField(
            model_name="user",
            old_name="active",
            new_name="is_active",
        ),
    ]
