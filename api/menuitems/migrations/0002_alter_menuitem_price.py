# Generated by Django 4.2 on 2023-04-14 12:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("menuitems", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="menuitem",
            name="price",
            field=models.DecimalField(db_index=True, decimal_places=2, max_digits=10),
        ),
    ]