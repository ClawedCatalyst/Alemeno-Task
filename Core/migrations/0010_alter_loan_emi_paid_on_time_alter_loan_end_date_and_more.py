# Generated by Django 5.0 on 2023-12-13 14:47

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("Core", "0009_alter_loan_interest_rate"),
    ]

    operations = [
        migrations.AlterField(
            model_name="loan",
            name="emi_paid_on_time",
            field=models.BigIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name="loan",
            name="end_date",
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="loan",
            name="start_date",
            field=models.DateField(auto_now_add=True),
        ),
    ]