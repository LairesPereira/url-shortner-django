# Generated by Django 5.0.6 on 2024-05-16 00:14

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("urlshortnerapp", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="shorturl",
            name="originalUrl",
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name="shorturl",
            name="shortUrl",
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.DeleteModel(
            name="OriginalUrl",
        ),
    ]
