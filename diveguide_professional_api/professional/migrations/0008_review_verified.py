# Generated by Django 4.2 on 2023-04-20 15:41

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("professional", "0007_remove_professional_schools_schoolmembership"),
    ]

    operations = [
        migrations.AddField(
            model_name="review",
            name="verified",
            field=models.BooleanField(default=False, verbose_name="Verified"),
        ),
    ]
