# Generated by Django 4.2.7 on 2024-01-04 16:03

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("userManagement", "0002_alter_account_account_status"),
    ]

    operations = [
        migrations.RenameField(
            model_name="account",
            old_name="Account_status",
            new_name="account_status",
        ),
    ]