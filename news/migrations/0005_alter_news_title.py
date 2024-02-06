# Generated by Django 4.2.3 on 2024-01-08 19:36

import django.core.validators
from django.db import migrations, models
import news.models


class Migration(migrations.Migration):
    dependencies = [
        ("news", "0004_remove_news_categoties_news_categories"),
    ]

    operations = [
        migrations.AlterField(
            model_name="news",
            name="title",
            field=models.CharField(
                max_length=200,
                validators=[
                    django.core.validators.MinLengthValidator(2),
                    news.models.validate_title,
                ],
            ),
        ),
    ]
