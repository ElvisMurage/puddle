# Generated by Django 4.2.12 on 2024-05-10 15:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("item", "0002_alter_category_options_item"),
    ]

    operations = [
        migrations.AddField(
            model_name="item",
            name="name",
            field=models.CharField(default="noname", max_length=255),
        ),
    ]
