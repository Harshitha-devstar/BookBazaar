# Generated by Django 5.1 on 2024-11-09 19:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("baseapp", "0003_user_dob_user_gender_user_phone_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="gender",
            field=models.CharField(
                blank=True,
                choices=[("F", "Female"), ("M", "Male"), ("N", "Prefer Not Say")],
                max_length=1,
                null=True,
            ),
        ),
    ]
