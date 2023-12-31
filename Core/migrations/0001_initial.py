# Generated by Django 5.0 on 2023-12-12 15:57

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Customer",
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
                ("customer_id", models.IntegerField()),
                ("first_name", models.CharField(max_length=200)),
                ("last_name", models.CharField(max_length=200)),
                ("phone_number", models.IntegerField(max_length=10)),
                ("monthy_salary", models.IntegerField()),
                ("approved_limit", models.IntegerField()),
                ("current_debt", models.IntegerField()),
            ],
        ),
    ]
