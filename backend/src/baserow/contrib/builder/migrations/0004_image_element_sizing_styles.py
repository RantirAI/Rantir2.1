# Generated by Django 4.0.10 on 2024-01-23 14:57

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("builder", "0003_heading_text_alignment"),
    ]

    operations = [
        migrations.AddField(
            model_name="imageelement",
            name="style_image_constraint",
            field=models.CharField(
                choices=[
                    ("cover", "Cover"),
                    ("contain", "Contain"),
                    ("full-width", "Full Width"),
                ],
                default="contain",
                help_text="The image constraint to apply to this image",
                max_length=32,
            ),
        ),
        migrations.AddField(
            model_name="imageelement",
            name="style_max_height",
            field=models.PositiveIntegerField(
                help_text="The max-height for this image element.",
                null=True,
                validators=[
                    django.core.validators.MinValueValidator(
                        5, message="Value cannot be less than 5."
                    ),
                    django.core.validators.MaxValueValidator(
                        3000, message="Value cannot be greater than 3000."
                    ),
                ],
            ),
        ),
        migrations.AddField(
            model_name="imageelement",
            name="style_max_width",
            field=models.PositiveIntegerField(
                default=100,
                help_text="The max-width for this image element.",
                null=True,
                validators=[
                    django.core.validators.MinValueValidator(
                        0, message="Value cannot be less than 0."
                    ),
                    django.core.validators.MaxValueValidator(
                        100, message="Value cannot be greater than 100."
                    ),
                ],
            ),
        ),
    ]
