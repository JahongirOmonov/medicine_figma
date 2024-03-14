# Generated by Django 4.2.7 on 2024-03-13 10:40

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0003_remove_user_name_user_first_name_user_last_name"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="first_name",
            field=models.CharField(blank=True, default=None, max_length=31, null=True),
        ),
        migrations.AlterField(
            model_name="user",
            name="last_name",
            field=models.CharField(blank=True, default=None, max_length=31, null=True),
        ),
    ]
