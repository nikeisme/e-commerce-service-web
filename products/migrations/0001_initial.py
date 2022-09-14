# Generated by Django 4.1.1 on 2022-09-14 10:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Product",
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
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("name", models.CharField(max_length=200)),
                (
                    "price",
                    models.DecimalField(decimal_places=2, default=0, max_digits=13),
                ),
                ("stock", models.IntegerField(default=1)),
            ],
            options={"db_table": "products",},
        ),
    ]