# Generated by Django 4.2 on 2023-04-20 15:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("professional", "0003_review"),
    ]

    operations = [
        migrations.CreateModel(
            name="ContactInfo",
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
                (
                    "phone_number",
                    models.CharField(
                        blank=True,
                        max_length=20,
                        null=True,
                        verbose_name="Phone number",
                    ),
                ),
                ("email", models.EmailField(max_length=254, verbose_name="Email")),
                (
                    "website",
                    models.URLField(blank=True, null=True, verbose_name="Website"),
                ),
                (
                    "instagram_handle",
                    models.CharField(
                        blank=True,
                        max_length=30,
                        null=True,
                        verbose_name="Instagram handle",
                    ),
                ),
                (
                    "diveplus_handle",
                    models.CharField(
                        blank=True,
                        max_length=30,
                        null=True,
                        verbose_name="Dive+ handle",
                    ),
                ),
                (
                    "professional",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="contact_info",
                        to="professional.professional",
                    ),
                ),
            ],
        ),
    ]
