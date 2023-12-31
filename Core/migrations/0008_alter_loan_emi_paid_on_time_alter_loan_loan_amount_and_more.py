# Generated by Django 5.0 on 2023-12-12 17:19

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("Core", "0007_remove_customer_monthy_salary_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="loan",
            name="emi_paid_on_time",
            field=models.BigIntegerField(),
        ),
        migrations.AlterField(
            model_name="loan",
            name="loan_amount",
            field=models.BigIntegerField(),
        ),
        migrations.AlterField(
            model_name="loan",
            name="loan_id",
            field=models.BigIntegerField(),
        ),
        migrations.AlterField(
            model_name="loan",
            name="monthly_emi",
            field=models.BigIntegerField(),
        ),
        migrations.AlterField(
            model_name="loan",
            name="tenure",
            field=models.BigIntegerField(),
        ),
    ]
