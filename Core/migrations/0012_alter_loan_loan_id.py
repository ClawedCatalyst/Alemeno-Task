# Generated by Django 5.0 on 2023-12-13 15:07

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("Core", "0011_remove_loan_id_alter_loan_loan_id"),
    ]

    operations = [
        migrations.AlterField(
            model_name="loan",
            name="loan_id",
            field=models.AutoField(
                db_column="loan_id", primary_key=True, serialize=False
            ),
        ),
    ]