# Generated by Django 4.2 on 2023-04-20 15:21

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("professional", "0005_school_member_number"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="school",
            name="member_number",
        ),
    ]
