# Generated by Django 5.0 on 2023-12-13 15:00

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("Core", "0010_alter_loan_emi_paid_on_time_alter_loan_end_date_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="loan",
            name="id",
        ),
        migrations.AlterField(
            model_name="loan",
            name="loan_id",
            field=models.AutoField(
                db_column="customer_id", primary_key=True, serialize=False
            ),
        ),
    ]
