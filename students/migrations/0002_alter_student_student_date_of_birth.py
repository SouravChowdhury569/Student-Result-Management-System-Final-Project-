# Generated by Django 5.1.4 on 2024-12-30 12:59

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("students", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="student",
            name="student_date_of_birth",
            field=models.DateField(default=datetime.date(2024, 12, 30)),
        ),
    ]