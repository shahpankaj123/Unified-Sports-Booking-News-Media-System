# Generated by Django 5.2 on 2025-06-14 07:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0011_notification'),
    ]

    operations = [
        migrations.AddField(
            model_name='notification',
            name='IsRead',
            field=models.BooleanField(default=False),
        ),
    ]
